from osgeo import gdal
import subprocess
import sys

def get_dataset_info(Filename):
	#Open dataset.
	hDataset = gdal.Open(Filename, gdal.GA_ReadOnly)
	#Report subdatasets.
	SUBDATASET_1_NAME=''
	papszMetadata = hDataset.GetMetadata_List("SUBDATASETS")
	for metadata in papszMetadata:
	    if("SUBDATASET_1_NAME" in metadata):
	    	name=metadata.split('/')[1]
	    	SUBDATASET_1_NAME=metadata.split('=')[1]
	return name,SUBDATASET_1_NAME

def processing(path):
	#get info
	name,SUBDATASET_1_NAME=get_dataset_info(path)
	#gdal_translate (Format: xml to Tif
	subprocess.getstatusoutput('gdal_translate '+SUBDATASET_1_NAME+' products/tmp.tif')
	#gdalwarp for reprojection
	subprocess.getstatusoutput('gdalwarp products/tmp.tif products/'+name+'.tif -t_srs EPSG:3857')
	#remove the temporary file
	subprocess.getstatusoutput('rm products/tmp.tif')
	return 1