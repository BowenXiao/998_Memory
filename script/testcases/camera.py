#! /usr/bin/env python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class CameraTest(unittest.TestCase):
	def setUp(self):
		u.setUp()
		# Launch camera
		d.start_activity(component='com.android.camera2/com.android.camera.CameraLauncher')
		assert d(resourceId = 'com.android.camera2:id/shutter_button').wait.exists(timeout = 5000),'Launch camera failed in 5s!'

	def tearDown(self):
		u.tearDown()
		commands.getoutput('adb shell rm -r /sdcard/DCIM/Camera/*')

	def testTake2000Pictures(self):
		# get pics count
		before = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep jpg | wc -l')
		mode_list = ['rear','front']
		for i in range(2000):
			mode = random.choice(mode_list)
			self._switchCameraMode(mode)
			d(resourceId = 'com.android.camera2:id/shutter_button').click.wait()
			d.sleep(2)
		after = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep jpg | wc -l')
		result = string.atoi(after) - string.atoi(before)
		assert result == 2000,'Picture number is not 2000!'
			# clear pics
			# commands.getoutput('adb shell rm /sdcard/DCIM/Camera/*.jpg')

	def testRecordLongTimeVideo(self):
		# count video number
		before = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep mp4 | wc -l')
		# Start record
		d(resourceId = 'com.android.camera2:id/mode_video_hammer').click()
		assert d(resourceId = 'com.android.camera2:id/recording_time').wait.exists(timeout = 5000),'Start recording failed in 5s!'

		#Keep recording 30min
		d.sleep(1800)
		assert d(textStartsWith = '30:').wait.exists(timeout = 5000),'Camera stop recording before 30min!'

		#Stop record
		d(resourceId = 'com.android.camera2:id/mode_video_hammer').click()
		assert d(resourceId = 'com.android.camera2:id/ctrl_btn').wait.exists(timeout = 5000),'Stop recording failed in 5s!'

		# count video number
		after = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep mp4 | wc -l')
		
		# confirm recorded video exists
		after = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep mp4 | wc -l')
		result = string.atoi(after) - string.atoi(before)
		assert result == 1,'Recorded video is not in sdcard!'
		# clear video
		# commands.getoutput('adb shell rm /sdcard/DCIM/Camera/*.mp4')

	def testRecord200Video(self):
		# count video number
		before = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep mp4 | wc -l')
		for i in range(200):
			# Start record
			d(resourceId = 'com.android.camera2:id/mode_video_hammer').click()
			assert d(resourceId = 'com.android.camera2:id/recording_time').wait.exists(timeout = 5000),'Start recording failed in 5s!'

			#Keep recording 10s
			d.sleep(10)
			assert d(textStartsWith = '00:1').wait.exists(timeout = 5000),'Camera stop recording before 10min!'

			#Stop record
			d(resourceId = 'com.android.camera2:id/mode_video_hammer').click()
			assert d(resourceId = 'com.android.camera2:id/ctrl_btn').wait.exists(timeout = 5000),'Stop recording failed in 5s!'
			
			# record video interval
			d.sleep(5)
		# confirm recorded video exists
		after = commands.getoutput('adb shell ls /sdcard/DCIM/Camera/* | grep mp4 | wc -l')
		result = string.atoi(after) - string.atoi(before)
		assert result == 200,'Recorded video number is not 200!'
			# clear video
			# commands.getoutput('adb shell rm /sdcard/DCIM/Camera/*.mp4')


	def _switchCameraMode(self,mode):
		current_mode = self._getCameraMode()
		if current_mode == mode:
			pass
		else:
			d(resourceId = 'com.android.camera2:id/camera_switcher_btn').click.wait()

	def _getCameraMode(self):
		if d(resourceId = 'com.android.camera2:id/flip_btn').wait.exists(timeout = 5000):
			return 'rear'
		elif d(resourceId = 'com.android.camera2:id/flash_btn').wait.exists(timeout = 5000):
			return 'front'