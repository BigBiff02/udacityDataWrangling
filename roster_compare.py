__author__ = 'rgilbert'
import csv
import re
import xlrd
import xlwt
WW_INSTRUMENTS = ["Flute", "Alto Sax", "Oboe", "Bass Clarinet", "Clarinet", "Bassoon", "Tenor Sax"]
BRASS_INSTRUMENTS = ["Baritone", "French Horn", "Trombone", "Trumpet", "Tuba"]
ROSTER = "c:/Users/rgilbert/Downloads/clean band roster 2013-2014.xlsx"
MISFITS = "c:/Users/rgilbert/Downloads/band roster 2013.xlsx"
next_year_brass_file = "c:/Users/rgilbert/Downloads/next_year_brass.csv"
current_brass_file = "c:/Users/rgilbert/Downloads/current_brass.csv"
new_var = "I am a new var"
next_year_ww_file = "c:/Users/rgilbert/Downloads/next_year_ww.csv"
current_ww_file = "c:/Users/rgilbert/Downloads/current_ww.csv"

def fill_blank_names(sheet_array):
    counter =0
    for row in sheet_array:
        if counter>0:
            if len(row[2])<1:
                row[2]= row[1]
        counter +=1
    return sheet_array

def parse_roster():
    workbook = xlrd.open_workbook(ROSTER)
    sheet = workbook.sheet_by_index(0)
    brass_names = [str(sheet.cell_value(r,2)) + ' ' + str(sheet.cell_value(r,0)) for r in range(sheet.nrows) if sheet.cell_value(r, 5) in BRASS_INSTRUMENTS]
    #all_vals = [sheet.row_values(r, start_colx=0, end_colx=None) for r in range(sheet.nrows)]
    #return fill_blank_names(all_vals)
    print brass_names
    return brass_names

def filter_lists(next_year, current):
    print next_year
    #print current
    results = [name for name in current if name not in next_year]
    #wkbk = xlrd.open_workbook(ROSTER)
    wkbk = xlwt.Workbook()
    sheet = wkbk.add_sheet('misfits')
    for i,v in enumerate(results):
        sheet.write(i, 0, v)
    wkbk.save(MISFITS)
    return results

def comp():
    current = []
    next_year = []
    with open(next_year_brass_file, "r") as f:
        headers = f.readline()
        #print headers
        for line in f:
            vals = line.split(',')

            vals[0] = re.sub(r'[\s"\n]', '', vals[0])
            vals[1] = re.sub(r'["\n]', '', vals[1]).strip()
            if re.search('\s', vals[1]):

                multiname = vals[1].split(' ')
                vals[1] = multiname[0]

            next_year.append(vals[1]+' '+vals[0])
        #print next_year



    with open(current_brass_file, "r") as c:
        c_headers = c.readline()
        for line in c:
            vals = line.split(',')

            vals[0] = re.sub(r'[\s"\n]', '', vals[0])
            vals[1] = re.sub(r'[\s"\n]', '', vals[1])
            current.append(vals[1]+' '+vals[0])

    quitters = filter_lists(parse_roster(), current)
    print len(quitters)
    for t in quitters:
        print t


def fill_in_power_name():
    workbook = xlrd.open_workbook(ROSTER)
    sheet = workbook.sheet_by_index(0)

    data = parse_roster()
    wkbk = xlwt.Workbook()
    sheet = wkbk.add_sheet('misfits')
    #print data[1]
    for i,v in enumerate(data):
       # print type(v)
        for n, cell in enumerate(v):

            sheet.write(i, n, cell)
           #print n
    wkbk.save(MISFITS)

comp()