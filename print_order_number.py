#!/usr/bin/python

from csvOperations import csvOps

def printOrdersPerCustomer(file_name):
    """
    Prints out the number of orders per customer
    """
    csv_handler = csvOps()
    dict_data = csv_handler.createDictFromCsvColumn(file_name, 'Customer Name')
    counted_data = csv_handler.countDataInColumn(dict_data)
    csv_handler.formatCountedDataAndPrint(counted_data)

def calcAverageCostOfOrderPerCustomer(file_name):
    """
    Does all the things
    """

printOrdersPerCustomer('orders.csv')

