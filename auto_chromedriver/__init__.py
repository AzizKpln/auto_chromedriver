import requests,string,subprocess,re
import logging
from bs4 import BeautifulSoup
from sys import platform;import sys
class auto_chromedriver_installer:
	def __init__(self):
		self.url_file = 'https://chromedriver.storage.googleapis.com/'
		
		if platform == "linux" or platform == "linux2":
			self.system="Linux"
			self.file_name = 'chromedriver_linux64.zip'
			self.version_chromium=subprocess.check_output(["chromium","--version"]).decode().split(" ")
		elif platform == "darwin":
			self.system="MacOS"
			print("This Python Module Is Developed For Linux Systems")
			sys.exit()
		elif platform == "win32":
			self.system="Windows"
			self.file_name = 'chromedriver_win32.zip'
			print("This Python Module Is Developed For Linux Systems")
			sys.exit()
	def check_chromium(self):
		
		for j in self.version_chromium:
			for i in string.digits:
				if i in j:
					self.current_chromium_version=j
	def chromium_version(self):
		self.check_chromium()
		print(self.current_chromium_version)
	def chromedriver_version(self):
		self.check_chromium()
		self.current_chromedriver_version=self.current_chromium_version.split(".")
		self.current_chromedriver_version=self.current_chromedriver_version[0]+"."+self.current_chromedriver_version[1]+"."+self.current_chromedriver_version[2]
	def parseTheWeb(self):
		r = requests.get('https://chromedriver.chromium.org/downloads')
		source=BeautifulSoup(r.content,"html.parser")
		self.findVersion=source.find("div").text
		self.findVersion=self.findVersion.split(self.current_chromedriver_version)
		self.get_version=re.search("\d\d",self.findVersion[1]).group(0)
		self.current_chromedriver_version=self.current_chromedriver_version+"."+self.get_version
	def install(self):
		self.chromedriver_version()
		self.parseTheWeb()
		file = requests.get(self.url_file + self.current_chromedriver_version + '/' + self.file_name)
		with open(self.file_name, "wb") as code:
			code.write(file.content)
	def log(self):
		self.chromedriver_version();self.parseTheWeb()
		logging.basicConfig(level=logging.DEBUG)
		logging.info("Chromedriver OS Info:"+self.system)
		logging.info('System Chromedriver Version:'+self.current_chromium_version)
		logging.info('Needed Chromedriver Version:'+self.current_chromedriver_version)
		logging.info('Link For Chromedriver:'+self.url_file + self.current_chromedriver_version + '/' + self.file_name)
		logging.info('Your File Is Installed As:'+self.file_name)
		logging.info('https://github.com/AzizKpln/auto_chromedriver')
		
