from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from osgeo import gdal
import argparse
import json

parser = argparse.ArgumentParser(usage='This script allows you to Search Sentinel-2 imagery using Sentinelsat API')
parser.add_argument('-u', metavar='user', type=str,
                    help='a string for your username',dest='user')
parser.add_argument('-p', metavar='password', type=str,
                    help='a string for your password',dest='password')
parser.add_argument('-SD', metavar='Date', type=str,dest='start_date',
                    help='a string for start date searching for images [YYYYMMDD]')
parser.add_argument('-ED', metavar='Date', type=str,dest='end_date',               
                    help='a string for end date searching for images [YYYYMMDD]')
parser.add_argument('-plat', metavar='platform', type=str,default='Sentinel-2',
                    help='a string for your platform name (default: Sentinel-2)',dest='platform_name')
parser.add_argument('-l', metavar='Level', type=str,default='Level-2A',
                    help='a string for your processing level (default: Level-2A)',dest='processing_level')
parser.add_argument('-in', metavar='File', type=str,default='/home/faiez_benamar/Bureau/doc/polygone.geojson',
                    help='The path of your geojson file',dest='file_input')
parser.add_argument('-out', metavar='folder', type=str,dest='file_output',default='./products',
                    help='The path of directory where to save downloaded files')
args = parser.parse_args()

#read geojson file
footprint = geojson_to_wkt(read_geojson(args.file_input))

# connect to the API
api = SentinelAPI(args.user,args.password,'https://scihub.copernicus.eu/dhus')

# search by polygon
print ("The coordinates of our geometry: \n" + footprint)
products = api.query(area=footprint,
                     initial_date=args.start_date,
                     end_date=args.end_date,
                     platformname=args.platform_name,
                     processinglevel=args.processing_level)

#number of products found
print("The number of data found: "+str(len(products)))

#show the universally unique identifier of each product
print("The uuids <universally unique identifier> of data found:")
uuid_list=api.to_geodataframe(products).uuid
for i in range(len(uuid_list)):
	print('products N '+str(i)+': '+str(list(uuid_list)[i]))

# GeoJSON FeatureCollection containing footprints and metadata of the scenes
data=api.to_geojson(products)
with open('./FeatureCollection/data.json', 'w') as outfile:
    json.dump(data, outfile)

P_download=input("do you want to download a product(T/F): ")
# download single scene by known product id
if (P_download=='T'):
	P_id= input("Enter product id: ")
	api.download(P_id, directory_path=args.file_output)