import json, requests
from fuzzywuzzy import fuzz
import itertools
from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

# # import re
url1 = 'https://api.foursquare.com/v2/venues/search'
url2 = 'https://api.foursquare.com/v2/venues/'
url3 = 'https://api.foursquare.com/v2/venues/explore'
USER_ID='BBR2BVZJIUIPNFVKSAIEJZMI2KU0LVDLG42WCX55U34JHFWH'
SECRET='I5P3JBEA1ICUR3HNHYICPSQLNR4E5UXJEMXIFRG12SXXGNEZ'
# # USER_ID='TYRYTGKWKWJR5PMEZBCUKSW1BC4KUHMEB3OVB2YZSOIBQTEO'
# # SECRET='VL40XCHT0HJMZ5HNRDB0G5GCO2B20B2M1ERUKBOP4RQGTIWS'




def search_venue(interests):
	params = dict(
	  client_id=USER_ID,
	  client_secret=SECRET,
	  v='20180323',
	  near='San Francisco, CA',
	  checkin='browse',
	  query=interests,
	  limit=5,
	  radius=8000
	)
	resp = requests.get(url=url1, params=params)
	data = json.loads(resp.text)
	return data

def get_details(id):
	params = dict(
	  client_id=USER_ID,
	  client_secret=SECRET,
	  v='20180323')
	#print(url2+str(id))
	resp = requests.get(url=url2+str(id),params=params)
	data2 = json.loads(resp.text)	
	return data2

