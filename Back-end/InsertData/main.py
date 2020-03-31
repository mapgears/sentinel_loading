import convertTif2Sql as conv
import postgresDataInsert as db

database_name = 'gisdata'
database_buser = 'faiez'
database_password = 'faiez'
database_port = '5432'
database_host= '127.0.0.1'
table_name= 'tifband'
tif_path= '/var/www/sentinel_loading-master/products/*.tif'
epsg='4326'
SQL_file_name='schema.sql'

create_sql_from_Tif = conv.ConvertTif2Sql(epsg, tif_path, table_name ,SQL_file_name)
create_sql_from_Tif.createSQLfile()
nbr = create_sql_from_Tif.nbr_lines()-1
create_sql_from_Tif.delete_line(nbr)

connect_and_insert = db.PostgresDataInsert(database_name, database_buser, database_password, database_port, database_host,table_name,SQL_file_name)
connect_and_insert.connect()
connect_and_insert.create_table_and_insert_data()
#connect_and_insert.show_table_rows()
connect_and_insert.disconnect()

create_sql_from_Tif.remove_file()