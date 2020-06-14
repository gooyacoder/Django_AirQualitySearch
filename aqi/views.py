from django.shortcuts import render


def home(request):
	import requests
	import json

	if request.method == 'POST':
		city = request.POST['city']
		error = False
		status = ''
		status_color = ''
		try:
			request_api = requests.get('http://api.waqi.info/feed/' + city + '/?token=e6089546a3dc14e1fe3d717777e9c7df3e7e5f99')
			api = json.loads(request_api.content)
			if api['data']['aqi'] < 51:
				status = 'Good'
				status_color = 'good'
			elif api['data']['aqi'] < 101:
				status = 'Moderate'
				status_color = 'moderate'
			elif api['data']['aqi'] < 151:
				status = 'Unhealthy for Sensitive Groups'
				status_color = 'usg'
			elif api['data']['aqi'] < 201:
				status = 'Unhealthy'
				status_color = 'unhealthy'
			elif api['data']['aqi'] < 301:
				status = 'Very Unhealthy'
				status_color = 'veryunhealty'
			else:
				status = 'Hazardous'
				status_color = 'hazardous'
		except Exception as e:
			er_msg_1 = 'No data found for the city "' + city + '".'
			er_msg_2 = 'Please try again.'
			error = True
			return render(request, 'home.html', {'api' : api, 'error' : error,
				'status' : status, 'status_color' : status_color, 'er_msg_1' : er_msg_1,
				'er_msg_2' : er_msg_2,})


		return render(request, 'home.html', {'api' : api, 'error' : error,
		'status' : status, 'status_color' : status_color, })

	else:

		error = False

		try:
			request_api = requests.get('http://api.waqi.info/feed/shiraz/?token=e6089546a3dc14e1fe3d717777e9c7df3e7e5f99')
			api = json.loads(request_api.content)
		except Exception as e:
			api = e
			error = True


		if api['data']['aqi'] < 51:
			status = 'Good'
			status_color = 'good'
		elif api['data']['aqi'] < 101:
			status = 'Moderate'
			status_color = 'moderate'
		elif api['data']['aqi'] < 151:
			status = 'Unhealthy for Sensitive Groups'
			status_color = 'usg'
		elif api['data']['aqi'] < 201:
			status = 'Unhealthy'
			status_color = 'unhealthy'
		elif api['data']['aqi'] < 301:
			status = 'Very Unhealthy'
			status_color = 'veryunhealty'
		else:
			status = 'Hazardous'
			status_color = 'hazardous'

		return render(request, 'home.html', {'api' : api, 'error' : error,
			'status' : status, 'status_color' : status_color,})


def about(request):
	return render(request, 'about.html', {})