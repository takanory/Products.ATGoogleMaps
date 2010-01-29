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
# from Products.CMFCore.permissions import View, ModifyPortalContent

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
                    size=30,
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
    LatLngField('point',
                required=True,
                default_method='getGMapCenter',
                widget=LatLngWidget(
                    label='Point',
                    label_msgid='label_point',
                    description='Point of this marker.',
                    description_msgid='help_point',
                    i18n_domain='googlemaps',
                    size=12,
                    )
                ),
    StringField('tab1',
                widget=IntegerWidget(
                    label='Tab #1 title',
                    label_msgid='label_tab1',
                    description_msgid='help_tab1',
                    i18n_domain='googlemaps',
                    size=20,
                    ),
                schemata='googlemaps_tabbed',
                ),
    StringField('tab2',
                widget=IntegerWidget(
                    label='Tab #2 title',
                    label_msgid='label_tab2',
                    description_msgid='help_tab2',
                    i18n_domain='googlemaps',
                    size=20,
                    ),
                schemata='googlemaps_tabbed',
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
              schemata='googlemaps_tabbed',
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
    

registerType(GMarker, PROJECTNAME)
