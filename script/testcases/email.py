#! /usr/bin/env python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

ACCOUNT = 'stabilitymailpost@smartisan.com'
PASSWORD = 'Smartisantest011'
SEND_TO = 'stabilitymailget@smartisan.com'
#SEND_TO = 'smartisanauto@hotmail.com'
SUBJECT = 'Test Send Email'
ATT_SUBJECT = 'Send With Attachment'
NOATT_SUBJECT = 'Send Without Attachment'
BODY = 'This mail is send by autotest'

class EmailTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testSendEmail(self):
		#Launch Email
		self._launchEmail()

		#Edit mail content and then send out
		for i in range(500):
			d(resourceId = 'com.android.email:id/compsoe_view').click.wait()
			# edit receiver
			d(resourceId = 'com.android.email:id/to_recipient_view').set_text(SEND_TO)
			d.press('enter')
			# edit cc
			#d(resourceId = 'com.android.email:id/compose_thumbnail').click.wait()
			#d(resourceId = 'com.android.email:id/cc_recipient_view').set_text(CC_TO)
			# edit mail content
			d(resourceId = 'com.android.email:id/subject').set_text(SUBJECT)
			d(resourceId = 'com.android.email:id/body').set_text(BODY)
			# add attachment
			d(resourceId = 'com.android.email:id/compose_attach').click.wait()
			d(text = 'ES文件浏览器').click.wait()
			u.selectOption('JPG_640x480_8bit_standart.jpg')
			d(text = '发送').click.wait()
			d.sleep(3)

	def testReadEmail(self):
		#Launch Email
		self._launchEmail()

		#Get into send box
		d(resourceId = 'com.android.email:id/options_view').click.wait()
		d(text = '已加旗标').click.wait()
		for i in range(1000):
			d(resourceId = 'com.android.email:id/refresh_view').click.wait()
			# check received mail
			d(descriptionContains = ATT_SUBJECT).click()
			assert d(resourceId = 'com.android.email:id/send_calendar_btn').wait.exists(timeout = 5000),'Switch to mail detail failed in 5s!'
			# check attachment
			if  d(text = '加载').exists:
				d(text = '加载').click.wait()
			d(text = '打开').click.wait()
			if d(text = '联网提示').wait.exists(timeout = 5000):
				d(text = '确定').click.wait()
			d.press('back')
			d.sleep(1)
			d.press('back')
			d.sleep(1)

	def _launchEmail(self):
		#Launch Email
		d.start_activity(component='com.android.email/.activity.Welcome')
		#Check if login account is needed.
		if d(text = '添加账户').wait.exists(timeout = 5000):
			self._loginAccount()
		else:
			pass
		assert d(resourceId = 'com.android.email:id/subtitle',text = 'Exchange').wait.exists(timeout = 10000),'Launch email failed in 10s!'

	def _loginAccount(self):
		# select exchage
		d(resourceId = 'com.android.email:id/perset_exchange').click.wait()
		d(resourceId = 'com.android.email:id/account_email').set_text(ACCOUNT)
		d(resourceId = 'com.android.email:id/account_password').set_text(PASSWORD)
		d(text = '下一步').click.wait()
		if d(text = '远程安全管理').wait.exists(timeout = 20000):
			d(text = '确定').click.wait()
			if d(text = '要激活设备管理器吗？').wait.exists(timeout = 5000):
				d(text = '激活').click.wait()
		d(resourceId = 'com.android.email:id/subtitle',text = 'Exchange').wait.exists(timeout = 120000)

	def _selectOption(self,option):
		i = 1
		while i:
			if d(text = option).exists:
				break
			d.swipe(540,1400,540,400,100)
			d.sleep(1)
			i+=1
			if d(text = option).exists or i==10:
				break
		d.sleep(1)
		d(text = option).click.wait()

	def _clearAccount(self):
		commands.getoutput('adb shell am start -n com.android.settings/.Settings')
		self._selectOption('高级设置')
		self._selectOption('账户和同步')
		if d(text = 'Exchange').exists:
			d(text = 'Exchange').click.wait()
			d(text = '账户设置').click.wait()
			d(text = 'Exchange').click.wait()
			d(text = '删除此账户').click.wait()
			d(text = '确认删除').click.wait()
		else:
			pass