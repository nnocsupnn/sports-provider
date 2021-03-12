from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import sys
import json


class Crawler:
	src = ""

	def __init__(self):
		print("Crawling..")


	def crawl(self, path):
		self.src = path

		# Set browser
		gecko_options = Options()
		# gecko_options.add_argument('--headless')
		gecko_options.add_argument('--disable-gpu')

		browser = webdriver.Firefox(options=gecko_options)

		# Load the page
		browser.get(self.src)
		browser.implicitly_wait(10)
		browser.set_page_load_timeout(30)

		oddTypes = [
			# '1X2',
			# 'Asian Handicap',
			# 'Home/Away',
			'Over/Under'
			# 'Draw No Bet',
			# 'European Handicap',
			# 'Double Chance',
			# 'To Qualify',
			# 'Correct Score',
			# 'Half Time / Full Time',
			# 'Odd or Even',
			# 'Both Teams to Score'
		]

		defDict = { 
			'1X2': 'wdl',
			'Home/Away': 'ha',
			'Draw No Bet': 'dnb',
			'Double Chance': 'dc',
			'To Qualify': 'tq',
			'Correct Score': 'cs',
			'Half Time / Full Time': 'htft',
			'Odd or Even': 'oe',
			'Both Teams to Score': 'bts'
		}

		while True:
			sleep(1)
			for _type in oddTypes:
				try:
					odds = []
					if _type in defDict:
						print(_type, defDict[_type])
						# self[defDict[_type]](_type, browser)
					else:
						odds = self.defaultMarket(_type, browser)

					print(odds)

				except Exception as error:
					print(error)




	# For default markets
	def defaultMarket(self, _type, browser):
		print("Checking market type " + _type)

		data = WebDriverWait(browser, 5).until(
			EC.element_to_be_clickable((By.XPATH, "//a[contains(@title, '" + _type + "')]"))
		)

		d = data.click()

		oddsTable = WebDriverWait(browser, 2).until(
			EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'odds-data-table')]"))
		)

		dataTable = oddsTable.find_elements_by_class_name("table-container")
		
		oddsData = []
		for j, odd in enumerate(dataTable):


			showMore = odd.find_element_by_xpath("div[contains(@class, 'table-header-light')]//a[contains(.,'Compare odds')]")
			showMore.click()

			oddTab = odd.find_element_by_class_name('detail-odds')

			tBody = oddTab.find_element_by_tag_name('tbody')
			
			rows = tBody.find_elements_by_tag_name("td")
			
			# ths = teeHeds.find_elements_by_tag_name("th")

			field = {}
			for x, row in enumerate(rows):
				v = row.text.replace(" ", "")
				field[x] = v
				continue

			oddsData.append(field)

		return oddsData


	def wdl(self, _type, browser):
		print("wdl")