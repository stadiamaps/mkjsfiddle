import os.path as path

from mkjsfiddle.parser import ScriptAndStyleParser

here = path.abspath(path.dirname(__file__))

test_data = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Vector Map Demo</title>
        <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no" />
        <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/mapbox-gl/0.52.0/mapbox-gl.js"></script>
        <link href="//cdnjs.cloudflare.com/ajax/libs/mapbox-gl/0.52.0/mapbox-gl.css" rel="stylesheet" />
        <style type="text/css">
            body {
              margin: 0;
              padding: 0;
            }

            #map {
              position: absolute;
              top: 0;
              bottom: 0;
              width: 100%;
            }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script type="text/javascript">
         var map = new mapboxgl.Map({
           container: 'map',
           style: 'https://tiles.stadiamaps.com/styles/alidade_smooth.json',  // Theme URL; see our themes documentation for more options
           center: [12, 53],  // Initial focus coordinate
           zoom: 4
         });
         
         // Mapbox GL JS has a bug in it's handling of RTL, so we have to grab this dependency as well until they
         // combine it with the main library
         mapboxgl.setRTLTextPlugin('https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.2.1/mapbox-gl-rtl-text.js');

         // Add zoom and rotation controls to the map.
         map.addControl(new mapboxgl.NavigationControl());
        </script>
    </body>
</html>"""

html_data = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Vector Map Demo</title>
        <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
        <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/mapbox-gl/0.52.0/mapbox-gl.js"></script>
        <link href="//cdnjs.cloudflare.com/ajax/libs/mapbox-gl/0.52.0/mapbox-gl.css" rel="stylesheet">
    </head>
    <body>
        <div id="map"></div>
    </body>
</html>"""

js_data = """var map = new mapboxgl.Map({
  container: 'map',
  style: 'https://tiles.stadiamaps.com/styles/alidade_smooth.json',  // Theme URL; see our themes documentation for more options
  center: [12, 53],  // Initial focus coordinate
  zoom: 4
});

// Mapbox GL JS has a bug in it's handling of RTL, so we have to grab this dependency as well until they
// combine it with the main library
mapboxgl.setRTLTextPlugin('https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.2.1/mapbox-gl-rtl-text.js');

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());
"""

css_data = """body {
  margin: 0;
  padding: 0;
}

#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}
"""


def test_extraction():
    """Test the parser's ability to separate HTML, JS and CSS input"""
    parser = ScriptAndStyleParser()
    parser.feed(test_data)

    assert parser.html_body == html_data
    assert parser.js_body == js_data
    assert parser.css_body == css_data
