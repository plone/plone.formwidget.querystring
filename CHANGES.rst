Changelog
=========

1.1.11 (unreleased)
-------------------

Breaking changes:

- *add item here*

New features:

- *add item here*

Bug fixes:

- fixed deprecated import ``zope.site.hooks.getSite``
  [petschki]


1.1.10 (2017-08-09)
-------------------

Bug fixes:

- Recent Plone 4.3 versions have a change in the base href calculation. Fix
  calculation of the baseUrl in updating the queryresults in the widgets if
  /edit is part of the base href.
  [fredvd, maurits]


1.1.9 (2017-05-06)
------------------

Bug fixes:

- Make "Remove line" from input.pt translatable


1.1.8 (2016-12-19)
------------------

Bug fixes:

- Prevent ASCII error for encode/decode in utf8 into converter.
  [bsuttor]


1.1.7 (2016-08-15)
------------------

Bug fixes:

- Use zope.interface decorator.
  [gforcada]


1.1.6 (2016-05-10)
------------------

Fixes:

- Fix way to decode utf-8 into template.
  [bsuttor]


1.1.5 (2015-07-18)
------------------

- Conditionally setup zope.app.form field.
  [vangheem]


1.1.4 (2014-11-05)
------------------

- Fix criteria checkbox rendering if value contains non ASCII characters.
  [rnixx]


1.1.3 (2014-11-01)
------------------

- Fixed sort index selection which was not preserved when editing collection
  criteria.
  [naro]

- make compatible with jQuery >= 1.9
  [petschki]


1.1.2 (2014-04-05)
------------------

- Fixed label for "Add Criteria" (missing id="addindex")
  [djay]


1.1.1 (2014-02-23)
------------------

- Avoid `TypeError: 'NoneType' object is not iterable` when the query
  of the collection is still `None`, like is the case when adding one.
  [maurits]


1.1.0 (2013-11-14)
------------------

- Change javascript to work on ``form-widgets-ICollection`` fields instead of
  ``form-widgets``.
  [maurits, kaselis]


1.0b4 (unreleased)
------------------

- If we set background to 'white' we should set foreground to 'black' to avoid
  people getting white font on white background if they use white font color
  for their plone sites.  [saily]

- Add handling of the RelativeDateWidget, already expected to exist in
  p.a.querystring.
  [tmog]

- Add jquery dateinput to dateWidget and dateRangeWidget.
  [tmog]


1.0b3 (2013-02-04)
------------------

- Fixed context for getting ajax results
  [kroman0]

- Fixed conditional initialization of querywidget,
  see http://dev.plone.org/ticket/12529
  [kroman0]

- The widget can now be hidden, when clicking on the
  window or the widget. The event is only effective
  when the widget is displayed.
  [bosim]

- Translations are now in Plone domain
  [bosim]

- Made the widget a bit more resistent to missing entries, i.e. vocabularies
  or in other way indexes. The problem occur if an option is deleted from the
  registry but not deleted from the collections in before hand.
  [bosim]

- Update import path for pagetemplate. Now only works with 4.1 and higher
  [do3cc]


1.0b2 (2012-03-19)
------------------

- Fix sort-reversed checkbox javascript.
  [timo]

- Move docs/HISTORY.txt to CHANGES.txt to apply to Plone conventions.
  [timo]


1.0b1 (2012-03-09)
------------------

- Stop hardcoding the field name so it works with other field names and
  prefixes.
  [davisagli]

- Rename ArcheTypesQueryWidget to Querywidget to avoid confusion.
  [timo]

- Several JSLint fixes on querywidget.js
  [timo]

- Make sure the sorting settings are actually stored on the collection.
  [timo]


1.0a1 (2011-10-28)
------------------

- Initial release.
  [ralphjacobs, kcleong, jbaumann, hannosch, timo]
