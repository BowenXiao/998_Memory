#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

class TelephonyTest(unittest.TestCase):
	def setUp(self):
		u.setUp()
		#Launch telephony
		d.start_activity(component='com.android.contacts/.activities.DialtactsActivity')
		assert d(text = '拨号').wait.exists(timeout = 5000),'Launch settings failed in 5s!'

	def tearDown(self):
		u.tearDown()

	def testCreate1000Contact(self):
		# switch to contact view
		d(text = '联系人').click.wait()
		assert d(text = '群组').wait.exists(timeout = 5000), 'Switch to contact view failed in 5s!'
		d(text = '全部').click.wait()
		assert d(resourceId = 'com.android.contacts:id/btn_sort').wait.exists(timeout = 5000),'Switch all contact failed in 5s!'
		for i in range(1000):
			d(text = '添加').click.wait()
			if d(text = '本地保存').exists:
				d(text = '本地保存').click.wait()
			d(text = '姓名').set_text('Contact%d'%i)
			# click the top of screen, prevent the duplication
			d.click(580,170)
			d(text = '公司').set_text('Compony%d'%i)
			tel = random.randint(15000000000,15999999999)
			d(text = '电话',className = 'android.widget.EditText').set_text('%d'%tel)
			# set portrait
			d(description = '联系人照片').click.wait()
			d(text = '从相册中选择照片').click.wait()
			d.sleep(1)
			d.click('album.png')
			d.click('root_dir.png')
			d.click('pic.png')
			d.click('done.png')
#			d.click(900,1825)
#			d.sleep(1)
#			d.click(420,400)
#			d.sleep(1)
#			d.click('image.png')
#			# select first image in the folder
#			d.click(980,150)
#			d.sleep(1)
			d(text = '确定').click.wait()
			d(text = '完成').click.wait()
			assert d(text = '联系人详情').wait.exists(timeout = 10000),'Switch to contact detail failed in 5s!'
			d(text = '返回').click.wait()
