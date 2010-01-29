#!/usr/bin/env python
# encoding: utf-8
"""
test_content.py

Created by Manabu Terada on 2009-12-16.
Copyright (c) 2009 CMScom. All rights reserved.
"""
import random
from Products.CMFCore.utils import getToolByName

import Products.ATGoogleMaps
import base

class TestContentTypes(base.TestCase):
    """ TopPage test """ 
    def afterSetUp(self):
        qi = self.portal.portal_quickinstaller
        qi.installProduct('ATGoogleMaps')
        self.css        = self.portal.portal_css
        self.kupu       = self.portal.kupu_library_tool
        self.skins      = self.portal.portal_skins
        self.types      = self.portal.portal_types
        self.factory    = self.portal.portal_factory
        self.workflow   = self.portal.portal_workflow
        self.properties = self.portal.portal_properties
        self.g_allow_types = [
                            "GMarker",
                            ]
        self.no_g_allow_types = [
                                # "BlogEntry",
                                # "ReportFolder",
                                ]
        self.folder_into_types = [
                    # ("contenttype name", (parent,))
                    # ("BlogEntry", ('BlogFolder',)),
                                ]
        self.addingtypes = self.g_allow_types + self.no_g_allow_types
        

    # def test_testcode_test(self):
    #     self.assertEqual(set(self.no_g_allow_types), 
    #             set((i for p, t in self.folder_into_types for i in t)))

    def test_types_installed(self):
        for t in self.addingtypes:
            self.failUnless(t in self.types.objectIds())

    def test_portal_factorySetup(self):
        for t in self.addingtypes:
            self.failUnless(t in self.factory.getFactoryTypes())

    def test_permission(self):
        permissions = [p['name'] for p in self.app.permission_settings()]
        for t in self.addingtypes:
            p = 'ATGoogleMaps: Add %s' % t
            self.failUnless(p in permissions)

    def test_global_creating(self):
        self.setRoles(['Manager'])
        allow_content_types = [al.id for al in self.portal.allowedContentTypes()]
        print allow_content_types
        for t in self.g_allow_types:
            self.failUnless(t in allow_content_types)
            id = t + '1'
            self.portal.invokeFactory(t, id)
            obj = getattr(self.portal, id)
            self.failUnless(self.portal.hasObject(id))
            # self.failUnless(obj()) No Good #######

        for t in self.no_g_allow_types:
            self.failUnless(t not in allow_content_types)
    
    def test_folder_into_creating(self):
        self.setRoles(['Manager'])
        for t, ps in self.folder_into_types:
            parent = self.portal
            for p in ps:
                base_parent = parent
                pid = p + str(random.random())
                base_parent.invokeFactory(p, pid)
                parent = getattr(base_parent, pid)
                self.failUnless(base_parent.hasObject(pid))
                self.failUnless(parent())
            allw_content_types = [al.id for al in parent.allowedContentTypes()]

            # print t, parent.id # Is this comment?
            self.failUnless(t in allw_content_types)
            tid = t + '1'
            parent.invokeFactory(t, tid)
            tobj = getattr(parent, tid)
            self.failUnless(parent.hasObject(tid))
            print tobj.absolute_url(), tobj.id
            self.failUnless(tobj())    

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestContentTypes))
    return suite

