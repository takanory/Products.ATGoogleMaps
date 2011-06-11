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
from Products.ATGoogleMaps.widget import PolylineWidget

schema = Schema((
    StringField('color',
                default="#0000ff",
                widget=StringWidget(
                    label='Color',
                    label_msgid='label_color',
                    description='Enter the color in hexadecimal numeric HTML style, i.e. #RRGGBB.',
                    description_msgid='help_color',
                    i18n_domain='googlemaps',
                    size=8,
                    )
                ),
    FloatField('opacity',
               default=0.5,
               widget=StringWidget(
                   label='Opacity',
                   label_msgid='label_opacity',
                   description='Enter stroke opacity between 0.0 and 1.0.',
                   description_msgid='help_opacity',
                   i18n_domain='googlemaps',
                   size=8,
                   )
               ),
    IntegerField('weight',
                 default=5,
                 widget=StringWidget(
                     label='Weight',
                     label_msgid='label_weight',
                     description='Enter stroke width in pixels.',
                     description_msgid='help_weight',
                     i18n_domain='googlemaps',
                     size=8,
                     )
                 ),
    LinesField('coordinates',
               widget=PolylineWidget(
                   label='Coordinates',
                   label_msgid='label_coordinates',
                   description='Enter stroke coordinates.',
                   description_msgid='help_coordinates',
                   i18n_domain='googlemaps',
                   )
               ),
    FloatField('north',
               widget=ComputedWidget(
                 visible={'vew': 'invisible', 'edit': 'hidden'},
                 )
               ),
    FloatField('east',
               widget=ComputedWidget(
                 visible={'vew': 'invisible', 'edit': 'hidden'},
                 )
               ),
    FloatField('south',
               widget=ComputedWidget(
                 visible={'vew': 'invisible', 'edit': 'hidden'},
                 )
               ),
    FloatField('west',
               widget=ComputedWidget(
                 visible={'vew': 'invisible', 'edit': 'hidden'},
                 )
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

    # set bounds from coordinates
    def setCoordinates(self, value, **kwargs):
        field=self.getField('coordinates')
        field.set(self,value,**kwargs)
        north = -91.0
        south = 91.0
        east = -181.0
        west = 181.0
        for coordinate in self.coordinates:
            lat, lng = coordinate.split(",")
            lat = float(lat)
            lng = float(lng)
            if lat < south:
                south = lat
            if lat > north:
                north = lat
            if lng < west:
                west = lng
            if lng > east:
                east = lng
        self.setNorth(north)
        self.setSouth(south)
        self.setEast(east)
        self.setWest(west)
        
    # default point value from parent GMap center
    def getContainerCenter(self):
        latlng = {'latitude': '0.0', 'longitude': '0.0'}
        try:
            latlng = self.aq_parent.getCenter()
        except:
            pass
        return latlng

    # return coordinates array string
    def getCoordinatesArray(self):
        coordinates_array = "["
        for coordinate in self.coordinates:
             coordinates_array += "[%s]," % coordinate
        coordinates_array = coordinates_array[:-1] + "]"
        return coordinates_array

    # return coordinates array string
    def getKMLCoordinates(self):
        kml_coordinates = ""
        for coordinate in self.coordinates:
            (lat, lng) = coordinate.split(",")
            kml_coordinates += "%s,%s " % (lng, lat)
        return kml_coordinates

    def getKMLColor(self):
        self.color
        a_value = (int)(self.opacity * 255)
        return "%02x%s%s%s" % (a_value, self.color[5:7], self.color[3:5], self.color[1:3])

    def getStaticMap(self):
        '''
        get Google Static Map URL
        '''
        color = "0x%s%02x" % (self.color[1:], int(self.opacity * 255))
        staticmap = "http://maps.google.com/maps/api/staticmap?path=color:%s|weight:%d" % (color, self.weight)
        for coordinate in self.coordinates:
            staticmap += "|%s" % coordinate
        staticmap += "&size=640x640&sensor=false"
        return staticmap

registerType(GPolyline, PROJECTNAME)
