# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from example.p4p5.testing import EXAMPLE_P4P5_INTEGRATION_TESTING  # noqa
from plone import api

import unittest

PROJECTNAME = 'example.p4p5'

CSS = '++resource++example.p4p5/chart.css'
JS = '++resource++example.p4p5/chart.js'


class InstallTestCase(unittest.TestCase):

    """Test that example.p4p5 is properly installed."""

    layer = EXAMPLE_P4P5_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
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
        css_resource_ids = self.portal.portal_css.getResourceIds()
        self.assertIn(CSS, css_resource_ids)

    def test_js_resources(self):
        js_resource_ids = self.portal.portal_javascripts.getResourceIds()
        self.assertIn(JS, js_resource_ids)


class UninstallTestCase(unittest.TestCase):

    """Test that example.p4p5 is properly uninstalled."""

    layer = EXAMPLE_P4P5_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstall(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_uninstall_css_resources(self):
        css_resource_ids = self.portal.portal_css.getResourceIds()
        self.assertNotIn(CSS, css_resource_ids)

    def test_uninstall_js_resources(self):
        js_resource_ids = self.portal.portal_javascripts.getResourceIds()
        self.assertNotIn(JS, js_resource_ids)
