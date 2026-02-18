import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

gdf = gpd.read_file("Zona_Top5_Prioritas.geojson")
lat = gdf.geometry.centroid.y.mean()
lon = gdf.geometry.centroid.x.mean()
m = folium.Map(location=[lat, lon], zoom_start=12)
folium.GeoJson(gdf).add_to(m)
st_folium(m, width=700, height=500)