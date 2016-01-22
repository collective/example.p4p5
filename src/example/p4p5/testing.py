# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import example.p4p5

try:
    from plone.app.upgrade.v50 import final
    IS_PLONE40 = False
except ImportError:
    IS_PLONE40 = True


class ExampleP4P5Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=example.p4p5)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.p4p5:default')
        if IS_PLONE40:
            applyProfile(portal, 'example.p4p5:plone4')
        else:
            applyProfile(portal, 'example.p4p5:plone5')


EXAMPLE_P4P5_FIXTURE = ExampleP4P5Layer()


EXAMPLE_P4P5_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_P4P5_FIXTURE,),
    name='ExampleP4P5Layer:IntegrationTesting'
)


EXAMPLE_P4P5_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_P4P5_FIXTURE,),
    name='ExampleP4P5Layer:FunctionalTesting'
)


EXAMPLE_P4P5_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_P4P5_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ExampleP4P5Layer:AcceptanceTesting'
)
