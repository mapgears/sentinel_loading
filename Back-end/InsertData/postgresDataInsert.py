import subprocess
import psycopg2
import time
import sys
import os

class PostgresDataInsert:

    def __init__(self, db_name, dbuser,dbpassword, dbport,dbhost,dbtable,SQL_file_name):
        """Constructor for the instance. Options for conecting to a database."""
        self.db_name = db_name
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbport = dbport
        self.dbhost=dbhost
        self.db_table_name=dbtable
        self.SQL_file_name=SQL_file_name

    def connect(self):
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(
                "dbname={0} user={1} password={2} port={3} host={4}" 
                .format(self.db_name,
                        self.dbuser,
                        self.dbpassword,
                        self.dbport,
                        self.dbhost))

            # create a cursor
            self.cur = self.conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            self.cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            self.db_version = self.cur.fetchone()
            print(self.db_version)

            print('Database connection established.')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_table_and_insert_data(self):
        """ Creates a table from schema.sql """        
        self.cur.execute("DROP TABLE IF EXISTS "+self.db_table_name+" ;")
        self.cur.execute(open(self.SQL_file_name, "r").read())
        self.conn.commit()
        print('Table '+self.db_table_name+' created.')

    def show_table_rows(self):
        """ Creates a table from schema.sql """        
        self.cur.execute("SELECT filename FROM "+self.db_table_name+" ;")
        for row in self.cur.fetchall():
            print(row)

    def disconnect(self):
        """ Disconnects from the PostgreSQL database server """
        self.cur.close()
        print('Database connection ended.')