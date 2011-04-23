# create initialize method
def initialize_func(js):
    lat = context.center['latitude']
    lng = context.center['longitude']
    js.extend(('function initialize() {',
               '  var map = createMap("map_canvas", %s, %s, %s, "%s", "%s", "%s");' % (lat, lng, context.zoom, context.mapType, context.mapTypeControl, context.navigationControl),
               ))
    if len(context.coordinates) > 1:
        js.append('  var polyline = createPolyline(map, "%s", %f, %d, "%s");'
                  % (context.color, context.opacity, context.weight, context.title))
        js.append('  polyline.setPath(createPath(%s));' % (context.getCoordinatesArray()))
        js.append('  var sw = new google.maps.LatLng(%f, %f);' % (context.getSouth(), context.getWest()))
        js.append('  var ne = new google.maps.LatLng(%f, %f);' % (context.getNorth(), context.getEast()))
        js.append('  var bounds = new google.maps.LatLngBounds(sw, ne);')
        js.append('  map.fitBounds(bounds);')

    js.append('}')
    

js = ['<script type="text/javascript">']
initialize_func(js)
js.append('google.maps.event.addDomListener(window, "load", initialize);')
js.append('</script>')

return "\n".join(js)
