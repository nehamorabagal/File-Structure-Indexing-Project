# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1efgI8QTwUK1KBcTtJDwXgjVn2PhsfCQG
"""

import pandas as pd
import time


class Index1:
    FILENAME = '1L_sales_records.csv'
    csv_df = pd.read_csv(FILENAME)
    region_list = []
    primary_index = {}
    secondary_index = {}

    @staticmethod
    def create_index():
        print("Please wait while data is loading and index is created...")
        start = time.time()
        for index, row in Index1.csv_df.iterrows():
            my_list = ["Region:" + row['Region'],
                       "Country:" + row['Country'],
                       "Item Type:" + row['Item Type'],
                       "Sales Channel:" + row['Sales Channel'],
                       "Order ID:" + str(row['Order ID']),
                       "Unit Price:" + str(row['Unit Price'])]

            #   Creating primary index.
            Index1.primary_index[index] = my_list

            #   Creating secondary index.
            if row['Region'] not in Index1.secondary_index.keys():
                Index1.secondary_index[row['Region']] = [my_list]
            else:
                temp = Index1.secondary_index[row['Region']]
                temp.append(my_list)
        end = time.time()
        print("Creating Index Completed.")
        print('Time taken to create and build index in seconds: ', end - start)
        print()


    @staticmethod
    def get_input():
        region = input("Enter the Region: ")
        country = input("Enter Country Name: ")
        item_type = input("Enter Item Type: ")
        sales_channel = input("Enter Sales Channel: ")
        order_id = input("Enter Order ID: ")
        unit_price = input("Enter Unit Price: ")
        new_row_data = {"Region": region,
                        "Country": country,
                        "Item Type": item_type,
                        "Sales Channel": sales_channel,
                        "Order ID": order_id,
                        "Unit Price": unit_price}
        return new_row_data

    # @staticmethod
    # def write_to_csv(new_data):
    #     Index1.csv_df = Index1.csv_df.append(new_data, ignore_index=True)
    #     Index1.csv_df.to_csv(Index1.FILENAME, index=False)

    @staticmethod
    def new_row_update_df():
        new_data = Index1.get_input()
        Index1.csv_df = Index1.csv_df.append(new_data, ignore_index=True)
        Index1.csv_df.to_csv(Index1.FILENAME, index=False)
        Index1.csv_df = pd.read_csv(Index1.FILENAME)
        Index1.create_index()

    @staticmethod
    def delete_row_update_df(drop_index):
        Index1.csv_df = Index1.csv_df.drop(int(drop_index))
        Index1.csv_df.to_csv(Index1.FILENAME, index=False)
        Index1.csv_df = pd.read_csv(Index1.FILENAME)
        Index1.create_index()

    @staticmethod
    def print_all_dict():
        print("PRIMARY INDEX:\n")
        for key in Index1.primary_index.keys():
            Index1.prettify_primary(key, Index1.primary_index[key])

        print("\nSECONDARY INDEX:\n")
        for key in Index1.secondary_index.keys():
            Index1.prettify_secondary(key, Index1.secondary_index[key])

    @staticmethod
    def print_index_dict(start_i, stop_i):
        out = ""
        for j in range(start_i, stop_i + 1):
            out += "Index: " + str(j) + "\n\t| "
            for l in Index1.primary_index[j]:
                out += l + " | "
            out += "\n"
        print(out)

    @staticmethod
    def prettify_primary(i1, list1):
        out = ""
        out += "Index: " + str(i1) + "\n\t| "
        for l in list1:
            out += l + " | "
        out += "\n"
        print(out)

    @staticmethod
    def prettify_secondary(r1, list_list):
        out = ""
        out += "Index: " + r1
        for sublist in list_list:
            out += "\n\t| "
            for l in sublist:
                out += l + " | "
        out += "\n"
        print(out)


welcome_message = "Welcome: For Indexing"
print(welcome_message)

# i_object = Index1(Index1.FILENAME)
# i_object.create_index()


Index1.create_index()


display_message = ""
display_message += "\tHit [1] - To Search using Primary Index\n"
display_message += "\tHit [2] - To Search using Secondary Index\n"
display_message += "\tHit [3] - To ADD a NEW row to the csv file\n"
display_message += "\tHit [4] - To DELETE a row from the csv file\n"
display_message += "\tHit [5] - To Display values in the given range of index\n"
display_message += "\tHit [6] - To Exit The File\n"
n = int(input(display_message))

# input_validate = [1, 2, 3, 4]
while n != 6:
    if n == 1:
        i = int(input("Enter a Search Index: \n"))
        while i not in range(len(Index1.primary_index)):
            i = int(input("Please Enter a Valid Search Index: \n"))
        start = time.time() * 1000
        for index in range(len(Index1.primary_index)):
            if index == i:
                Index1.prettify_primary(i, Index1.primary_index[i])
                break
        end = time.time() * 1000
        print('Time taken to search using primary index in milli seconds: ', end - start)
        print()
    elif n == 2:
        list1 = []
        r = input("Enter a Region Name(Secondary Index): \n")
        while r not in Index1.secondary_index.keys():
            r = input("Please Enter a Valid Region Name(Secondary Index): \n")
        start = time.time() * 1000
        list1 = Index1.secondary_index[r]
        Index1.prettify_secondary(r, list1)
        end = time.time() * 1000
        print('Time taken to search using secondary index in milli seconds: ', end - start)
        print()
    elif n == 3:
        start = time.time() * 1000
        Index1.new_row_update_df()
        end = time.time() * 1000
        print('Time taken to insert in a file in milli seconds: ', end - start)
        print()
    elif n == 4:
        i = int(input("Enter a Index to Delete: \n"))
        while i not in range(len(Index1.primary_index)):
            i = int(input("Please Enter a Valid Index to Delete: \n"))
        start = time.time() * 1000
        Index1.delete_row_update_df(i)
        end = time.time() * 1000
        print('Time taken to delete a file in milli seconds: ', end - start)
        print()
    elif n == 5:
        i1 = int(input("Enter a Start Index: \n"))
        while i1 not in range(len(Index1.primary_index)):
            i1 = int(input("Please Enter a Valid Start Index: \n"))
        i2 = int(input("Enter a Stop Index: \n"))
        while i2 not in range(len(Index1.primary_index) or i2 < i1):
            i = int(input("Please Enter a Valid Stop Index: \n"))
        start = time.time() * 1000
        Index1.print_index_dict(i1, i2)
        end = time.time() * 1000
        print('Time taken to search a range of index in milli seconds: ', end - start)
        print()
    else:
        print("Invalid Command:\n")
    n = int(input(display_message))

if n == 6:
    print("Thank you, Bye!!")
