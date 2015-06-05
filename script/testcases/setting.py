#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class SettingTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testTurnOnOffWifi(self):
		'''
		before running, keep wi-fi connected.
		'''
		#Launch Setting
		d.start_activity(component='com.android.settings/.Settings')
		assert d(text = '设置').wait.exists(timeout = 5000),'Launch settings failed in 5s!'

		u.selectOption('无线网络')
		assert d(resourceId = 'smartisanos:id/tv_title',text = '无线网络').wait.exists(timeout = 5000),'Switch to WIFI failed in 5s!'
		if d(text = '要查看可用网络，请打开无线网络').exists:
			print 'Current wifi status: Off'
			d(resourceId = 'com.android.settings:id/item_switch').swipe.right(steps = 5)
			d(text = '已连接').wait.exists(timeout = 15000)
		else:
			print 'Current wifi status: On'
			d(text = '已连接').wait.exists(timeout = 15000)
		for i in range(1000):
			#Turn off wifi
			d(resourceId = 'com.android.settings:id/item_switch').swipe.left(steps = 5)
			assert d(text = '要查看可用网络，请打开无线网络').wait.exists(timeout = 15000),'Turn off wifi failed in 5s!'
			#Turn on wifi
			d(resourceId = 'com.android.settings:id/item_switch').swipe.right(steps = 5)
			assert d(text = '已连接').wait.exists(timeout = 15000),'Turn on wifi failed in 5s!(UI)'
			assert self._getWifiStatus(),'Turn on wifi failed in 5s!(Dumpsys)'

	def _getWifiStatus(self):
		result = commands.getoutput("adb shell dumpsys wifi | grep 'Wi-Fi is'")
		if result.find('enable') == -1:
			# wifi disabled
			return False
			# wifi enabled
		else:
			return True

	def testTurnOnOffBT(self):
		#Launch Setting
		d.start_activity(component='com.android.settings/.Settings')
		assert d(text = '设置').wait.exists(timeout = 5000),'Launch settings failed in 5s!'

		u.selectOption('蓝牙')
		assert d(resourceId = 'smartisanos:id/tv_title',text = '蓝牙').wait.exists(timeout = 5000),'Switch to BT failed in 5s!'
		if d(text = '要查看可用蓝牙设备，请打开蓝牙功能').exists:
			print 'Current BT status: Off'
			d(resourceId = 'com.android.settings:id/item_switch').swipe.right(steps = 5)
			d(text = '范围内可配对设备').wait.exists(timeout = 5000)
		else:
			print 'Current BT status: On'
			d(text = '范围内可配对设备').wait.exists(timeout = 5000)
		for i in range(1000):
			#Turn off BT
			d(resourceId = 'com.android.settings:id/item_switch').swipe.left(steps = 5)
			assert d(text = '要查看可用蓝牙设备，请打开蓝牙功能').wait.exists(timeout = 5000),'Turn off BT failed in 5s!'
			#Turn on wifi
			d(resourceId = 'com.android.settings:id/item_switch').swipe.right(steps = 5)
			assert d(text = '范围内可配对设备').wait.exists(timeout = 5000),'Turn on BT failed in 5s!'