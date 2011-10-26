Introduction
============

A z3c.form-based widget for composing a Query string/search. 

This widget is used by the contentlisting tile and the dexterity-based version 
of plone.app.collection (>2.0), to make selections, and 'build' your query. It 
stores a list of dictionaries containing the query you've build. This query is 
being parsed by using plone.app.collection and that used
plone.app.contentlisting to display the results in the tile.
