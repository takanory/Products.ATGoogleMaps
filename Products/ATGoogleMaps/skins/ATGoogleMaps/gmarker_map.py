try:
    js = ['<script type="text/javascript">']
    lat = context.point['latitude']
    lng = context.point['longitude']
    js.extend(('function initialize() {',
               '  var latlng = new google.maps.LatLng(%s, %s)' % (lat, lng),
               '  var myOptions = {',
               '    zoom: 14,',
               '    center: latlng,',
               '    mapTypeId: google.maps.MapTypeId.ROADMAP,',
               '    mapTypeControl: false,',
               '    navigationControl: false',
               '  };',
               '  var map = new google.maps.Map(document.getElementById("map"), myOptions);',
               '  var marker = new google.maps.Marker({',
               '    position: latlng,',
               '    map: map',
               '  });'
               '}',
               'google.maps.event.addDomListener(window, "load", initialize);'
               )) 
    js.append('</script>')

    return "\n".join(js)
except:
    return
