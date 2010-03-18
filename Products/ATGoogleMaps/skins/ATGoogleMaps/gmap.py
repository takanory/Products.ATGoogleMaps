site_encoding =  context.plone_utils.getSiteEncoding()

def add_markers(js, items):
    for index in range(len(items)):
        marker = items[index].getObject()
        lat = marker.point['latitude']
        lng = marker.point['longitude']
        js.append('  var marker_%d = createMarker(map, %s, %s, "%d", "%s");' % (index, lat, lng, index, marker.title))

# create initialize method
def initialize_func(js):
    lat = context.center['latitude']
    lng = context.center['longitude']
    js.extend(('function initialize() {',
               '  var map = createMap("map_canvas", %s, %s, %s, "%s", "%s", "%s");' % (lat, lng, context.zoom, context.mapType, context.mapTypeControl, context.navigationControl),
               ))

    add_markers(js, context.getFolderContents())

    js.append('}')
    
js = ['<script type="text/javascript">']
initialize_func(js)
js.append('google.maps.event.addDomListener(window, "load", initialize);')
js.append('</script>')

return "\n".join(js)
