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

# How to use the script
 * use: >> ***python3 script.py -h***
  - -h, --help      show this help message and exit
  - -u user         a string for your username
  - -p password     a string for your password
  - -SD Date        a string for start date searching for images (YYYYMMDD)
  - -ED Date        a string for end date searching for images (YYYYMMDD)
  - -plat platform  a string for your platform name (default: Sentinel-2)
  - -l Level        a string for your processing level (default: Level-2A)
  - -in File        The path of your geojson file
  - -out folder     The path of directory where to save downloaded files
  * use: >>***python3 script.py -u user -p password -SD date -ED date -in path1 -out path2***
