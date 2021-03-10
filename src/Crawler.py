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

	def __init__(self):
		print('Crawler')


	def crawl():
		srcUrl = "https://www.oddsportal.com/basketball/usa/nba-g-league/santa-cruz-warriors-lakeland-magic-hA7TQlan/"

		# Set browser
		gecko_options = Options()
		# gecko_options.add_argument('--headless')
		gecko_options.add_argument('--disable-gpu')

		browser = webdriver.Firefox(options=gecko_options)

		# Load the page
		browser.get(srcUrl)
		browser.implicitly_wait(10)
		browser.set_page_load_timeout(30)

		oddTypes = [
			# '1X2',
			'Asian Handicap',
			# 'Home/Away',
			'Over/Under',
			# 'Draw No Bet',
			'European Handicap',
			# 'Double Chance',
			# 'To Qualify',
			# 'Correct Score',
			# 'Half Time / Full Time',
			# 'Odd or Even',
			# 'Both Teams to Score'
		]

		while True:
			sleep(1)
			for _type in oddTypes:
				try:
					print("Checking market type " + _type)
					data = WebDriverWait(browser, 5).until(
						EC.element_to_be_clickable((By.XPATH, "//a[contains(@title, '" + _type + "')]"))
					)

					print("clicking tab..")

					d = data.click()

					oddsTable = WebDriverWait(browser, 2).until(
						EC.element_to_be_clickable((By.XPATH, "//div[contains(@id, 'odds-data-table')]"))
					)

					odds = oddsTable.find_elements_by_class_name('table-container')
					for odd in odds:
						tds = odd.find_elements_by_class_name("table-header-light")

						for td in tds:
							title = td.find_element_by_tag_name('strong')
							oddElements = td.find_elements_by_class_name('chunk-odd')
							odds = []

							for idx, oddElement in enumerate(oddElements):
								oddValues = oddElement.find_element_by_xpath("//a[contains(@xparam, 'odds_text')]")
								odds.append({
									"index": idx,
									"odd": oddValues.text
								})

							print(title.text, odds)

				except Exception as error:
					print(error)
		