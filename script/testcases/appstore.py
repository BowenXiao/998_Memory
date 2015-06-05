#! /usr/bin/env python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class AppstoreTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testSwitchView(self):
		#Launch camera
		d.start_activity(component = 'com.smartisanos.appstore/.AppStoreActivity')
		assert d(resourceId = 'com.smartisanos.appstore:id/main_header').wait.exists(timeout = 5000), 'Launch appstore failed in 5s!'

		view_list = ['推荐','榜单','分类','搜索','应用管理']
		for i in range(500):
			view = random.choice(view_list)
			d(text = view).click()