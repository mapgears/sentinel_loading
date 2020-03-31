import subprocess
import sys
import os

class ConvertTif2Sql(object):

    def __init__(self, epsg, Tif_path, table_name ,SQL_file_name):
        """Constructor for the instance. """
        self.epsg = epsg
        self.Tif_path = Tif_path
        self.table_name = table_name
        self.SQL_file_name = SQL_file_name
        
    def createSQLfile(self):
        """ Create a Sql file from files Tif with raster2pgsql"""
        command='raster2pgsql -s '+self.epsg+' -I -C -M '+self.Tif_path+' -F '+self.table_name+' > '+self.SQL_file_name
        subprocess.getstatusoutput(command)
        print(command)

    def remove_file(self):
        """ Delete file."""
        command='rm '+self.SQL_file_name
        subprocess.getstatusoutput(command)

    def nbr_lines(self):
        """ Count the number of lines. """
        count = 0
        with open(self.SQL_file_name, 'r') as f:
            for line in f:
                count += 1
        return count

    def delete_line(self, line_number):
        """ Delete a line from a file at the given line number """
        is_skipped = False
        current_index = 0
        dummy_file = self.SQL_file_name + '.bak'
        # Open original file in read only mode and dummy file in write mode
        with open(self.SQL_file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            # Line by line copy data from original file to dummy file
            for line in read_obj:
                # If current line number matches the given line number then skip copying
                if current_index != line_number:
                    write_obj.write(line)
                else:
                    is_skipped = True
                current_index += 1
        # If any line is skipped then rename dummy file as original file
        if is_skipped:
            os.remove(self.SQL_file_name)
            os.rename(dummy_file, self.SQL_file_name)
        else:
            os.remove(dummy_file)
