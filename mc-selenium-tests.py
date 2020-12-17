#! /usr/bin/env python
import pytest
import time
import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options

# global vars for all functions

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)

mc_ip = sys.argv[1]

def pre_reqs():


# login
def login():
    driver.get("https://" + mc_ip + "/dashboard")
    driver.set_window_size(1440, 877)
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("userpass")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)


# assign syslog server
def firmware_upload():
    # driver.get("https://" + mc_ip + "/diagnostics/event_log.html")
    driver.find_element(By.ID, "settingsMainNav").click()
    driver.find_element(By.LINK_TEXT, "SOFTWARE").click()
    element = self.driver.find_element(By.LINK_TEXT, "SOFTWARE")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    driver.find_element(By.CSS_SELECTOR, "#btnUploadSoftware > span").click()
    driver.find_element(By.ID, "uploadSoftware").click()


# disable syslog - used for initial testing of script only
def profile_disable():
    # driver.get("https://" + mc_ip + "/diagnostics/event_log.html")
    driver.find_element(By.LINK_TEXT, "PROFILE").click()
    driver.find_element(By.CSS_SELECTOR, ".mcImportLabel").click()
    driver.find_element(By.ID, "importProfile").click()


# logout
def logout():
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.close()


def main():
    login()
    logout()


main()
