from Globals import InitializeClass
from Products.validation import validation
from Products.validation.interfaces.IValidator import IValidator
from Products.CMFCore.utils import getToolByName

class LatLngValidator:
    """
    Latitude and Longitude validator. To be used with LatLngField.
    """

    __implements__ = IValidator

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title
        self.description = description

    def __call__(self, value, *args, **kwargs):
        """
        Tests if the password values match. If value is just one string,
        only tests size.
        """

        try:
            latitude = float(value.latitude)
            longitude = float(value.longitude)
        except:
            return 1

        if latitude < -90 or latitude > 90:
            return 'Latitude is out of range.'
        if longitude < -180 or longitude > 180:
            return 'Longitude is out of range.'

        return 1

validation.register(LatLngValidator('LatLngValidator'))
