url="https://www.rottentomatoes.com/m/star_wars_the_rise_of_skywalker/reviews?type=user"

from selenium import webdriver
from selenium.webdriver.firefox.options import Options # for headless mode
from selenium.webdriver.common.keys import Keys # to open developer tools

options = Options() 
# operate without browser
# # options.headless = True
options.add_argument("-devtools") # open developer tools
options.set_preference("devtools.toolbox.selectedTool", "netmonitor")

driver = webdriver.Firefox(options=options)
driver.get(url)

xpath = "/html/body/div[4]/div[3]/div[2]/section/div/div/nav[3]/button[2]/span"
buttons = driver.find_elements_by_xpath(xpath)

i = 1
n = 10000 # collect n reviews
while buttons and i < (n+1)/10+1: # we dont scrape the first page since html instead of json
    print("Scraping page", i)
    print("Collecting ", 10*i, "reviews")
    i += 1

    # click to next page
    python_button = driver.find_elements_by_xpath(xpath)[0]
    python_button.click()
    buttons = driver.find_elements_by_xpath(xpath)

