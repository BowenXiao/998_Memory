#! /usr/bin/env python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import util as u
# Send Item
SMS_MAX_CONTENT = 'AutoTestContentAutoTestContentAutoTestContentAutoTestContentAutoTestContentAutoTestContentAutoTestContentAutoTestContentAutoTestContentAutoTestContent'
MMS_RECEIVER	= '15650790637'
MMS_VIDEO_CONT	= 'Test MMS With Video'
MMS_PICS_CONT	= 'Test MMS With PICS'

#Read Item
SMS_SENDER_INSERT			= '\"156 1234 9876\"'
SMS_CONT_INSERT				= '\"Test SMS\"'
SMS_SENDER					= '156 1234 9876'
SMS_CONT					= 'Test SMS'
MMS_PICS_SENDER 			= '150 0845 5658'
MMS_VIDEO_SENDER 			= '151 0845 5658'
MMS_PICS_SENDER_INSERT 		= '\"150 0845 5658\"'
MMS_VIDEO_SENDER_INSERT		= '\"151 0845 5658\"'
MMS_VIDEO_CONT_INSERT		= '\"Test MMS With Video\"'
MMS_PICS_CONT_INSERT		= '\"Test MMS With PICS\"'

class MessageTest(unittest.TestCase):
	def setUp(self):
		u.setUp()

	def tearDown(self):
		u.tearDown()

	def testMessageAttachCamera(self):
		#Launch message app and enter new message screen
		self._launchAndEnterNewMsg()

		#Input receiver and content
		self._editTestContent(u.getNumber(),SMS_MAX_CONTENT)
		d(resourceId = 'com.android.mms:id/switch_button').click.wait()
		for i in range(1000):
			d.click(100,1850)
			assert d(text = '请选择操作').wait.exists(timeout=5000),'Action does not pop-up in 5s!'
			d(text = '拍摄照片').click.wait()
			assert d(packageName = 'com.android.camera2').wait.exists(timeout = 5000),'Switch to camera failed in 5s!'
			d(resourceId = 'com.android.camera2:id/shutter_button').click.wait()
			assert d(resourceId = 'com.android.camera2:id/btn_done').wait.exists(timeout = 5000),'Take picture failed in 5s!'
			d(resourceId = 'com.android.camera2:id/btn_cancel').click.wait()

	def _launchAndEnterNewMsg(self):
		#Start message
		d.start_activity(component='com.android.mms/.ui.ConversationList')
		if  d(text = '短信',resourceId = 'com.android.mms:id/button_left').exists:
			d(text = '短信',resourceId = 'com.android.mms:id/button_left').click.wait()
		if  d(text = '返回').exists:
			d(text = '返回').click.wait()
		if  d(resourceId = 'com.android.mms:id/creat_new_message').wait.exists(timeout=1000):
			d(resourceId = 'com.android.mms:id/creat_new_message').click.wait()
		assert d(description='发送').wait.exists(timeout=5000), 'Can not switch to new message screen. '



	def _editTestContent(self,receiver,content):
		#Input receiver and text content
		d(resourceId = 'com.android.mms:id/recipients_edittext',text = '接收者').set_text(receiver)
		d(resourceId = 'com.android.mms:id/embedded_text_editor',text = '键入短信').set_text(content)

	def _sendMessage(self):
		#Send Message
		d(description = '发送').click.wait()
		d(text = '准备发送…').wait.exists(timeout = 5000)
		d(text = '准备发送…').wait.gone(timeout = 10000)
		d.sleep(1)
		d(text="发送中…").wait.gone(timeout=60000), 'Send SMS failed in 60s'

	def _insertSMS(self,name,content):
		'''
		@param method:  add or clear
		@param content: phone number
		@param count:   call number
		'''
		commands.getoutput('adb shell am startservice -a smartisan.datahelper.InitData --es type "Sms" --es name %s --es content %s'%(name,content))

	def _insertMMS(self,atttype,name,content):
		'''
		@param method:  add or clear
		@param content: phone number
		@param count:   call number
		'''
		commands.getoutput('adb shell am startservice -a smartisan.datahelper.InitData --es type %s --es method "add" --es name %s --es content %s'%(atttype,name,content))