import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	#region = rec['region']
	country = rec['country_name']
	longitude = rec['longitude']
	lat = rec['latitude']
	print ('[*] Target: ' + tgt + ' Geo-located. ')
	print ('[+] '+str(city)+', '+str(country))
	print ('[+] Latitude: '+str(lat)+ ', longitude: '+ str(longitude))
tgt = '173.255.226.98'
printRecord(tgt)