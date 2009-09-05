"""Definition of the GMap content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.ATGoogleMaps import ATGoogleMapsMessageFactory as _
from Products.ATGoogleMaps.interfaces import IGMap
from Products.ATGoogleMaps.config import PROJECTNAME

GMapSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

GMapSchema['title'].storage = atapi.AnnotationStorage()
GMapSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    GMapSchema,
    folderish=True,
    moveDiscussion=False
)

class GMap(folder.ATFolder):
    """Google Maps Type"""
    implements(IGMap)

    meta_type = "GMap"
    schema = GMapSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(GMap, PROJECTNAME)
