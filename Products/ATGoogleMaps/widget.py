from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.Archetypes.public import StringWidget
from Products.Archetypes.Registry import registerWidget

class LatLngWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update({
        'macro' : "latlng_widget",
        })
    security = ClassSecurityInfo()

InitializeClass(LatLngWidget)

registerWidget(LatLngWidget,
               title='LatLng',
               description="Renders latitude and longitude fields.",
               used_for=('Products.ATGoogleMaps.field.LatLngField',)
               )
