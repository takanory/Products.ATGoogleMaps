from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import LinesWidget
from Products.Archetypes.Registry import registerWidget

class LatLngWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update({
        'macro' : "latlng_widget",
        })
    security = ClassSecurityInfo()

#InitializeClass(LatLngWidget)

registerWidget(LatLngWidget,
               title='LatLng',
               description="Renders latitude and longitude fields.",
               used_for=('Products.ATGoogleMaps.field.LatLngField',)
               )

class PolylineWidget(LinesWidget):
    _properties = LinesWidget._properties.copy()
    _properties.update({
        'macro' : "polyline_widget",
        })
    security = ClassSecurityInfo()

#InitializeClass(PolylineWidget)

registerWidget(PolylineWidget,
               title='Polyline',
               description="Renders polyline fields.",
               used_for=('Products.Archetypes.Field.LinesField',)
               )