def search_trendy(no):
	params = dict(
	  client_id=USER_ID,
	  client_secret=SECRET,
	  v='20180323',
	  near='San Francisco, CA',
	  #checkin='browse',
	  section='topPicks',
	  limit=no,
	  radius=8000
	)
	resp = requests.get(url=url3, params=params)
	data = json.loads(resp.text)
	return data


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/result', methods=['GET'])
def getItenary():
	inp =  {"interests":["Mini Golf","Clothing Store"],"food":["Burget Joint","Coffee Shop"]}
	input_json = json.dumps(inp)
	inp = json.loads(input_json)
	l = []
	for i in inp['interests']:
		l.append(i)
	for i in inp['food']:
		l.append(i)
	print(l)

	response = {}
	inters = []
	#data = {u'meta': {u'code': 200, u'requestId': u'5b50d2d2db04f50b20284df4'}, u'response': {u'geocode': {u'parents': [], u'what': u'', u'where': u'san francisco ca', u'feature': {u'highlightedName': u'<b>San Francisco</b>, <b>CA</b>, United States', u'displayName': u'San Francisco, CA, United States', u'name': u'San Francisco', u'longId': u'72057594043319895', u'cc': u'US', u'id': u'geonameid:5391959', u'geometry': {u'center': {u'lat': 37.77493, u'lng': -122.41942}, u'bounds': {u'sw': {u'lat': 37.708085, u'lng': -122.536232}, u'ne': {u'lat': 37.833687, u'lng': -122.34905}}}, u'matchedName': u'San Francisco, CA, United States', u'woeType': 7, u'slug': u'san-francisco-california'}}, u'venues': [{u'verified': False, u'name': u'Subpar Miniature Golf', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.805965, u'lng': -122.42273, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94109', u'state': u'CA', u'formattedAddress': [u'San Francisco, CA 94109', u'United States'], u'lat': 37.805965, u'lng': -122.42273}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'5b1d99216f706a002c077a84', u'categories': [{u'pluralName': u'Mini Golf Courses', u'primary': True, u'name': u'Mini Golf', u'shortName': u'Mini Golf', u'id': u'52e81612bcbc57f1066b79eb', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/golfcourse_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'MINI of San Francisco Service Center', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.78043700168738, u'lng': -122.40929846524473, u'label': u'display'}], u'neighborhood': u'SoMa', u'cc': u'US', u'country': u'United States', u'postalCode': u'94103', u'state': u'CA', u'formattedAddress': [u'1023 Mission St', u'San Francisco, CA 94103', u'United States'], u'address': u'1023 Mission St', u'lat': 37.78043700168738, u'lng': -122.40929846524473}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'5727a17ecd1040df68579d85', u'categories': [{u'pluralName': u'Automotive Shops', u'primary': True, u'name': u'Automotive Shop', u'shortName': u'Automotive', u'id': u'4bf58dd8d48988d124951735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/shops/automotive_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'MiNi Nails & Waxing', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.79051733997, u'lng': -122.42118536110195, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94109', u'state': u'CA', u'formattedAddress': [u'1621 California St (btwn Van Ness & Polk)', u'San Francisco, CA 94109', u'United States'], u'crossStreet': u'btwn Van Ness & Polk', u'address': u'1621 California St', u'lat': 37.79051733997, u'lng': -122.42118536110195}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'4b2d7ba3f964a52098d724e3', u'categories': [{u'pluralName': u'Cosmetics Shops', u'primary': True, u'name': u'Cosmetics Shop', u'shortName': u'Cosmetics', u'id': u'4bf58dd8d48988d10c951735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/shops/beauty_cosmetic_', u'suffix': u'.png'}}]}, {u'verified': True, u'name': u'MINI of San Francisco', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.78269968474699, u'lng': -122.4210094996542, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94102', u'state': u'CA', u'formattedAddress': [u'799 Van Ness Ave (Eddy St)', u'San Francisco, CA 94102', u'United States'], u'crossStreet': u'Eddy St', u'address': u'799 Van Ness Ave', u'lat': 37.78269968474699, u'lng': -122.4210094996542}, u'venuePage': {u'id': u'53544957'}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'4a43924af964a52091a61fe3', u'categories': [{u'pluralName': u'Automotive Shops', u'primary': True, u'name': u'Automotive Shop', u'shortName': u'Automotive', u'id': u'4bf58dd8d48988d124951735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/shops/automotive_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'Peralta Mini Park', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.746134545577306, u'lng': -122.40889320489723, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94110', u'state': u'CA', u'formattedAddress': [u'200 Peralta Avenue (Mullen Avenue)', u'San Francisco, CA 94110', u'United States'], u'crossStreet': u'Mullen Avenue', u'address': u'200 Peralta Avenue', u'lat': 37.746134545577306, u'lng': -122.40889320489723}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'4ad9e2f2f964a520961b21e3', u'categories': [{u'pluralName': u'Dog Runs', u'primary': True, u'name': u'Dog Run', u'shortName': u'Dog Run', u'id': u'4bf58dd8d48988d1e5941735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/dogrun_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'Mini Dog Park', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.79651480933364, u'lng': -122.41735966058928, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94109', u'state': u'CA', u'formattedAddress': [u'1235 Broadway', u'San Francisco, CA 94109', u'United States'], u'address': u'1235 Broadway', u'lat': 37.79651480933364, u'lng': -122.41735966058928}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'4e6ace411f6e1e74e4670a77', u'categories': [{u'pluralName': u'Dog Runs', u'primary': True, u'name': u'Dog Run', u'shortName': u'Dog Run', u'id': u'4bf58dd8d48988d1e5941735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/dogrun_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'MINI of San Francisco (Service)', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.77064225761089, u'lng': -122.41651305675623, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94103', u'state': u'CA', u'formattedAddress': [u'1675 Howard St (S Van Ness Ave)', u'San Francisco, CA 94103', u'United States'], u'crossStreet': u'S Van Ness Ave', u'address': u'1675 Howard St', u'lat': 37.77064225761089, u'lng': -122.41651305675623}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'522657b411d28e35f61e0cce', u'categories': [{u'pluralName': u'Auto Dealerships', u'primary': True, u'name': u'Auto Dealership', u'shortName': u'Auto Dealer', u'id': u'4eb1c1623b7b52c0e1adc2ec', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/shops/automotive_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'Page and Laguna Mini Park', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.77358168449208, u'lng': -122.42529194239862, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'state': u'CA', u'formattedAddress': [u'275 Page St. (Laguna)', u'San Francisco, CA', u'United States'], u'crossStreet': u'Laguna', u'address': u'275 Page St.', u'lat': 37.77358168449208, u'lng': -122.42529194239862}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'4b6468bdf964a520e1b02ae3', u'categories': [{u'pluralName': u'Parks', u'primary': True, u'name': u'Park', u'shortName': u'Park', u'id': u'4bf58dd8d48988d163941735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/park_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'Presidio Golf Course', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.79056496678854, u'lng': -122.45973243289684, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94129', u'state': u'CA', u'formattedAddress': [u'300 Finley Rd (Arguello Blvd.)', u'San Francisco, CA 94129', u'United States'], u'crossStreet': u'Arguello Blvd.', u'address': u'300 Finley Rd', u'lat': 37.79056496678854, u'lng': -122.45973243289684}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'4f99cababe776dab0cd27a3b', u'categories': [{u'pluralName': u'Golf Courses', u'primary': True, u'name': u'Golf Course', u'shortName': u'Golf Course', u'id': u'4bf58dd8d48988d1e6941735', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/golfcourse_', u'suffix': u'.png'}}]}, {u'verified': False, u'name': u'MINI shuttle', u'referralId': u'v-1532023506', u'venueChains': [], u'hereNow': {u'count': 0, u'groups': [], u'summary': u'Nobody here'}, u'contact': {}, u'hasPerk': False, u'location': {u'city': u'San Francisco', u'labeledLatLngs': [{u'lat': 37.770677, u'lng': -122.417674, u'label': u'display'}], u'cc': u'US', u'country': u'United States', u'postalCode': u'94103', u'state': u'CA', u'formattedAddress': [u'San Francisco, CA 94103', u'United States'], u'lat': 37.770677, u'lng': -122.417674}, u'beenHere': {u'count': 0, u'unconfirmedCount': 0, u'marked': False, u'lastCheckinExpiredAt': 0}, u'stats': {u'checkinsCount': 0, u'tipCount': 0, u'visitsCount': 0, u'usersCount': 0}, u'id': u'507ed016e4b09a52c003ccc1', u'categories': [{u'pluralName': u'Moving Targets', u'primary': True, u'name': u'Moving Target', u'shortName': u'Moving Target', u'id': u'4f2a23984b9023bd5841ed2c', u'icon': {u'prefix': u'https://ss3.4sqi.net/img/categories_v2/travel/movingtarget_', u'suffix': u'.png'}}]}]}}
	for interests in l:
		
		i = {}
		ids = []
		data = search_venue(interests)
		for i in data['response']['venues']:
			for c in i['categories']:
				if fuzz.token_set_ratio(c['pluralName'],interests)>50:
					ids.append(i['id'])
		ids = list(set(ids))

		like=0
		inter={}
		if len(ids)==1:
			d2 = get_details(ids[0])
			#print(d2)
			
			inter['activity']=str(interests)
			inter['lat'] = d2['response']['venue']['location']['lat']
			inter['lng'] = d2['response']['venue']['location']['lng']
			inter['name'] = d2['response']['venue']['name']
			try:
				inter['contact'] = d2['response']['venue']['contact']['formattedPhone']
			except:
				inter['contact'] = None
			location = d2['response']['venue']['location']['formattedAddress']
			inter['like'] = d2['response']['venue']['likes']['count']
			inter['location'] = ' '.join(location)
			inters.append(inter)
			inter={}
			
		else:
			for one in ids:
				inter['activity']=str(interests)
				d2 = get_details(one)
				#print(d2)
				
				if d2['response']['venue']['likes']['count']>like:
					inter['lat'] = d2['response']['venue']['location']['lat']
					inter['lng'] = d2['response']['venue']['location']['lng']
					inter['like'] = d2['response']['venue']['likes']['count']
					inter['name'] = d2['response']['venue']['name']
					try:
						inter['contact'] = d2['response']['venue']['contact']['formattedPhone']
					except:
						inter['contact'] = None
					location = d2['response']['venue']['location']['formattedAddress']
					inter['location'] = ' '.join(location)
			inters.append(inter)
			inter={}

	hours = 10

	intera=[]
	if len(inters)<hours:
		data=search_trendy(hours-len(inters))
		for i in data['response']['groups']:
			for d in i['items']:
				inter={}
				inter['name'] = d['venue']['name']
				location = d['venue']['location']['formattedAddress']
				inter['location'] = ' '.join(location)
				inter['lat'] = d['venue']['location']['lat']
				inter['lng'] = d['venue']['location']['lng']
				inter['activity'] ='popular'
				inter['contact'] = None
				inter['like']=None
				intera.append(inter)
	#print(intera)
	response={}
	response['data']=intera+inters
	return json.dumps(response)


    
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", debug=True, threaded=True)

