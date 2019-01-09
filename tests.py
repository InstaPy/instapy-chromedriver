from selenium import webdriver
from instapy_chromedriver import binary_path # this will get you the path variable

driver = webdriver.Chrome(executable_path = binary_path)
driver.get("http://www.python.org")
assert "Python" in driver.title
