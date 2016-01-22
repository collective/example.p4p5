# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from example.p4p5.testing import EXAMPLE_P4P5_FUNCTIONAL_TESTING  # noqa
import Globals
from plone import api
from plone.testing.z2 import Browser
import unittest

PROJECTNAME = 'example.p4p5'

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
        self.assertTrue(CSS in self.browser.contents)

    def test_js_resources(self):
        self.browser.open(self.portal.absolute_url())
        self.assertTrue(JS in self.browser.contents)
