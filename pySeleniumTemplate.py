from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Initializing WebDriver
options = Options()
options.add_argument("--headless")  # optional: To run webdriver in headless mode (no GUI)
driver = webdriver.Chrome(options=options)
