from plone.formwidget.querystring.interfaces import IQueryStringWidget
from Products.CMFPlone.utils import safe_unicode
from z3c.form.converter import BaseDataConverter
from zope.schema.interfaces import IList

import zope.component


def safe_utf8(s):
    if isinstance(s, unicode):
        s = s.encode('utf8')
    return s


class AttributeDict(dict):
    """Dictionary which provides contents as attributes"""

    def __getattr__(self, key):
        return self[key]


class QueryStringConverter(BaseDataConverter):
    """Converts values for use with QueryStringWidget (make z3c.form happy)"""
    zope.component.adapts(IList, IQueryStringWidget)

    def toWidgetValue(self, value):
        """Converts given value for use in the widget"""

        if value is self.field.missing_value:
            return value
        else:
            data = []
            for dict_ in value:
                new_dict = AttributeDict()
                for key, value in dict_.items():
                    if isinstance(value, list):
                        new_dict[safe_utf8(key)] = \
                            [safe_utf8(x) for x in value]
                    else:
                        new_dict[safe_utf8(key)] = safe_utf8(value)
                data.append(new_dict)
            return data

    def toFieldValue(self, value):
        """Converts value for use in the field"""
        if value is self.field.missing_value:
            return value
        else:
            data = []
            for dict_ in value:
                new_dict = {}
                for key, value in dict_.items():
                    if isinstance(value, list):
                        new_dict[safe_unicode(key)] = \
                            [safe_unicode(x) for x in value]
                    else:
                        new_dict[safe_unicode(key)] = safe_unicode(value)
                data.append(new_dict)
            return data
