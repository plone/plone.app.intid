# -*- coding: utf-8 -*-
from five.intid.intid import IntIds
from five.intid.site import addUtility
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from zope.intid.interfaces import IIntIds

import logging


logger = logging.getLogger(__name__)


try:
    # XXX here we must consider plone.app.multilingual as well!
    import Products.LinguaPlone
    Products.LinguaPlone
    HAS_LINGUAPLONE = True
except ImportError:
    HAS_LINGUAPLONE = False


def register_all_content_for_intids(portal):
    """Registers all existing content with the intid utility.
    This will not be fast."""
    cat = getToolByName(portal, 'portal_catalog', None)
    if cat is None:
        return
    intids = getUtility(IIntIds)
    # Take advantage of paths stored in keyreferences in five.intid to optimize
    # registration
    registered_paths = {
        ref.path for ref in intids.ids
        if hasattr(ref, 'path')
    }
    # Count how many objects we register
    registered = 0
    existing = 0
    query = {'object_provides': IContentish.__identifier__}
    if HAS_LINGUAPLONE:
        query['Language'] = 'all'
    for brain in cat(query):
        if brain.getPath() in registered_paths:
            existing += 1
            continue
        try:
            obj = brain.getObject()
            intids.register(obj)
            registered += 1
        except (AttributeError, KeyError, TypeError):
            # "TypeError" happens on a "could not adapt" - this may happen
            # for some contenttypes and must not stop this from working.
            logger.exception(brain.getURL())
    return registered, existing


def add_intids(context):
    addUtility(context, IIntIds, IntIds, ofs_name='intids',
               findroot=False)


def installIntIds(context):
    if context.readDataFile('install_intids.txt') is None:
        return
    portal = context.getSite()
    add_intids(portal)
    return 'Added intid utility.'


def registerContent(context):
    if context.readDataFile('intid_register_content.txt') is None:
        return
    portal = context.getSite()
    registered, existing = register_all_content_for_intids(portal)
    return ('Assigned intids to {0} content objects, {1} objects '
            'already had intids.'.format(registered, existing))
