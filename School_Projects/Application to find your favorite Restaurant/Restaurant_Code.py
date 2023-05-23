from geocode import getGeocodeLocation
import json
import httplib2

foursquare_client_id = "##"
foursquare_client_secret = "##"


def findARestaurant(mealType,location):
	
	latitude, longitude = getGeocodeLocation(location)
	
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	#print result
	
	if result['response']['venues']:
		restaurant = result['response']['venues'][0]
		venue_id = restaurant['id'] 
		restaurant_name = restaurant['name']
		restaurant_address = restaurant['location']['formattedAddress']
		address = ""
		for i in restaurant_address:
			address += i + " "
		restaurant_address = address
		url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
		result = json.loads(h.request(url, 'GET')[1])
		if result['response']['photos']['items']:
			firstpic = result['response']['photos']['items'][0]
			prefix = firstpic['prefix']
			suffix = firstpic['suffix']
			imageURL = prefix + "300x300" + suffix
		else:
			imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
		restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
		print "Restaurant Name: %s" % restaurantInfo['name']
		print "Restaurant Address: %s" % restaurantInfo['address']
		print "Image: %s \n" % restaurantInfo['image']
		return restaurantInfo
	else:
		print "No Restaurants Found for %s" % location
		return "No Restaurants Found"

if __name__ == '__main__':
	while True:
		food = raw_input("Enter the food item you wanna eat:")
		place = raw_input("Enter the location:")
		print "*******************************Searching**************************************"
		print "*******************************Searching**************************************"
		print "*******************************Searching**************************************"
		findARestaurant(food, place)
	
