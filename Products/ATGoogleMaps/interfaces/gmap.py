from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from Products.ATGoogleMaps import ATGoogleMapsMessageFactory as _

class IGMap(Interface):
    """A Google Map Type"""
    
    # -*- schema definition goes here -*-
