#!/usr/bin/python

from csvOperations import csvOps

def calcAverageCostOfOrderPerCustomer(file_name):
    """
    Does all the things

    create a dictionary of customer names and their associated prices
    create list of customers
    check dictionary for each customer name and count against customer name
        so for customer in list_o_customers
                customer count 0
                for customer_name in customer_dictionary
                    if customer_name == customer
                        iterate customer count
                        remove dollar sign from price
                        iterate total price
                    average = total price % cusotmer count
                    print customer name + average

    """



calcAverageCostOfOrderPerCustomer('orders.csv')