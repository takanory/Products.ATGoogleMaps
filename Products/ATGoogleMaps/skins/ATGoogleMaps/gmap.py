print '<script type="text/javascript">'
print "//<![CDATA["
print "window.onload = function() {"
print "    if (GBrowserIsCompatible()) {"
print "        var map = createMap('map', %s, %s, %d, '%s', %s, %s, %s, '%s');" % (
    context.center['latitude'], context.center['longitude'],
    context.zoom, context.mapControl,
    str(context.typeControl).lower(),
    str(context.scaleControl).lower(),
    str(context.overviewControl).lower(),
    context.mapType,
    )

for marker in context.objectValues(['GMarker']):
    try:
        latitude = marker.point['latitude']
        longitude = marker.point['longitude']
        print "        var tabs = ["
        print "          new GInfoWindowTab('%s', document.getElementById('marker_html_%s').innerHTML)" % (marker.tab1 , marker.id)
        if marker.detail:
            print "          ,new GInfoWindowTab('%s', document.getElementById('detail_html_%s').innerHTML)" % (marker.tab2, marker.id)
        print "        ];"
        print "        addMarker(map, tabs, '%s', %s, %s);" % (marker.id, latitude, longitude)
    except:
        continue
print "    }"
print "}"
print "//]]>"
print "</script>"

return printed

