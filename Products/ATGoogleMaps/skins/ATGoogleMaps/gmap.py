# create initialize method
def initialize_func(js):
    lat = context.center['latitude']
    lng = context.center['longitude']
    js.extend(('function initialize() {',
	       '  var myOptions = {',
	       '    zoom: %s,' % context.zoom,
	       '    center: new google.maps.LatLng(%s, %s),' % (lat, lng),
	       '    mapTypeId: google.maps.MapTypeId.%s,' % context.mapType
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
    
js = ['<script type="text/javascript">']
initialize_func(js)
print "\n".join(js)

# custom marker javascript
print """
      url = "%s";
      var image = new google.maps.MarkerImage(url + '/gmap_marker.png',
        new google.maps.Size(20, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(8,34));
      var shadow = new google.maps.MarkerImage(url + '/gmap_shadow.png',
        new google.maps.Size(37, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(9, 34));
      var shape = {
        coord: [1, 1, 1, 20, 18, 20, 18 , 1],
        type: 'poly'
      }
       

""" % context.absolute_url()

# marker javascript
for marker in context.objectValues(['GMarker']):
        lat = marker.point['latitude']
        lng = marker.point['longitude']

        print """
    var infowindow_%s = new google.maps.InfoWindow({
      content: '<h1>%s</h1>%s'
    });

    var marker_%s = new google.maps.Marker({
      position: new google.maps.LatLng(%s, %s),
      map: map,
      title: "%s",
      icon: image,
      shape: shape,
      shadow: shadow,
    });

    google.maps.event.addListener(marker_%s, 'click', function() {
      infowindow_%s.open(map, marker_%s);
    });
        """ % (marker.id, marker.Title(), marker.Description(), marker.id, lat, lng, marker.Title(), marker.id, marker.id, marker.id)

print """
  }
  window.onload = initialize;
</script>"""

return printed
