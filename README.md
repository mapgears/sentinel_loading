# sentinel_loading
Scripts that check Sentinel API to load new version of raster data

# Getting Started
## Prerequisites
What things you need to run this script and how to install them
 * The sentinelsat libraries: 
 * to install use: >>***pip3 install sentinelsat***
 * The argparse libraries: 
 * to install use: >>***pip3 install argparse***
 * The json libraries: 
 * to install use: >>***pip3 install json***
 * The osgeo libraries:
 * to install use: >>***pip3 install GDAL == 'GDAL VERSION FROM OGRINFO'***

# Code description

1. connect to the API
2. read geojson file
3. search by geometry
4. download products
