from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.interface import implements, implementer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.site.hooks import getSite
import z3c.form.interfaces
import z3c.form.util
from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget
from plone.app.querystring.querybuilder import QueryBuilder
from plone.app.querystring.interfaces import IQuerystringRegistryReader
from plone.formwidget.querystring.interfaces import IQueryStringWidget
from plone.registry.interfaces import IRegistry


class QueryStringWidget(Widget):
    implements(IQueryStringWidget)

    klass = u'querystring-widget'
    input_template = ViewPageTemplateFile('input.pt')

    def render(self):
        return self.input_template(self)

    def getConfig(self):
        """get the config"""
        registry = getUtility(IRegistry)
        registryreader = IQuerystringRegistryReader(registry)
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

    def SearchResults(self):
        """Search results"""
        site = getSite()
        options = dict(original_context=site)
        querybuilder = QueryBuilder(site, self.request)
        listing = querybuilder(query=self.value)
        return getMultiAdapter((listing, self.request),
            name='display_query_results')(**options)


@implementer(z3c.form.interfaces.IFieldWidget)
def QueryStringFieldWidget(field, request):
    return FieldWidget(field, QueryStringWidget(request))
