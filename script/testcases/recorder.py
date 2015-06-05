#! /usr/bin/env python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import util as u

class RecorderTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()
		commands.getoutput('adb shell rm -r /sdcard/smartisan/Recorder/*')

	def testRecord200Audio(self):
		d.start_activity(component='com.smartisanos.recorder/.activity.EmptyActivity')
		d.click(880,1545)
		assert d(text = '录音机').wait.exists(timeout = 5000),'Launch sound recorder failed in 5s!'

		for i in range(200):
			d(resourceId = 'com.smartisanos.recorder:id/recorder_main_control_record').click.wait()
			d.sleep(5)
			d(resourceId = 'com.smartisanos.recorder:id/recorder_main_control_stop').click.wait()
			d(text = '命名并保存').wait.exists(timeout = 10000)
			d(text = '确定').click.wait()

	def testRecord30minAudio(self):
		d.start_activity(component='com.smartisanos.recorder/.activity.EmptyActivity')
		d.click(880,1545)
		assert d(text = '录音机').wait.exists(timeout = 5000),'Launch sound recorder failed in 5s!'

		d(resourceId = 'com.smartisanos.recorder:id/recorder_main_control_record').click.wait()

		#Record time
		d.sleep(1800)
		d(resourceId = 'com.smartisanos.recorder:id/recorder_main_control_stop').click.wait()
		d(text = '命名并保存').wait.exists(timeout = 10000)
		d(text = '确定').click.wait()