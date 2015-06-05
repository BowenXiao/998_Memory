#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import random
import util as u

# screen display resolution
RESOLUTION_X = d.info['displayWidth']
RESOLUTION_Y = d.info['displayHeight']

VIEW_MODE = {'36':'三十六宫格',
			'81':'八十一宫格',
			'16':'十六宫格',
			'default':'安卓原生'}

THEME_LIST = ['经典','蓝色','褐色','青色','木纹','浅灰','橙色','紫色','灰岩']

class LauncherTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testSingleViewSwipe(self):
		# swipe home screen 1000 times totally
		for i in range(500):
			direction = random.choice(['left','right'])
			step = random.randint(5,50)
			self._swipeScreen(direction,step)
			d.sleep(1)

	def testLauncherMultiViewDrag(self):
		# press menu to enter multi view
		d.press('menu')
		d.sleep(1)
		for i in range(500):
			# random select drag range
			range_X = range(30,1060)
			range_Y = range(210,1630)
			sx = random.choice(range_X)
			sy = random.choice(range_Y)
			ex = random.choice(range_X)
			ey = random.choice(range_Y)
			step = random.randint(10,50)
			d.drag(sx, sy, ex, ey,step)
			d.sleep(1)
		
#	def testSwitch81View(self):
#		self._switchLauncherSettings('81')
#		d.press('back')
#		d.press('back')
#		d.press('menu')
#		for i in range(10):
#			direction = random.choice(['left','right'])
#			step = random.randint(5,50)
#			self._swipeScreen(direction,step)

#		for i in range(2):
#			d.press('menu')
#			d.sleep(1)

	def testSwitch16View(self):
		self._switchLauncherSettings('16')
		d.press('back')
		d.press('back')
		d.press('home')
		d.press('menu')
		for i in range(500):
			direction = random.choice(['left','right'])
			step = random.randint(5,50)
			self._swipeScreen(direction,step)

		for i in range(2):
			d.press('menu')
			d.sleep(1)

	def testSwitch64View(self):
		self._switchLauncherSettings('16')
		d.press('back')
		d.press('back')
		d.press('home')
		d.press('menu')
		for i in range(500):
			direction = random.choice(['left','right'])
			step = random.randint(5,50)
			self._swipeScreen(direction,step)

		for i in range(2):
			d.press('menu')
			d.sleep(1)

#	def testSwitch36View(self):
#		self._switchLauncherSettings('36')
#		d.press('back')
#		d.press('back')
#		d.press('menu')
#		for i in range(10):
#			direction = random.choice(['left','right'])
#			step = random.randint(5,50)
#			self._swipeScreen(direction,step)

