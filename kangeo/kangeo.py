"""Main module."""

import ipyleaflet
import ipywidgets as widgets


class Map(ipyleaflet.Map):
    
    def __init__(self, center=[20, 0], zoom=2, height="600px", **kwargs):
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.layout.height = height

        # Add default basemap
    def add_basemap(self, basemap="OpenTopoMap"):
        url  = eval(f"ipyleaflet.basemaps.{basemap}").build_url()
        layer = ipyleaflet.TileLayer(url=url, name=basemap)
        self.add_layer(layer)

    def add_google_map(self, map_type="SATELLITE"):

        map_types = {
            "SATELLITE": "s",
            "ROADMAP": "m",
            "TERRAIN": "t",
            "HYBRID": "h"
        }
        map_type = map_types [map_type.upper()]

        url = f"https://mt1.googleapis.com/vt/lyrs={map_type.lower()}&x={{x}}&y={{y}}&z={{z}}"
        layer = ipyleaflet.TileLayer(url=url, name=f"Google {map_type}")
        self.add_layer(layer)