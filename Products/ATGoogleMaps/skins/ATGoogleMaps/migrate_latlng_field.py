from Products.CMFCore.utils import getToolByName

print "Migrate Float field to Latlng filed"
print ""
catalog = getToolByName(context, 'portal_catalog')
content = catalog.searchResults(portal_type = ['GMap', 'GMarker'])
for item in content:
    obj = item.getObject()
    if hasattr(obj, 'latitude') and hasattr(obj, 'longitude'):
        latlng = {'latitude': obj.latitude,
                  'longitude': obj.longitude}
        if obj.portal_type == 'GMap':
            print obj.portal_type, obj.absolute_url()
            obj.setCenter(latlng)
            obj.setScaleControl(True)
        if obj.portal_type == 'GMarker':
            print obj.portal_type, obj.absolute_url()
            obj.setPoint(latlng)

return printed
