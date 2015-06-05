#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class ClockTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testSwitchView(self):
		#Launch clock
		d.start_activity(component='com.smartisanos.clock/.activity.ClockActivity')
		if d(textContains = '时钟需要获取定位数据').wait.exists(timeout=3000):
			d(text = '同意').click.wait()
		if d(text = '提醒').exists:
			d(text = '同意').click.wait()
		assert d(text = '闹钟').wait.exists(timeout=5000),'Launch clock failed in 5s!'
		
		view_list = ['世界时钟','闹钟','秒表','计时器']
		for i in range(500):
			view = random.choice(view_list)
			d(text = view).click()