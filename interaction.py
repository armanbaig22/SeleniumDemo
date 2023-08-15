from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
search_bar = driver.find_element_by_name("search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
# driver.quit()