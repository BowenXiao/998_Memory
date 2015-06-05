#! /usr/bin/env python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import util as u

class WeatherTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testAdd20City(self):
		city_list = ['北京','上海','广州','深圳','成都','武汉','南京','杭州','天津','重庆','西安','苏州','厦门','福州','宁波','沈阳','长春','大连','郑州','长沙']
		d.start_activity(component = 'com.smartisanos.weather/.CityWeather')
		assert d(resourceId = 'com.smartisanos.weather:id/textview_cityname').wait.exists(timeout = 5000),'Launch Weather failed in 5s!'

		for city in city_list:
			d(resourceId = 'com.smartisanos.weather:id/imagebutton_add').click.wait()
			u.selectOption(city)

	def testDel20City(self):
		city_list = ['北京','上海','广州','深圳','成都','武汉','南京','杭州','天津','重庆','西安','苏州','厦门','福州','宁波','沈阳','长春','大连','郑州','长沙']
		d.start_activity(component = 'com.smartisanos.weather/.CityWeather')

		for city in city_list:
			if not d(resourceId = 'com.smartisanos.weather:id/imagebutton_minus').wait.exists(timeout = 5000):
				d(resourceId = 'com.smartisanos.weather:id/viewpager_mian').swipe.left()
			assert d(resourceId = 'com.smartisanos.weather:id/textview_cityname').wait.exists(timeout = 5000),'No added city in current view!'
			if d(resourceId = 'com.smartisanos.weather:id/imagebutton_minus').wait.exists(timeout = 5000):
				d(resourceId = 'com.smartisanos.weather:id/imagebutton_minus').click.wait()
				d(text = '删除城市').click.wait()
			