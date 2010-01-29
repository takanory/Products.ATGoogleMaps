#!/usr/bin/env python
# encoding: utf-8
"""
GMap.py
"""
from AccessControl import ClassSecurityInfo
from ComputedAttribute import ComputedAttribute
from zope import interface

from Products.Archetypes.atapi import *
from Products.CMFCore.utils import getToolByName

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.configuration import zconf
# from Products.CMFCore.permissions import View, ModifyPortalContent

from Products.ATGoogleMaps.interfaces import IGMap
from Products.ATGoogleMaps.config import *
from Products.ATGoogleMaps.field import LatLngField
from Products.ATGoogleMaps.widget import LatLngWidget

zoom_vocaburary = range(18)
zoom_vocaburary.reverse()

schema = Schema((
    IntegerField('height',
	        default="480",
	        required=True,
	        widget=IntegerWidget(
	            label='Height',
	            label_msgid='label_height',
	            description='Height(pixel) of this map.',
	            description_msgid='help_height',
	            i18n_domain='googlemaps',
	        )
	    ),
    LatLngField('center',
	        required=True,
	        widget=LatLngWidget(
	            label='Center',
	            label_msgid='label_center',
	            description='Center of this map.',
	            description_msgid='help_center',
	            i18n_domain='googlemaps',
	            size=12,
	        )
	    ),
    IntegerField('zoom',
	        default=15,
	        vocabulary=zoom_vocaburary,
	        widget=SelectionWidget(
	            label='Zoom',
	            label_msgid='label_zoom',
	            description='Select a zoom level.',
	            description_msgid='help_zoom',           
	            i18n_domain='googlemaps',
	        )
	    ),
    StringField('mapType',
	        vocabulary=('hybrid', 'roadmap', 'satellite', 'terrain'),
	        default='hybrid',
	        widget=SelectionWidget(
	            label='Map Type',
	            label_msgid='label_map_type',
	            description='Select a default map type.',
	            description_msgid='help_map_type',
	            i18n_domain='googlemaps',
	        ),
	        schemata='googlemaps_control',
	    ),
    StringField('navigationControl',
	        vocabulary=('default', 'small', 'zoom_pan', 'android', 'nothing'),
	        default='default',
	        widget=SelectionWidget(
	            label='Navigation Control',
	            label_msgid='label_navigation_control',
	            description='Select navigation control type',
	            description_msgid='help_map_control',
	            i18n_domain='googlemaps',
	        ),
	        schemata='googlemaps_control',
	    ),
    StringField('mapTypeControl',
	        vocabulary=('default', 'horizontal_bar', 'dropdown_menu', 'nothing'),
	        default='default',
	        widget=SelectionWidget(
	            label='Select mapType control type.',
	            label_msgid='label_scale_control',
	            description_msgid='help_scale_control',
	            i18n_domain='googlemaps',
	        ),
	        schemata='googlemaps_control',
	    ),
    ),)
gmap_schema = getattr(ATFolder, 'schema', Schema(())).copy() + schema.copy()
finalizeATCTSchema(gmap_schema)

class GMap(ATFolder):
    """
    For GMap
    """
    security = ClassSecurityInfo()
    interface.implements(IGMap)
    schema = gmap_schema
    
    meta_type = "GMap"
    _at_rename_after_creation = True
    

registerType(GMap, PROJECTNAME)
