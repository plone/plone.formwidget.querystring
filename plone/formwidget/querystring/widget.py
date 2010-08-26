from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.interface import implements, implementer
from plone.app.collection import queryparser
from plone.app.contentlisting.interfaces import IContentListing
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

import z3c.form.interfaces
import z3c.form.util

from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget

from plone.app.collection.interfaces import ICollectionRegistryReader
from plone.formwidget.querystring.interfaces import IQueryStringWidget
from plone.registry.interfaces import IRegistry



class QueryStringWidget(Widget):
    implements(IQueryStringWidget)

    klass = u'querystring-widget'

    input_template = ViewPageTemplateFile('input.pt')
    display_template = ViewPageTemplateFile('display.pt')


    def render(self):
        #if self.mode == z3c.form.interfaces.DISPLAY_MODE:
        #    return self.display_template(self)
        #else:
        return self.input_template(self)

    def getConfig(self):
        """get the config"""
        registry = getUtility(IRegistry)
        registryreader = ICollectionRegistryReader(registry)
        config = registryreader()

        # Group indices by "group", order alphabetically
        groupedIndexes = {}
        for indexName in config['indexes']:
            index = config['indexes'][indexName]
            if index['enabled']:
                group = index['group']
                if group not in groupedIndexes:
                    groupedIndexes[group] = []
                groupedIndexes[group].append((index['title'], indexName))

        # Sort each index list
        [a.sort() for a in groupedIndexes.values()]

        config['groupedIndexes'] = groupedIndexes
        return config

    def SearchResults(self, request, context, accessor):
        """search results"""
        parsedquery = queryparser.parseFormquery(self.context, self.value)
        accessor = getMultiAdapter((self.context, self.request), name='searchResults')(query=parsedquery)

        return getMultiAdapter((accessor, request), name='display_query_results')()

    def fakeAccessor(self, raw=None):
#        parsedquery = queryparser.parseFormquery(self.context, self.value)
#        if not parsedquery:
#            return IContentListing([])
#        return getMultiAdapter((self.context, self.request), name='searchResults')(query=parsedquery)
        return self.value or []


@implementer(z3c.form.interfaces.IFieldWidget)
def QueryStringFieldWidget(field, request):
    return FieldWidget(field, QueryStringWidget(request))
