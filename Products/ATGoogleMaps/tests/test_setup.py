#!/usr/bin/env python
# encoding: utf-8
"""
test_setup.py

Created by Manabu Terada on 2009-12-16.
Copyright (c) 2009 CMScom. All rights reserved.
"""
from Products.CMFCore.utils import getToolByName

import Products.ATGoogleMaps
import base

class TestInstall(base.TestCase):
    """ Install basic test """ 
    def afterSetUp(self):
        pass

    def testQuickInstall(self):
        qi = self.portal.portal_quickinstaller
        print '\n'.join(p['id'] for p in qi.listInstallableProducts())
        self.failUnless(1, len([p['title'] for p in qi.listInstallableProducts() 
                                        if p['title'] == 'ATGoogleMaps']))
        self.failUnless('ATGoogleMaps' in (p['id'] for p in qi.listInstallableProducts()))        
        qi.installProduct('ATGoogleMaps')
        self.failUnless(qi.isProductInstalled('ATGoogleMaps'))
        self.failUnless('ATGoogleMaps' not in ''.join(p['id'] for p in qi.listInstallableProducts()))        
    
class TestSkinInstall(base.TestCase):
    """  """
    def afterSetUp(self):
        qi = self.portal.portal_quickinstaller
        qi.installProduct('ATGoogleMaps')

    def testSkinLayersInstalled(self):
        self.skins = self.portal.portal_skins
        # print self.skins.objectIds()
        self.failUnless('ATGoogleMaps' in self.skins.objectIds())
        self.assertEqual(len(self.skins.ATGoogleMaps.objectIds()), 1)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInstall))
    suite.addTest(makeSuite(TestSkinInstall))
    return suite