#		for i in range(2):
#			d.press('menu')
#			d.sleep(1)

	def testSwitchLanguage(self):
		#language_dir = {'English':'Language',
		#				'中文 (简体)':'语言',
		#				'中文 (繁體)':'語言'
		#				}
		d.start_activity(component='com.android.settings/.Settings')
		assert d(text = '设置').wait.exists(timeout = 5000),'Launch settings failed in 5s!'

		u.selectOption('语言和键盘')
		assert d(text = '语言').wait.exists(timeout = 5000),'Switch to language setting failed in 5s!'
		for i in range(50):
			d(text = '语言').click.wait()
			assert d(resourceId = 'smartisanos:id/tv_title',text = '语言').wait.exists(timeout = 5000),'Get into language setting failed in 5s!'
			# switch to traditional chinese
			d(text = '中文 (繁體)').click.wait()
			assert d(text = '語言').wait.exists(timeout = 5000),'Switch to Traditional Chinese failed in 5s!'
			d(text = '語言').click.wait()
			assert d(resourceId = 'smartisanos:id/tv_title',text = '語言').wait.exists(timeout = 5000),'Get into language setting failed in 5s!'
			# switch to english
			d(text = 'English').click.wait()
			assert d(text = 'Language').wait.exists(timeout = 5000),'Switch to English failed in 5s!'
			d(text = 'Language').click.wait()
			assert d(resourceId = 'smartisanos:id/tv_title',text = 'Language').wait.exists(timeout = 5000),'Get into language setting failed in 5s!'
			# switch to simple chinese
			d(text = '中文 (简体)').click.wait()
			assert d(text = '语言').wait.exists(timeout = 5000),'Switch to English failed in 5s!'

	def testSwitchTheme(self):
		d.start_activity(component='com.android.settings/.Settings')
		assert d(text = '设置').wait.exists(timeout = 5000),'Launch settings failed in 5s!'
		u.selectOption('主题、壁纸、图标')
		assert d(resourceId = 'smartisanos:id/tv_title',text = '主题、壁纸、图标').wait.exists(timeout = 5000),'Switch to theme view failed in 5s!'
		u.selectOption('桌面主题')
		assert d(resourceId = 'com.smartisanos.launcher:id/tv_title',text = '桌面主题').wait.exists(timeout = 5000),'Switch to theme view failed in 5s!'
		for i in range(30):
			for theme in THEME_LIST:
				if i==0 and theme == '经典':
					continue
				d.start_activity(component='com.android.settings/.Settings')
				assert d(resourceId = 'com.smartisanos.launcher:id/tv_title',text = '桌面主题').wait.exists(timeout = 5000),'Switch to theme view failed in 5s!'
				if theme == '经典':
					d(resourceId = 'com.smartisanos.launcher:id/list_theme').swipe.down()
					d(resourceId = 'com.smartisanos.launcher:id/list_theme').swipe.down()
					d(resourceId = 'com.smartisanos.launcher:id/list_theme').swipe.down()
					d.sleep(1)
				u.selectOption(theme)
				assert d(resourceId = 'smartisanos:id/tv_title',text = theme).wait.exists(timeout = 5000),'Switch to theme thumbnail failed in 5s!'
				d(text = '设定').click.wait()
				assert d(text = '正在加载主题').wait.exists(timeout = 5000),'Loading theme view does not show up in 5s!'
				assert d(text = '正在加载主题').wait.gone(timeout = 10000),'Loading theme view does not disappeared in 10s!'
				assert d(resourceId = 'com.smartisanos.launcher:id/glview').wait.exists(timeout = 5000), 'Switch to launcher failed in 5s!'
				d.sleep(3)
		# exit theme setting
		d.start_activity(component='com.android.settings/.Settings')
		d.press('back')

	def _switchLauncherSettings(self,viewmode):
		# launch setting
		d.start_activity(component='com.android.settings/.Settings')
		if not d(text = '设置').wait.exists(timeout = 5000):
			d.press('back')
			d.press('back')
			d.press('home')
			d.start_activity(component='com.android.settings/.Settings')
		assert d(text = '设置').wait.exists(timeout = 5000),'Launch settings failed in 5s!'

		# get into launcher settings
		if d(text = '单板块视图').wait.exists(timeout = 5000):
			pass
		else:
			u.selectOption('桌面设置项')
			assert d(text = '单板块视图').wait.exists(timeout = 5000),'Switch to Desktop Settings failed in 5s!'
		if viewmode == '36' or viewmode == '81':
			if d(text = '多板块视图').exists:
				d(text = VIEW_MODE[viewmode]).click.wait()
				if d(text = '设置桌面').wait.exists(timeout = 5000):
					d(text = '确定').click.wait()
			else:
				d(text = '九宫格').click.wait()
				d.sleep(3)
				if d(text = '设置桌面').wait.exists(timeout = 5000):
					d(text = '确定').click.wait()
					d.sleep(3)
				d.start_activity(component='com.android.settings/.Settings')
				assert d(text = '设置').wait.exists(timeout = 5000),'Launch settings failed in 5s!'
				d(text = VIEW_MODE[viewmode]).click.wait()
				if d(text = '设置桌面').wait.exists(timeout = 5000):
					d(text = '确定').click.wait()
		else:
			d(text = VIEW_MODE[viewmode]).click.wait()
			if d(text = '设置桌面').wait.exists(timeout = 5000):
				d(text = '确定').click.wait()

	def _swipeScreen(self,direction,step=None):
		if direction == 'left':
			d(resourceId = 'com.smartisanos.launcher:id/glview').swipe.left(steps=step)
		elif direction == 'right':
			d(resourceId = 'com.smartisanos.launcher:id/glview').swipe.right(steps=step)
		else:
			raise NameError
			print 'invalid string'