#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

TOP5 = ['www.baidu.com','www.taobao.com','www.163.com','www.qq.com','www.youku.com']

class BrowserTest(unittest.TestCase):
	def setUp(self):
		u.setUp()
		d.start_activity(component='com.android.browser/.BrowserActivity')
		assert d(resourceId = 'com.android.browser:id/switch_btn').wait.exists(timeout=5000),'Launch browser failed in 5s!'

	def tearDown(self):
		u.tearDown()

	def testVisitWebpage1000(self):
		if d(resourceId = 'com.android.browser:id/stop').exists:
			d(resourceId = 'com.android.browser:id/newtab_btn').click.wait()
		for i in range(1000):
			url = random.choice(TOP5)
			d(text = '输入网址').set_text(url)
			d.press('enter')
			d.sleep(3)
			# random swipe position
			#sx = random.randint(30,1060)
			#sy = random.randint(210,1630)
			#ex = random.randint(30,1060)
			#ey = random.randint(210,1630)
			#step = random.randint(10,50)
			#d.swipe(sx, sy, ex, ey,step)
			#d.sleep(2)
			d(resourceId = 'com.android.browser:id/newtab_btn').click.wait()

	def testSwitchThumbs(self):
		if d(resourceId = 'com.android.browser:id/stop').exists:
			d(resourceId = 'com.android.browser:id/newtab_btn').click.wait()
		if d(resourceId = 'com.android.browser:id/frame0').exists:
			d(resourceId = 'com.android.browser:id/switch_btn').click.wait()
		for i in range(1000):
			d(resourceId = 'com.android.browser:id/switch_btn').click()
			assert d(resourceId = 'com.android.browser:id/main_content').wait.exists(timeout = 5000),'Switch to thumbs view failed in 5s!'
			num = random.randint(0,1)
			thumbs_list = ['com.android.browser:id/frame0','com.android.browser:id/frame1','com.android.browser:id/frame2','com.android.browser:id/frame3']
			thumbs = random.choice(thumbs_list)
			if num == 0:
				d(description = '标签页管理').swipe.right()
			else:
				d(description = '标签页管理').swipe.left()
			d(resourceId = thumbs).click()
			d.sleep(1)

	def testSwitchView(self):
		if d(resourceId = 'com.android.browser:id/stop').exists:
			d(resourceId = 'com.android.browser:id/newtab_btn').click.wait()
		if d(resourceId = 'com.android.browser:id/frame0').exists:
			d(resourceId = 'com.android.browser:id/switch_btn').click.wait()
		for i in range(1000):
			d(resourceId = 'com.android.browser:id/menu_btn').click.wait()
			d.click('hiden_mode.png')
			d.sleep(1)
			d(resourceId = 'com.android.browser:id/menu_btn').click.wait()
			d.click('normal_mode.png')

