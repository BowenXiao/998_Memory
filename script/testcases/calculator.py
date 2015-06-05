#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

SIMPLE_KEYS = ['com.smartisanos.calculator:id/mc','com.smartisanos.calculator:id/madd','com.smartisanos.calculator:id/mminus','com.smartisanos.calculator:id/mr','com.smartisanos.calculator:id/neg','com.smartisanos.calculator:id/div','com.smartisanos.calculator:id/digit7','com.smartisanos.calculator:id/digit8','com.smartisanos.calculator:id/digit9','com.smartisanos.calculator:id/minus','com.smartisanos.calculator:id/digit4','com.smartisanos.calculator:id/digit5','com.smartisanos.calculator:id/digit6','com.smartisanos.calculator:id/add','com.smartisanos.calculator:id/digit1','com.smartisanos.calculator:id/digit2','com.smartisanos.calculator:id/digit3','com.smartisanos.calculator:id/digit0','com.smartisanos.calculator:id/dot','com.smartisanos.calculator:id/equal']
SCIENCE_KEYS = SIMPLE_KEYS + ['com.smartisanos.calculator:id/leftparen','com.smartisanos.calculator:id/rightparen','com.smartisanos.calculator:id/mod','com.smartisanos.calculator:id/reci','com.smartisanos.calculator:id/x2','com.smartisanos.calculator:id/x3','com.smartisanos.calculator:id/yx','com.smartisanos.calculator:id/fac','com.smartisanos.calculator:id/sqrt','com.smartisanos.calculator:id/x_sqrt_y','com.smartisanos.calculator:id/log','com.smartisanos.calculator:id/sin','com.smartisanos.calculator:id/cos','com.smartisanos.calculator:id/tan','com.smartisanos.calculator:id/ln','com.smartisanos.calculator:id/sinh','com.smartisanos.calculator:id/cosh','com.smartisanos.calculator:id/tanh','com.smartisanos.calculator:id/ex','com.smartisanos.calculator:id/pi','com.smartisanos.calculator:id/ee','com.smartisanos.calculator:id/rand']

class CalculatorTest(unittest.TestCase):
	def setUp(self):
		u.setUp()
		# Launch calculator
		d.start_activity(component='com.smartisanos.calculator/.Calculator')
		assert d(resourceId = 'com.smartisanos.calculator:id/show').wait.exists(timeout=5000),'Launch calculator failed in 5s!'

	def tearDown(self):
		u.tearDown()

	def testCalculatorClickAndRotated(self):
		for i in range(25):
			if d(resourceId = 'com.smartisanos.calculator:id/second').wait.exists(timeout = 3000):
				mode = 'science'
			else:
				mode = 'simple'
			if mode == 'simple':
				for i in range(10):
					key = random.choice(SIMPLE_KEYS)
					d(resourceId = key).click()
				# switch to science mode
				d(className="android.widget.LinearLayout").gesture((50, 770), (1000, 1460)).to((1000, 770), (50, 1460),30)
				if d(text = '提示').exists:
					d(resourceId = 'smartisanos:id/btn_close').click.wait()
			elif mode == 'science':
				for i in range(10):
					key = random.choice(SCIENCE_KEYS)
					d(resourceId = key).click()
				# switch to simple mode
				d(className="android.widget.LinearLayout").gesture((610, 340), (1550, 1000)).to((610, 1000), (1550, 340),30)
				if d(text = '提示').exists:
					d(resourceId = 'smartisanos:id/btn_close').click.wait()