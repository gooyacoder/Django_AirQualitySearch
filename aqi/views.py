from django.shortcuts import render


def home(request):
	import requests
	import json

	error = False

	try:
		request_api = requests.get('http://api.waqi.info/feed/shiraz/?token=e6089546a3dc14e1fe3d717777e9c7df3e7e5f99')
		api = json.loads(request_api.content)
	except Exception as e:
		api = e
		error = True




	return render(request, 'home.html', {'api' : api, 'error' : error,})


def about(request):
	return render(request, 'about.html', {})