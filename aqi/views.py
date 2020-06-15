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
				description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
			elif api['data']['aqi'] < 101:
				status = 'Moderate'
				status_color = 'moderate'
				description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
			elif api['data']['aqi'] < 151:
				status = 'Unhealthy for Sensitive Groups'
				status_color = 'usg'
				description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
			elif api['data']['aqi'] < 201:
				status = 'Unhealthy'
				status_color = 'unhealthy'
				description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
			elif api['data']['aqi'] < 301:
				status = 'Very Unhealthy'
				status_color = 'veryunhealty'
				description = 'Health alert: The risk of health effects is increased for everyone.'
			else:
				status = 'Hazardous'
				status_color = 'hazardous'
				description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
		except Exception as e:
			er_msg_1 = 'No data found for the city "' + city + '".'
			er_msg_2 = 'Please try again.'
			error = True
			return render(request, 'home.html', {'api' : api, 'error' : error,
				'status' : status, 'status_color' : status_color, 'er_msg_1' : er_msg_1,
				'er_msg_2' : er_msg_2,})


		return render(request, 'home.html', {'api' : api, 'error' : error,
		'status' : status, 'status_color' : status_color, 'description' : description, })

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
			description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
		elif api['data']['aqi'] < 101:
			status = 'Moderate'
			status_color = 'moderate'
			description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
		elif api['data']['aqi'] < 151:
			status = 'Unhealthy for Sensitive Groups'
			status_color = 'usg'
			description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
		elif api['data']['aqi'] < 201:
			status = 'Unhealthy'
			status_color = 'unhealthy'
			description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
		elif api['data']['aqi'] < 301:
			status = 'Very Unhealthy'
			status_color = 'veryunhealty'
			description = 'Health alert: The risk of health effects is increased for everyone.'
		else:
			status = 'Hazardous'
			status_color = 'hazardous'
			description = 'Health warning of emergency conditions: everyone is more likely to be affected.'

		return render(request, 'home.html', {'api' : api, 'error' : error,
			'status' : status, 'status_color' : status_color, 'description' : description, })


def about(request):
	return render(request, 'about.html', {})