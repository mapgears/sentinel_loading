from osgeo import gdal
import geopandas as gpd
from shapely.geometry import box
import os

# compute the bounding box of a gdal raster file
def bounds_raster(path):
    raster = gdal.Open(path) 
    ulx, xres, xskew, uly, yskew, yres  = raster.GetGeoTransform()
    lrx = ulx + (raster.RasterXSize * xres) 
    lry = uly + (raster.RasterYSize * yres)
    return box(lrx,lry,ulx,uly)

def update_shapefile():
	StartDir='./products'
	# creation of the index file
	df = gpd.GeoDataFrame(columns=['location'])
	# iterate through multiple tif files in a folder
	for dir, subdir, files in os.walk(StartDir):
	    for fname in files:
	        if fname.endswith(".tif"):
	        	df = df.append({'location': '/var/www/sentinel_loading-master/products/'+fname,'geometry': bounds_raster( os.path.join(dir+"/", fname))},ignore_index=True)
	# save resulting shapefile
	df.to_file("./web_application/data/drgidx.shp")
	return 1