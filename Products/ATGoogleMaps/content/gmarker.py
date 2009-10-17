"""Definition of the GMarker content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.ATGoogleMaps import ATGoogleMapsMessageFactory as _
from Products.ATGoogleMaps.interfaces import IGMarker
from Products.ATGoogleMaps.config import PROJECTNAME

GMarkerSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

GMarkerSchema['title'].storage = atapi.AnnotationStorage()
GMarkerSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(GMarkerSchema, moveDiscussion=False)

class GMarker(base.ATCTContent):
    """GMarker"""
    implements(IGMarker)

    meta_type = "GMarker"
    schema = GMarkerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(GMarker, PROJECTNAME)
