from halo import Halo
import requests

class Utils:
	def spinner(self, fn):
		spinner = Halo(text='Loading', spinner='dots')

		def func_wrapp(*args):
			spinner.start()
			fn(*args)
			spinner.stop()
		return func_wrapp

	def is_downloadable(self, url):
		if 'git' in url:
			return True

		try:
			h = requests.head(url, allow_redirects=True)
			header = h.headers
			content_type = header.get('content-type')

			if 'text' in content_type.lower():
				return False
			if 'html' in content_type.lower():
				return False

			return True
		except Exception as e:
			return False

utils = Utils()
