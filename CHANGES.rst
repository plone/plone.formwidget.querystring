Changelog
=========

1.0b4 (unreleased)
------------------

- If we set background to 'white' we should set foreground to 'black' to avoid
  people getting white font on white background if they use white font color
  for their plone sites.  [saily]


1.0b3 (2013-02-04)
------------------

- Fixed context for getting ajax results
  [kroman0]

- Fixed conditional initialization of querywidget,
  see http://dev.plone.org/ticket/12529 [kroman0]

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
