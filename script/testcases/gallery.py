#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class GalleryTest(unittest.TestCase):
	def setUp(self):
		u.setUp()
		# Launch camera
		d.start_activity(component='com.android.gallery3d/.app.Gallery')
		assert d(packageName = 'com.android.gallery3d').wait.exists(timeout = 5000),'Launch gallery failed in 5s!'

	def tearDown(self):
		u.tearDown()

	def testCheckPics(self):
		# select 'All album'
		d.click(810,1820)
		d.sleep(1)
		# get into image folder
		d.click('image.png')
		# select first image
		d.click(140,380)
		for i in range(500):
			d(resourceId = 'com.android.gallery3d:id/gl_root_view').swipe.left()
			d.sleep(0.5)
		for i in range(500):
			d(resourceId = 'com.android.gallery3d:id/gl_root_view').swipe.right()
			d.sleep(0.5)
		d.press('back')
		d.press('back')
		
	def testPlayVideo(self):
		# select 'All album'
		d.click(810,1820)
		d.sleep(1)
		# get into video folder
		d.click('video.png')
		# select video
		d.click(140,380)
		d.sleep(1)
		for i in range(200):
		#click play icon
			d.click(550,970)
			if d(text = '继续播放视频').wait.exists(timeout = 3000):
				d(text = '重新开始').click.wait()
			d.sleep(10)
			#rotate screen
			d(className="android.widget.LinearLayout").gesture((50, 770), (1000, 1460)).to((1000, 770), (50, 1460),30)
			d.sleep(10)
			d(className="android.widget.LinearLayout").gesture((610, 340), (1550, 1000)).to((610, 1000), (1550, 340),30)
			d.sleep(10)
			d.press('back')