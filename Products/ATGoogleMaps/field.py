from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.Archetypes.Registry import registerField
from Products.Archetypes.Field import ObjectField, Field
from Products.ATGoogleMaps.widget import LatLngWidget

import validator

class LatLngField(ObjectField):
    """A field that store latitude and longitude value"""
    __implements__ = ObjectField.__implements__

    _properties = Field._properties.copy()
    _properties.update({
        'type': 'latlng',
        'default': {},
        'size': 12,
        'default': None,
        'widget': LatLngWidget,
        'validators': ('LatLngValidator'),
        })

    security  = ClassSecurityInfo()
        
    security.declarePrivate('validate_required')
    def validate_required(self, instance, value, errors):
        try:
            float(value.latitude)
            float(value.longitude)
        except (ValueError, TypeError):
            result = False
        else:
            result = True
        return ObjectField.validate_required(self, instance, result, errors)

    security.declarePrivate('get')
    def get(self, instance, **kwargs):
        return ObjectField.get(self, instance, **kwargs)

    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        if type(value) != type({}) and hasattr(value, 'keys'):
            new_value = {}
            new_value.update(value)
            value = new_value
            
        ObjectField.set(self, instance, value, **kwargs)

InitializeClass(LatLngField)

registerField(LatLngField,
              title="LatLng",
              description="Used to store longitude and longitude.",
              )

