#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "/home/ryan/Udacity Data Wrangling Class/chapter2extraWorkFile.html"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []
    info = {}
    #info["courier"], info["airport"] = f[:6].split("-")
    
    with open(f, "r") as html:

        soup = BeautifulSoup(html)
        full_list = soup.find_all('tr', class_="dataTDRight")
        for row in full_list:
			row_data = row.find_all('td')
			if row_data[1].get_text()!="TOTAL":
				data.append({"courier": "delta",
                             "airport": "ATL",
                             "year": row_data[0].get_text(),
                             "month": row_data[1].get_text(),
                             "flights": {"domestic": row_data[2].get_text(),
                                         "international": row_data[3].get_text()}
                            })

    print data

    #return data


def test():
    print "Running a simple test..."
    #~ open_zip(datadir)
    #~ files = process_all(datadir)
    #~ data = []
    #~ for f in files:
        #~ data += process_file(f)
    process_file(datadir)
    #~ assert len(data) == 399
    #~ for entry in data[:3]:
        #~ assert type(entry["year"]) == int
        #~ assert type(entry["flights"]["domestic"]) == int
        #~ assert len(entry["airport"]) == 3
        #~ assert len(entry["courier"]) == 2
    #~ assert data[-1]["airport"] == "ATL"
    #~ assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    #~ 
    #~ print "... success!"

if __name__ == "__main__":
    test()
