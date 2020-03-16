import update.download_product as dp
import update.tif_to_shp
import update.xml_to_tif

featureCollection_path='../FeatureCollection/data.json'
file_input='../Geojson/polygone.geojson'
processing_level='Level-2A'
platform_name='Sentinel-2'
file_output='../products/'
start_date='20200309'
password='11080290'
end_date='20200310'
user='faiezbenamar'
def update_products():
	footprint=dp.read_polygone(file_input)
	api=dp.connect_API(user,password)
	products=dp.search_API(api,footprint,start_date,end_date,platform_name,processing_level)

	dp.show_product(api,products)
	dp.save_FeatureCollection(api,products,featureCollection_path)

	id=0
	P_directory_name=str(api.to_geodataframe(products).beginposition[int(id)])
	P_directory_name=P_directory_name.replace(" ","_")[:19]
	title=api.to_geodataframe(products).title[int(id)]

	title,P_directory_name=dp.download_product(api,products,id,file_output)
	if title!='':
		path_file_xml=file_output+P_directory_name+'/'+title+'.SAFE/MTD_MSIL2A.xml'
		xml_to_tif.processing(path_file_xml)
		tif_to_shp.update_shapefile()
		return 'product updated'
	return 'no new product'