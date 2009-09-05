## Script (Python) "prefs_gmap_set"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=api_key, RESPONSE=None
##title=set portalskin prefs
##

REQUEST=context.REQUEST

gmap = context.portal_properties.gmap_properties

gmap.manage_changeProperties(api_key=api_key)

msg = 'ATGoogleMaps settings updated.'
return state.set(portal_status_message=msg)