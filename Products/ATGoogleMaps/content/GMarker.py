#!/usr/bin/env python
# encoding: utf-8
"""
GMarker.py
"""
from AccessControl import ClassSecurityInfo
from ComputedAttribute import ComputedAttribute
from zope import interface

from Products.Archetypes.atapi import *
from Products.CMFCore.utils import getToolByName

from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.configuration import zconf

from Products.ATGoogleMaps.interfaces import IGMarker
from Products.ATGoogleMaps.config import *
from Products.ATGoogleMaps.field import LatLngField
from Products.ATGoogleMaps.widget import LatLngWidget

schema = Schema((
    StringField('address',
                widget=IntegerWidget(
                    label='Address',
                    label_msgid='label_address',
                    description_msgid='help_address',
                    i18n_domain='googlemaps',
                    size=60,
                    )
                ),
    StringField('phone',
                widget=IntegerWidget(
                    label='Phone',
                    label_msgid='label_phone',
                    description_msgid='help_phone',
                    i18n_domain='googlemaps',
                    size=30,
                    )
                ),
    StringField('url',
                widget=IntegerWidget(
                   label='URL',
                   label_msgid='label_url',
                   description_msgid='help_url',
                   i18n_domain='googlemaps',
                   size=60,
                   )
                ),
    StringField('imageurl',
                widget=IntegerWidget(
                    label='Image URL',
                    label_msgid='label_image_url',
                    description_msgid='help_image_url',
                    i18n_domain='googlemaps',
                    size=60,
                    )
                ),
    BooleanField('streetView',
                 widget=BooleanWidget(
                     label="Display Street View",
                     label_msgid="label_street_view",
                     description_msgid="help_street_view",
                     i18n_domain="googlemaps",
                     ),
                 ),
    LatLngField('point',
                required=True,
                default_method='getContainerCenter',
                widget=LatLngWidget(
                    label='Point',
                    label_msgid='label_point',
                    description='Point of this marker.',
                    description_msgid='help_point',
                    i18n_domain='googlemaps',
                    size=12,
                    )
                ),
    TextField('detail',
              searchable=True,
              validators=('isTidyHtmlWithCleanup',),
              default_content_type=zconf.ATDocument.default_content_type,
              default_output_type='text/x-html-safe',
              allowable_content_types=zconf.ATDocument.allowed_content_types,
              widget=RichWidget(
                  rows=10,
                  label="Detail",
                  label_msgid="label_detail",
                  description_msgid="help_detail",
                  i18n_domain="googlemaps",
                  ),
#              schemata='googlemaps_tabbed',
              ),
    ),)
gmarker_schema = getattr(ATCTContent, 'schema', Schema(())).copy() + schema.copy()
finalizeATCTSchema(gmarker_schema)

class GMarker(ATCTContent):
    """
    For GMarker
    """
    security = ClassSecurityInfo()
    interface.implements(IGMarker)
    schema = gmarker_schema
    
    meta_type = "GMarker"
    _at_rename_after_creation = True
    
    # default point value from parent GMap center
    def getContainerCenter(self):
        latlng = {'latitude': '0.0', 'longitude': '0.0'}
        try:
            latlng = self.aq_parent.getCenter()
        except:
            pass
        return latlng

registerType(GMarker, PROJECTNAME)
