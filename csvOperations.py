#!/usr/bin/python

import operator
import csv
from csv import DictReader
from collections import Counter
import json

class csvOps:

    def sortCSVbyColumn(self, column, file_name):
        """
        Method to sort csv data by column and return the data. Column
        1 is actually 0... it's like that
        """
        data = self.readCSVFile(file_name)
        sorted_csv = sorted(data, key=operator.itemgetter(column))
        return sorted_csv

    def readCSVFile(self, file_name):
        """
        Method to read a csv file and return the data in it
        """
        data = csv.reader(open(file_name), delimiter=',')
        return data

    def removeCSVHeader(self, file_name):
        """
        This method should check to see if the header exists
        right now the first row goes bye bye no matter what
        """
        csv_without_header = []
        with open(file_name) as csv_file:
            read_csv = csv.reader(csv_file)
            for row in read_csv:
                if read_csv.line_num == 1:
                    continue
                csv_without_header.append(row)

        return csv_without_header

    def writeCSVFile(self, new_file, csv_data):
        """
        Method to write a csv file
        """
        with open(new_file, 'w') as file:
            csv.writer(file).writerows(csv_data)

    def printCSVData(self, data):
        print(data)

    def createDictFromCsvColumn(self, file_name, header_id):
        """
        This feels like cheating to use Dictreader but its efficient.
        Method takes the filename and header id and creates a dictionary
        from the header id column
        """
        with open(file_name) as csv_file:
            column = [row[header_id] for row in DictReader(csv_file)]
        return column

    def countDataInColumn(self, dict_data):
        """
        This too feels like cheating. Uses the counter util to count the dictionary
        """
        return Counter(dict_data)

    def formatCountedDataAndPrint(self, counted_list):
        """
        Formats the counted data in the dictionary to be a little more readable
        """
        for key, val in counted_list.items():
            print(key, val)

    def createJson(self, filename, json_file):
        data = []
        with open(filename) as file:
            for row_data in DictReader(file):
                data.append(row_data)

        json_data = json.dumps(data)

        with open(json_file, 'w') as newfile:
            for line in json_data:
                newfile.write(line)

