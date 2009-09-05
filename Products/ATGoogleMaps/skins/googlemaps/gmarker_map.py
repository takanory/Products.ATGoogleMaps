try:
    latitude = context.point['latitude']
    longitude = context.point['longitude']
    print '<script type="text/javascript">'
    print "//<![CDATA["
    print "window.onload = function() {"
    print "    if (GBrowserIsCompatible()) {"
    print "        var map = createMap('map', %s, %s, 14);" % (latitude, longitude)
    print "        createMarker(map, %s, %s);" % (latitude, longitude)
    print "    }"
    print "}"
    print "//]]>"
    print "</script>"

    return printed
except:
    return
