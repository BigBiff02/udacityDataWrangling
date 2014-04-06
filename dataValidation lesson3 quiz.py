"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def check_num_and_write(year):
    
    
    try:
        float(year[0])
        if float(year[0]) > float(1885) and float(year[0])<float(2015):
            return True
        else:
            print year[0]
    except:
        return False

def check_URI(uri):
    u = uri.split('//')
    try:
        u[1]
        if u[1].split('/')[0] == 'dbpedia.org':
            print u[0]
            return True
        return false
    except:
        print u
        return False

def process_file(input_file, output_good, output_bad):
    good_vals = []
    bad_vals = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        year_col = header.index('productionStartYear')
        for i, val in enumerate(reader):
            if i>0:                
                uri = val['URI']
                
                if check_URI(uri):
                    year = val['productionStartYear'].split('-')
                    if check_num_and_write(year):
                        val['productionStartYear'] = year[0]
                        good_vals.append(val)
                    else:
                        bad_vals.append(val)
                             
        #COMPLETE THIS FUNCTION



    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
        
    with open(output_good, "w") as g:
        
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()            
        for q in good_vals:
            print q['productionStartYear']
            writer.writerow(q)
            
    with open(output_bad, "w") as h:
        
        writer = csv.DictWriter(h, delimiter=",", fieldnames= header)
        writer.writeheader()            
        for q in bad_vals:
            writer.writerow(q)
    

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
