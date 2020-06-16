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
				description = 'كیفیت هوا رضایت بخش است و آلودگی هوا خطری كم یا خطر ندارد.'
			elif api['data']['aqi'] < 101:
				status = 'Moderate'
				status_color = 'moderate'
				description = 'کیفیت هوا قابل قبول است. با این حال ، ممکن است برای برخی از افراد به ویژه افرادی که به طور غیرمعمول نسبت به آلودگی هوا حساس هستند ، خطر ایجاد کند.'
			elif api['data']['aqi'] < 151:
				status = 'Unhealthy for Sensitive Groups'
				status_color = 'usg'
				description = 'ممکن است بر سلامتی اعضای گروههای حساس اثر بگذارد. عموم مردم کمتر تحت تأثیر قرار می گیرند.'
			elif api['data']['aqi'] < 201:
				status = 'Unhealthy'
				status_color = 'unhealthy'
				description = 'برخی از افراد عمومی ممکن است اثرات آلودگی هوا را بر سلامتی خود تجربه کنند. اعضای گروههای حساس ممکن است اثرات جدی تری را تجربه کنند.'
			elif api['data']['aqi'] < 301:
				status = 'Very Unhealthy'
				status_color = 'veryunhealty'
				description = 'هشدار سلامتی: خطر تأثیرات آلودگی هوا بر سلامتی، برای همه افزایش یافته است.'
			else:
				status = 'Hazardous'
				status_color = 'hazardous'
				description = 'هشدار بهداشتی در مورد شرایط اضطراری: همه به احتمال زیاد تحت تأثیر قرار می گیرند.'
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
			description = 'كیفیت هوا رضایت بخش است و آلودگی هوا خطری كم یا خطر ندارد.'
		elif api['data']['aqi'] < 101:
			status = 'Moderate'
			status_color = 'moderate'
			description = 'کیفیت هوا قابل قبول است. با این حال ، ممکن است برای برخی از افراد به ویژه افرادی که به طور غیرمعمول نسبت به آلودگی هوا حساس هستند ، خطر ایجاد کند.'
		elif api['data']['aqi'] < 151:
			status = 'Unhealthy for Sensitive Groups'
			status_color = 'usg'
			description = 'ممکن است بر سلامتی اعضای گروههای حساس اثر بگذارد. عموم مردم کمتر تحت تأثیر قرار می گیرند.'
		elif api['data']['aqi'] < 201:
			status = 'Unhealthy'
			status_color = 'unhealthy'
			description = 'برخی از افراد عمومی ممکن است اثرات آلودگی هوا را بر سلامتی خود تجربه کنند. اعضای گروههای حساس ممکن است اثرات جدی تری را تجربه کنند.'
		elif api['data']['aqi'] < 301:
			status = 'Very Unhealthy'
			status_color = 'veryunhealty'
			description = 'هشدار سلامتی: خطر تأثیرات آلودگی هوا بر سلامتی، برای همه افزایش یافته است.'
		else:
			status = 'Hazardous'
			status_color = 'hazardous'
			description = 'هشدار بهداشتی در مورد شرایط اضطراری: همه به احتمال زیاد تحت تأثیر قرار می گیرند.'

		return render(request, 'home.html', {'api' : api, 'error' : error,
			'status' : status, 'status_color' : status_color, 'description' : description, })


def about(request):
	return render(request, 'about.html', {})