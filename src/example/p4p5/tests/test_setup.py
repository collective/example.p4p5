# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from example.p4p5.testing import EXAMPLE_P4P5_FUNCTIONAL_TESTING  # noqa
from plone import api
from plone.testing.z2 import Browser

import Globals
import transaction
import unittest

PROJECTNAME = 'example.p4p5'
PLONE_VERSION = api.env.plone_version()
CSS = '++resource++example.p4p5/chart.css'
JS = '++resource++example.p4p5/chart.js'


class InstallTestCase(unittest.TestCase):

    """Test that example.p4p5 is properly installed."""

    layer = EXAMPLE_P4P5_FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        Globals.DevelopmentMode = True
        self.portal = self.layer['portal']
        self.browser = Browser(self.layer['app'])
        self.qi = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if example.p4p5 is installed with portal_quickinstaller."""
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer(self):
        """Test that IExampleP4P5Layer is registered."""
        from example.p4p5.interfaces import IExampleP4P5Layer
        from plone.browserlayer import utils
        self.assertIn(IExampleP4P5Layer, utils.registered_layers())

    def test_css_resources(self):
        self.browser.open(self.portal.absolute_url())
        self.assertIn(CSS, self.browser.contents)

    def test_js_resources(self):
        self.browser.open(self.portal.absolute_url())
        self.assertIn(JS, self.browser.contents)


class UninstallTestCase(unittest.TestCase):

    """Test that example.p4p5 is properly uninstalled."""

    layer = EXAMPLE_P4P5_FUNCTIONAL_TESTING

    def setUp(self):
        Globals.DevelopmentMode = True
        self.portal = self.layer['portal']
        self.browser = Browser(self.layer['app'])
        self.qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            self.qi.uninstallProducts(products=[PROJECTNAME])
        transaction.commit()

    def test_uninstall(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_uninstall_css_resources(self):
        self.browser.open(self.portal.absolute_url())
        self.assertNotIn(CSS, self.browser.contents)

    def test_uninstall_js_resources(self):
        self.browser.open(self.portal.absolute_url())
        self.assertNotIn(JS, self.browser.contents)
