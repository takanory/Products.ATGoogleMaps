#!/usr/bin/env python
# encoding: utf-8
"""
GPolyline.py
"""
from AccessControl import ClassSecurityInfo
from ComputedAttribute import ComputedAttribute
from zope import interface

from Products.Archetypes.atapi import *
from Products.CMFCore.utils import getToolByName

from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.configuration import zconf

from Products.ATGoogleMaps.interfaces import IGPolyline
from Products.ATGoogleMaps.config import *

schema = Schema((
    StringField('color',
                default="#ff0000",
                widget=StringWidget(
                    label='Color',
                    label_msgid='label_color',
                    description_msgid='help_color',
                    i18n_domain='googlemaps',
                    size=8,
                    )
                ),
    FloatField('opacity',
               default=1.0,
               ),
    IntegerField('weight',
                 default=2,
                 ),
    ),)
gpolyline_schema = getattr(ATCTContent, 'schema', Schema(())).copy() + schema.copy()
finalizeATCTSchema(gpolyline_schema)

class GPolyline(ATCTContent):
    """
    For GPolyline
    """
    security = ClassSecurityInfo()
    interface.implements(IGPolyline)
    schema = gpolyline_schema
    
    meta_type = "GPolyline"
    _at_rename_after_creation = True
    
    # default point value from parent GMap center
    def getContainerCenter(self):
        latlng = {'latitude': '0.0', 'longitude': '0.0'}
        try:
            latlng = self.aq_parent.getCenter()
        except:
            pass
        return latlng

registerType(GPolyline, PROJECTNAME)
