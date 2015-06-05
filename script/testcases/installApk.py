#! /usr/bin/python
# -*- coding: utf-8 -*- 
import os
import commands

def installAPKs():
	apk_folder = os.getcwd() + os.sep + 'APKs' + os.sep
	apks       = commands.getoutput('ls %s | grep apk'%apk_folder)
	apk_list   = apks.split('\n')
	for apk in apk_list:
		print 'Installing %s ...'%apk
		os.system('adb install %s%s'%(apk_folder,apk))

if __name__ == '__main__':
	installAPKs()