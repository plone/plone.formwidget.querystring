from zope.interface import Interface
from zope.schema.interfaces import IText
3

class IQueryStringWidget(Interface):
    """Marker interface for the layout widget
    """

class IQueryString(IText):
    """QueryField for storing query"""