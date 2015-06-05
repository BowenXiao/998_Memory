#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class CalanderTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testCreatEvent(self):
		#Launch calander
		d.start_activity(component='com.android.calendar/.AllInOneActivity')
		d(text = '月').click.wait()
		assert d(text='今天').wait.exists(timeout = 5000),'Launch calendar failed in 5s!'

		for i in range(1000):
			#Create event and edit event title and address
			d(text = '新建').click.wait()
			if  d(text = '请选择将任务保存至').exists:
				d(text = '本地账户').click.wait()
			assert d(resourceId = 'com.android.calendar:id/calendar_name').wait.exists(timeout = 5000),'Switch to create event view failed in 5s!'
			d(text = '任务标题').set_text('Test Event')
			if  d(text = '更多选项').exists:
				d(text = '更多选项').click.wait()
			assert d(text = '地点').wait.exists(timeout=5000),'Switch detil edit view failed in 5s!'
			d(text = '地点').set_text('Motolora')
			d(text = '完成').click.wait()
			assert d(resourceId = "com.android.calendar:id/agenda_content").wait.exists(timeout=5000),'Event does not show on the screen in 5s!'

	def testDelEvent(self):
		#Launch calander
		d.start_activity(component='com.android.calendar/.AllInOneActivity')
		assert d(text='今天').wait.exists(timeout = 5000),'Launch calendar failed in 5s!'

		#d(resourceId = 'com.android.calendar:id/button_agenda').click.wait()
		#assert d(text = '未完成').wait.exists(timeout = 5000),'Switch to Events view failed in 5s!'

		i = 0
		while d(resourceId = 'com.android.calendar:id/agenda_content').wait.exists(timeout = 3000):
			if i == 10:
				break
			d(resourceId = 'com.android.calendar:id/agenda_content').swipe.right(steps = 5)
			d(resourceId = 'com.android.calendar:id/delete_icon').click.wait()
			i += 1

	def testSwitchView(self):
		#Launch calander
		d.start_activity(component='com.android.calendar/.AllInOneActivity')
		assert d(text='今天').wait.exists(timeout = 5000),'Launch calendar failed in 5s!'

		view_list = ['日','周','月']
		for i in range(500):
			view = random.choice(view_list)
			d(text = view).click()