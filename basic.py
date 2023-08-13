from selenium import webdriver

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# getting price of an item from amazon
# driver.get("https://www.amazon.in/MYFITNESS-Natural-Peanut-Crunchy-Unsweetened/dp/B08WRL1PYJ?pd_rd_w=LpKbm&content-id=amzn1.sym.18f84f8e-1d1c-4c06-9ae7-16d886f1f5eb&pf_rd_p=18f84f8e-1d1c-4c06-9ae7-16d886f1f5eb&pf_rd_r=C4SY7VHJCWS64978DRKF&pd_rd_wg=v9y5d&pd_rd_r=04b77d13-4ccd-4ff2-be79-368bd26540a4&pd_rd_i=B08WRL1PYJ&psc=1&ref_=pd_bap_d_grid_rp_0_2_i")
# currency = driver.find_element_by_class_name("a-price-symbol")
# price = driver.find_element_by_class_name("a-price-whole")
# print(currency.text+price.text)

# driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# anything can be accessed using xpath
# driver.get("https://www.python.org/")
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# close current tab
# driver.close()

# close all tabs
driver.quit()

