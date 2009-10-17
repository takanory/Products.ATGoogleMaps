"""Main product initializer
"""

from zope.i18nmessageid import MessageFactory

from Products.Archetypes.atapi import *
from config import *
from Products.CMFCore.utils import ContentInit


# Define a message factory for when this product is internationalised.
# This will be imported with the special name "_" in most modules. Strings
# like _(u"message") will then be extracted by i18n tools for translation.

ATGoogleMapsMessageFactory = MessageFactory('Products.ATGoogleMaps')

def initialize(context):
    import content

    content_types, constructors, ftis = process_types(listTypes(PROJECTNAME), PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        ContentInit(
            "%s: %s" % (PROJECTNAME, atype.portal_type),
            content_types = (atype,),
            permission = config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)
