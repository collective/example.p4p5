# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import example.p4p5

PLONE_VERSION = api.env.plone_version()


class ExampleP4P5Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=example.p4p5)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.p4p5:default')
        if PLONE_VERSION >= '5.0':
            applyProfile(portal, 'example.p4p5:plone5')
        else:
            applyProfile(portal, 'example.p4p5:plone4')


EXAMPLE_P4P5_FIXTURE = ExampleP4P5Layer()


EXAMPLE_P4P5_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_P4P5_FIXTURE,),
    name='ExampleP4P5Layer:IntegrationTesting'
)


EXAMPLE_P4P5_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_P4P5_FIXTURE,),
    name='ExampleP4P5Layer:FunctionalTesting'
)
