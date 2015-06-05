#! /usr/bin/python
# -*- coding: utf-8 -*-  
import unittest
from uiautomatorplug.android import device as d
import commands
import string
import random
import util as u

MUSIC_CONTROLLER_LIST = [
						'com.smartisanos.music:id/audio_player_next',
						'com.smartisanos.music:id/audio_player_prev',
						'com.smartisanos.music:id/audio_player_shuffle',
						'com.smartisanos.music:id/audio_player_repeat'
						]

class MusicTest(unittest.TestCase):
	def setUp(self):
		u.setUp()
		#Launch music player
		d.start_activity(component='com.smartisanos.music/.activities.MusicMain')
		assert d(resourceId = 'com.smartisanos.music:id/ib_right').wait.exists(timeout=5000),'Launch music player failed in 5s!'
		d(text = '歌曲',resourceId = 'com.smartisanos.music:id/rb_song').click.wait()
		assert d(resourceId = 'com.smartisanos.music:id/tv_title',text = '歌曲').wait.exists(timeout = 5000),'Switch to music list failed in 5s!'

	def tearDown(self):
		u.tearDown()

	def testMusicContraller(self):
		# select a song to play
		d(textContains = 'MP3').click.wait()
		assert d(resourceId = 'com.smartisanos.music:id/audio_player_play').wait.exists(timeout = 5000),'Switch to music play view failed in 5s!'
		for i in range(1000):
			music_controller = random.choice(MUSIC_CONTROLLER_LIST)
			d(resourceId = music_controller).click.wait()
		d(resourceId = 'com.smartisanos.music:id/audio_player_play').click.wait()

	def testSwitchView(self):
		view_list = ['播放列表','艺术家','专辑','歌曲']
		for i in range(1000):
			view = random.choice(view_list)
			d(text = view).click()
			
