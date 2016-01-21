# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from example.p4p5.testing import EXAMPLE_P4P5_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that example.p4p5 is properly installed."""

    layer = EXAMPLE_P4P5_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if example.p4p5 is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('example.p4p5'))

    def test_uninstall(self):
        """Test if example.p4p5 is cleanly uninstalled."""
        self.installer.uninstallProducts(['example.p4p5'])
        self.assertFalse(self.installer.isProductInstalled('example.p4p5'))

    def test_browserlayer(self):
        """Test that IExampleP4P5Layer is registered."""
        from example.p4p5.interfaces import IExampleP4P5Layer
        from plone.browserlayer import utils
        self.assertIn(IExampleP4P5Layer, utils.registered_layers())
