site_encoding =  context.plone_utils.getSiteEncoding()

def add_markers(js, markers):
    #js.extend(('function addMarker()'))
    for marker in markers:
        lat = marker.point['latitude']
        lng = marker.point['longitude']
        js.extend(('  var marker_%s = new google.maps.Marker({' % marker.id,
                   '    position: new google.maps.LatLng(%s, %s),' % (lat, lng),
                   '    map: map,',
                   '    title: "%s"' % unicode(marker.Title(), site_encoding),
#                   '    icon: image',
                   '  });',
                   ))
        js.extend(('  var infowindow_%s = new google.maps.InfoWindow({' % marker.id,
                   '    content: "<h2>%s</h2>"' % unicode(marker.Title(), site_encoding),
                   '  });',
                   "  google.maps.event.addListener(marker_%s, 'click', function() {" % marker.id,
                   '    infowindow_%s.open(map, marker_%s)' % (marker.id, marker.id),
                   '  });',
                   ))
#      shape: shape,
#      shadow: shadow,

# create initialize method
def initialize_func(js):
    lat = context.center['latitude']
    lng = context.center['longitude']
    js.extend(('function initialize() {',
	       '  var myOptions = {',
	       '    zoom: %s,' % context.zoom,
	       '    center: new google.maps.LatLng(%s, %s),' % (lat, lng),
	       '    mapTypeId: google.maps.MapTypeId.%s,' % context.mapType,
	       ))

    # set mapTypeControl
    if context.mapTypeControl == "nothing":
	js.append('    mapTypeControl: false,')
    else:
        js.extend(('    mapTypeControl: true,',
		   '    mapTypeControlOptions: {',
		   '      style: google.maps.MapTypeControlStyle.%s,' % context.mapTypeControl,
		   '    },',
		   ))

    # set mavigationControl
    if context.navigationControl == "nothing":
	js.append('    navigationControl: false,')
    else:
        js.extend(('    navigationControl: true,',
		   '    navigationControlOptions: {',
		   '      style: google.maps.NavigationControlStyle.%s' % context.navigationControl,
		   '    },',
		   ))

    js.extend(('  };',
	       '  var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);',
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


