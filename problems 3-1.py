FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]
          
ROWS = ["one", "two", "three"]

def nest():
	d = {}
	for i in FIELDS:
		d[i] = []
		for t in ROWS:
			d[i].append(t)
			try:
				float(t)
			except:
				pass         
		

	print d


nest()
