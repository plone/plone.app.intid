from plone.app.intid.testing import SETUP_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from zope.intid.interfaces import IIntIds

import unittest


class TestSetup(unittest.TestCase):
    layer = SETUP_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        # XXX below code is only needed if theres no Folder FTI already setup.
        typetool = getToolByName(self.portal, "portal_types")
        if "Folder" not in typetool.objectIds():
            # XXX Check if this is needed for Plone 5.0! In 4.3 the FTI is
            # already setup
            fti = DexterityFTI("Folder")
            typetool._setObject("Folder", fti)

    def tearDown(self):
        setRoles(self.portal, TEST_USER_ID, ["Member"])

    def test_already_installed(self):
        """plone.app.intid is a dependency of plone.app.linkintegrity
        which is a dependency of CMFPlone, so it is always installed.
        This tests if this is true.
        """
        # we create a folder
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        folder_id = self.portal.invokeFactory("Folder", "folder")
        folder = self.portal[folder_id]
        intids = getUtility(IIntIds)
        self.assertIsNotNone(intids.getId(folder))

    @unittest.skip("p.a.intid is always installed")
    def test_install(self):
        """When p.app.intid is intalled it registers some utility
        from zope.intid and five.intid and search in portal_catalog
        all contents in order to register them in these utilities.

        This test checks that all pre existing contents
        are registered correctly
        """
        from plone.app.intid.setuphandlers import add_intids
        from plone.app.testing import applyProfile

        # we create a folder before the intallation of plone.app.intid
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        folder_id = self.portal.invokeFactory("Folder", "folder")
        folder = self.portal[folder_id]

        # now we install manually the intid utilities
        add_intids(self.portal)
        intids = getUtility(IIntIds)

        # this folder is not referenced by intid utility
        self.assertRaises(KeyError, intids.getId, folder)

        # when we install p.app.intid our folder is referencend by intid
        applyProfile(self.portal, "plone.app.intid:default")
        self.assertIsNotNone(intids.getId(folder))
