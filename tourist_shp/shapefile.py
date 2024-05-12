"""
Created on Wed Nov 22 22:40:42 2023

@author: dell
"""

import pandas as pd
import geopandas as gpd
# read an excel file and convert into a dataframe object
df = pd.DataFrame(pd.read_excel("C:/Users/dell/Desktop/Women in GIS mentorship/Assignment 2/tourist_shp/Tourist sites sorted.xlsx"))
# show the dataframe
df 
#Read and store content of an excel file 
read_file = pd.read_excel ("C:/Users/dell/Desktop/Women in GIS mentorship/Assignment 2/tourist_shp/Tourist sites sorted.xlsx") 
# Write the dataframe object 
# into csv file
read_file.to_csv ("Tourist sites sorted.csv",  
                  index = None, 
                  header=True)
# read csv file and convert into a dataframe object
df = pd.DataFrame(pd.read_csv("Tourist sites sorted.csv"))
# show the dataframe
df
#read Csv file using pandas
tourist_data= pd.read_csv('Tourist sites sorted.csv')
#creating a geopandas geodataframe
tourist_gdf= gpd.GeoDataFrame(tourist_data, geometry = gpd.points_from_xy(tourist_data['Longitude'], tourist_data['Latitude']))
tourist_gdf.plot()
ESRI_WKT= 'GEOGCS["GCS_Arc_1950",DATUM["D_Arc_1950",SPHEROID["Clarke_1880_Arc",6378249.145,293.4663077]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
#Save file as an ESRI shapefile
tourist_gdf.to_file(filename= 'touristsites.shp', driver= 'ESRI Shapefile', crs= ESRI_WKT ) 

