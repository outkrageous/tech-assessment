#!/usr/bin/python

from csvOperations import csvOps


def getCustomerListSortedByName(file_name):
    """
    Takes the specified csv file and sorts it by the customer name
    prints the sorted data stdout and writes a new csv with the sorted data

    """
    csv_handler = csvOps()
    clean_data = csv_handler.removeCSVHeader(file_name)
    csv_handler.writeCSVFile('orders_noheader.csv', clean_data)
    sorted_data = csv_handler.sortCSVbyColumn(2, 'orders_noheader.csv')
    csv_handler.writeCSVFile('sort_by_name.csv', sorted_data)
    csv_handler.printCSVData(sorted_data)

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


#getCustomerListSortedByName('orders.csv')
printOrdersPerCustomer('orders.csv')

