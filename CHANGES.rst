Changelog
=========

1.0.4 (unreleased)
--------------

- Don't install utility for zope.app.intid's IIntIds,
  which is just an alias for the one in zope.intid.
  [davisagli]

- fix test to not add ``Folder`` fti in testSetup if it already exists.
  [jensens]


1.0.3 (2014-02-25)
------------------

- Make the test setup independent from basic content types in the
  PLONE_FIXTURE.
  [timo]


1.0.2 (2012-12-17)
------------------

- removing zope.app.container as dependency and importing events interfaces
  from zope.lifecycle
  [garbas]

- intid/setuphandlers.py: Removed blacklisted and unused interface
  IDynamicType from query. Closes http://dev.plone.org/ticket/11946.
  [kleist]


1.0.1 (2012-06-15)
------------------

- Fixed registration of pre existing contents in the intids utility
  [gborelli]

- Added setup tests
  [gborelli]

1.0 (2012-02-20)
----------------

- Remove includeOverride for five.intid. [thet]

- Fix import step intid-register-content to register content
  in all Languages if LinguaPlone is installed. [csenger]

1.0b3 2010-02-27
-------------------

- Made compatible with Plone 3.3
  [alecm]

1.0b2 2010-02-22
-------------------

- fixed dependecy of import profiles
  [naro]

1.0b1 2010-02-07
-------------------

- Initial release
  [alecm]
