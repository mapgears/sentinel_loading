#!/bin/bash

var1=$(ls products)
#consult all products
for var in $var1
do
	#make a test to know the repertoires
	if [ -z $(echo $var | grep "tif") ]
	then
		var2=$(ls products/$var | grep "SAFE")
		#make a test to know the repertoires
	    if [ -z $var2 ]
			then
	        echo '---'
	    	else
	    	#Fist launch the command gdalinfo
	    	var3=$( gdalinfo products/$var/$var2/MTD_MSIL2A.xml | grep 'SUBDATASET_1_NAME' | cut -d '=' -f 2)	
	    	#second launch the command gdal_translate (Format: xml to Tif)
	    	gdal_translate $var3 "products/tmp.tif"
	    	#third launch the command gdalwarp for reprojection
	    	gdalwarp products/tmp.tif products/${var}.tif -t_srs EPSG:3857
	    	#finally remove the temporary file
	    	rm "products/tmp.tif"
		fi
	fi
done
#Builds a shapefile as a raster tileindex
gdaltindex web_application/data/drgidx.shp products/*.tif