from zope.interface import implements, implementer

import z3c.form.interfaces
import z3c.form.widget
import z3c.form.util

from z3c.form.browser.textarea import TextAreaWidget

from plone.formwidget.querystring.interfaces import IQueryStringWidget

from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class QueryStringWidget(TextAreaWidget):
    implements(IQueryStringWidget)

    klass = u'layout-widget'

    input_template = ViewPageTemplateFile('input.pt')
    display_template = ViewPageTemplateFile('display.pt')

    def render(self):
        if self.mode == z3c.form.interfaces.DISPLAY_MODE:
            return self.display_template(self)
        else:
            return self.input_template(self)

@implementer(z3c.form.interfaces.IFieldWidget)
def QueryStringWidgetFieldWidget(field, request):
    return z3c.form.widget.FieldWidget(field, QueryWidget(request))
