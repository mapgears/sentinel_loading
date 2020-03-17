from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from geojson import Polygon, Feature, FeatureCollection, dump
from osgeo import gdal
import argparse
import zipfile
import string
import json
import os

def extracter_zip(title,pathDirectory):
	dirlist = os.listdir(str(pathDirectory))
	P_extract=False
	for i_dirlist in dirlist :
		if(str(title+'.SAFE')==i_dirlist):
			P_extract=True
	if P_extract==False:
		print('pleasse attend to extract product ...')
		with zipfile.ZipFile(pathDirectory+'/'+title+'.zip', 'r') as zip_ref:
			zip_ref.extractall(pathDirectory)

def createDirectory(path,name):
	# Create target Directory if don't exist
	dirName = path+name
	if not os.path.exists(dirName):
	    os.mkdir(dirName)
	    return 'F'
	return 'T'

def show_product(api,products):
	#show the List of data found
	P_list=api.to_geodataframe(products).uuid
	for i in range(len(P_list)):
		summary=api.to_geodataframe(products).summary[i]
		print('*id: '+"{:0>3d}".format(i)+' *Title: '+ api.to_geodataframe(products).title[i]+' *'+summary[summary.find('Size'):]+" *cloud%: {:.3f}".format(api.to_geodataframe(products).cloudcoverpercentage[i]))

def save_FeatureCollection(api,products,path) :
	# GeoJSON FeatureCollection containing footprints and metadata of the scenes
	data=api.to_geojson(products)
	with open(path,'w') as outfile:
	    json.dump(data, outfile)

def read_polygone(path):
	#read geojson file
	return geojson_to_wkt(read_geojson(path))

def write_polygone(file_input,Polygon,country=""):
	features = []
	features.append(Feature(geometry=Polygon, properties={"name_fr": country}))
	feature_collection = FeatureCollection(features)
	with open(file_input, 'w') as f:
	   dump(feature_collection, f)

def connect_API(user,password):
	# connect to the API
	return SentinelAPI(user,password,'https://scihub.copernicus.eu/dhus')

def search_API(api,footprint,start,end,platform,level):
	# search by polygon
	print ("The coordinates of our geometry: \n" + footprint)
	return api.query(area=footprint,initial_date=start,end_date=end,platformname=platform,processinglevel=level)

def download_product(api,products,P_id,file_output):
	# download and extract single scene by known product id
	P_directory_name=str(api.to_geodataframe(products).beginposition[int(P_id)])
	P_directory_name=P_directory_name.replace(" ","_")[:19]

	P_exist=createDirectory(file_output,P_directory_name)
	if P_exist=='F':
		directory_path=file_output+P_directory_name
		api.download(api.to_geodataframe(products).uuid[int(P_id)], directory_path=file_output+P_directory_name)
		title=api.to_geodataframe(products).title[int(P_id)]
		extracter_zip(title,file_output+P_directory_name)
		return title,P_directory_name
	return '',P_directory_name
