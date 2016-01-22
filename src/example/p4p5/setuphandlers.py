# -*- coding: utf-8 -*-
from plone import api


def isNotCurrentProfile(context):
    return context.readDataFile('examplep4p5_marker.txt') is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return
    portal = api.portal.get()
    setupTool = portal['portal_setup']
    plone_version = api.env.plone_version()
    if plone_version >= '5.0':
        profileName = 'plone5'
    else:
        profileName = 'plone4'
    profileId = 'profile-example.p4p5:%s' % (profileName, )
    setupTool.runAllImportStepsFromProfile(profileId)

    portal.clearCurrentSkin()
    portal.setupCurrentSkin(portal.REQUEST)
