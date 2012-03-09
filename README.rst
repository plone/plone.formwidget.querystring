Introduction
============

A z3c.form-based widget for composing a Query string/search.

This widget is used by the contentlisting tile and the dexterity-based version
of plone.app.collection (>2.0), to make selections, and 'build' your query. It
stores a list of dictionaries containing the query you've build. This query is
being parsed by using plone.app.collection and that used
plone.app.contentlisting to display the results in the tile.


Installation
============

If you install plone.formwidget.querystring, you probably want to use it in
an add-on product for Plone. Therefore you can add it to the setup.py of your
package::

    install_requires=[
        'plone.formwidget.querystring',
        ...
    ],

You probably want to also use it to the list of dependencies in your generic
setup profile (profiles/default/metadata.xml)::

    <metadata>
      <version>1</version>
      <dependencies>
        <dependency>profile-plone.formwidget.querystring:default</dependency>
      </dependencies>
    </metadata>


Dexterity Widget
================

To assign the plone.formwidget.querystring widget to a field in your custom
content type, you can use a plone.autoform directive in the interfaces
definition (interfaces.py)::


    from plone.formwidget.querystring.widget import QueryStringFieldWidget


    class IMyDexteritySchema(form.Schema):

        form.widget(query=QueryStringFieldWidget)
        query = schema.List(
            title=_(u'label_query', default=u'Search terms'),
            description=_(u"""Define the search terms for the items you want to
                list by choosing what to match on.
                The list of results will be dynamically updated"""),
            value_type=schema.Dict(value_type=schema.Field(),
                                   key_type=schema.TextLine()),
            required=False
            )


.. note::

  See:: See
  https://github.com/plone/plone.app.collection/blob/master/plone/app/collection/interfaces.py#L16
  and
  https://github.com/plone/plone.app.contentlistingtile/blob/master/plone/app/contentlistingtile/tile.py#L18
  for further examples of how to use plone.formwidget.querystring.


Credits
=======

  * Kim Chee Leong
  * Ralph Jacobs
  * Jonas Baumann
  * Hanno Schlichting
  * Timo Stollenwerk
