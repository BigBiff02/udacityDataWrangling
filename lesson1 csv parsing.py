# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = "/home/ryan/Downloads/"
DATAFILE = "/home/ryan/Downloads/beatles-diskography.csv"


def parse_file(datafile):
    data = []
    
    with open(datafile, "rb") as f:
        keys = f.readline().split(',');
        counter = 10
        for line in f:
			
			
            if counter==0:
                break
            vals = line.split(',')
            row = {}
            for h, val in enumerate(keys):
                row[keys[h].strip()] = vals[h].strip()
            print row
            data.append(row)
            counter-=1
    return data


def test():
    # a simple test of your implemetation
    datafile = DATAFILE
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '\xe2\x80\x94', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '\xe2\x80\x94', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline
    #print d

    
test()
