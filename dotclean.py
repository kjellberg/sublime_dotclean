import sublime
import sublime_plugin
import os
import time

class DotCleanOnSave(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		file_path = view.file_name()
		directory = os.path.dirname(file_path)
		cmd = "dot_clean '" + directory + "'"
		time.sleep(1)
		os.system(cmd)
