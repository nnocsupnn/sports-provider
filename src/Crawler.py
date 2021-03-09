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
		srcUrl = "https://www.oddsportal.com/soccer/italy/primavera-1/juventus-torino-IclkK9KD/"

		# Set browser
		gecko_options = Options()
		# gecko_options.add_argument('--headless')
		gecko_options.add_argument('--disable-gpu')

		browser = webdriver.Firefox(options=gecko_options)

		# Load the page
		browser.get(srcUrl)
		browser.implicitly_wait(10)
		browser.set_page_load_timeout(30)

		data = WebDriverWait(browser, 10).until(
			EC.element_to_be_clickable((By.XPATH, "//a[contains(@title, 'Asian Handicap')]"))
		)

		print("clicking tab..")

		d = data.click()

		oddsTable = WebDriverWait(browser, 10).until(
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
					oddValues = oddElement.find_element_by_tag_name('a')
					odds.append({
						"index": idx,
						"odd": oddValues.text
					})

				print(title.text, odds)