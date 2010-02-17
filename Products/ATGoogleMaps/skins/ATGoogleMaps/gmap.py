site_encoding =  context.plone_utils.getSiteEncoding()

def add_markers(js, markers):
    for marker in markers:
        lat = marker.point['latitude']
        lng = marker.point['longitude']
        js.append('  var marker_%s = createMarker(map, %s, %s, "%s");' % (marker.id, lat, lng, marker.title))
#      shape: shape,
#      shadow: shadow,

# create initialize method
def initialize_func(js):
    lat = context.center['latitude']
    lng = context.center['longitude']
    js.extend(('function initialize() {',
               '  var map = createMap("map_canvas", %s, %s, %s, "%s", "%s", "%s");' % (lat, lng, context.zoom, context.mapType, context.mapTypeControl, context.navigationControl),
               ))

    add_markers(js, context.objectValues(['GMarker']))

    js.append('}')
    
js = ['<script type="text/javascript">']
initialize_func(js)
js.append('google.maps.event.addDomListener(window, "load", initialize);')
js.append('</script>')

return "\n".join(js)

# custom marker javascript
#print """
#      url = "%s";
#      var image = new google.maps.MarkerImage(url + '/gmap_marker.png',
#        new google.maps.Size(20, 34),
#        new google.maps.Point(0,0),
#        new google.maps.Point(8,34));
#      var shadow = new google.maps.MarkerImage(url + '/gmap_shadow.png',
#        new google.maps.Size(37, 34),
#        new google.maps.Point(0,0),
#        new google.maps.Point(9, 34));
#      var shape = {
#        coord: [1, 1, 1, 20, 18, 20, 18 , 1],
#        type: 'poly'
#      }
#""" % context.absolute_url()


