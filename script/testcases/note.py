#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

SHORT_TEXT = 'Test Content...'


class NoteTest(unittest.TestCase):
	def setUp(self):
		u.setUp()   

	def tearDown(self):
		u.tearDown()

	def testSharePicToNote(self):
		#Launch Note
		d.start_activity(component='com.android.gallery3d/.app.Gallery')
		if d(text = '列表').exists:
			d(text = '列表').click.wait()
		assert d(packageName = 'com.android.gallery3d').wait.exists(timeout = 5000),'Launch gallery failed in 5s!'
		# select 'All Album'
		d.click(800,1830)
		d.sleep(1)
		# select pic folder
		d.click('image.png')
		for i in range(450):
			d.click('edit.png')
			d.sleep(1)
			for i in range(4):
				d.click(150,370+280*i)
			d.click('share.png')
			d(text = '便签').click.wait()
			assert d(resourceId = 'com.smartisanos.notes:id/send_finish_button').wait.exists(timeout = 10000),'Add pic to note failed in 10s!'
			d(resourceId = 'com.smartisanos.notes:id/send_finish_button').click.wait()
			assert d(resourceId = 'com.smartisanos.notes:id/delete_insert_button').wait.exists(timeout = 5000),'Create pic note failed in 5s!'
			d(text = '返回').click.wait()

	def testSaveNoteAsPic(self):
		# Launch Note
		d.start_activity(component='com.smartisanos.notes/.NotesActivity')
		if d(text = '列表').exists:
			d(text = '列表').click.wait()
		assert d(text = '便签').wait.exists(timeout = 5000),'Launch Note failed in 5s!'
		for i in range(500):
			d(resourceId = 'com.smartisanos.notes:id/add_button').click.wait()
			assert d(resourceId = 'com.smartisanos.notes:id/delete_insert_button').wait.exists(timeout = 5000),'Switch to note editer failed in 5s!'
			d(resourceId = 'com.smartisanos.notes:id/detail_note_editor').set_text('test content...')
			d(resourceId = 'com.smartisanos.notes:id/delete_insert_button').click.wait()
			d.sleep(1)
			d.click(900,1830)
			d.click('image.png')
			# select first pic
			d.click(150,370)
			d.click('done.png')
			assert d(resourceId = 'com.smartisanos.notes:id/detail_note_image').wait.exists(timeout = 5000),'Add pic to note failed in 5s!'
			d(resourceId = 'com.smartisanos.notes:id/send_finish_button').click.wait()
			d(resourceId = 'com.smartisanos.notes:id/send_finish_button').click.wait()
			assert d(text = '请选择操作').wait.exists(timeout = 5000),'Share selector does not pop-up in 5s!'
			d(text = '以图片形式分享').click.wait()
			assert d(text = '保存图片').wait.exists(timeout = 5000),'Switch to thumbs failed in 5s!'
			d(text = '取消').click.wait()
			d(text = '列表').click.wait()

	def testShareNoteToWeibo(self):
		# Launch Note
		d.start_activity(component='com.smartisanos.notes/.NotesActivity')
		assert d(text = '便签').wait.exists(timeout = 5000),'Launch Note failed in 5s!'
		for i in range(500):
			d(resourceId = 'com.smartisanos.notes:id/add_button').click.wait()
			assert d(resourceId = 'com.smartisanos.notes:id/delete_insert_button').wait.exists(timeout = 5000),'Switch to note editer failed in 5s!'
			d(resourceId = 'com.smartisanos.notes:id/detail_note_editor').set_text('test content...')
			d(resourceId = 'com.smartisanos.notes:id/delete_insert_button').click.wait()
			d.sleep(1)
			d.click(900,1830)
			d.click('image.png')
			# select first pic
			d.click(150,370)
			d.click('done.png')
			assert d(resourceId = 'com.smartisanos.notes:id/detail_note_image').wait.exists(timeout = 5000),'Add pic to note failed in 5s!'
			d(resourceId = 'com.smartisanos.notes:id/send_finish_button').click.wait()
			d(resourceId = 'com.smartisanos.notes:id/send_finish_button').click.wait()
			assert d(text = '请选择操作').wait.exists(timeout = 5000),'Share selector does not pop-up in 5s!'
			d(text = '发送至新浪微博').click.wait()
			#d(text = '生成长微博').click.wait()
			#d(text = '保存到相册并继续').click.wait()
			assert d(resourceId = 'com.smartisanos.notes:id/weibo_body_view').wait.exists(timeout = 5000),'Switch to Weibo proview failed in 5s!'
			d(text = '下一步').click.wait()
			assert d(text = '发送').wait.exists(timeout = 5000),'Prepare to send weibo failed in 5s!'
			d(text = '取消').click.wait()
			d(text = '取消').click.wait()
			d(text = '列表').click.wait()