import folium


class Map(folium.Map):
    """
    A class that extends folium.Map to create a map with a specific center and zoom level.
    """

    def __init__(self, center=(0, 0), zoom=2, **kwargs):
        super().__init__(location=center, zoom_start=zoom, **kwargs)
        folium.LayerControl().add_to(self)
        self.center = center
        self.zoom_start = zoom

    def add_marker(self, location, popup=None, **kwargs):
        """
        Adds a marker to the map at the specified location.
        """
        folium.Marker(location=location, popup=popup, **kwargs).add_to(self)
