# import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import html5lib
import lxml
import json
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from time import sleep

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_driver_path)

# driver.get("https://www.amazon.in/Bundled-Spider-Man-GTaSport-Ratchet-3Month/dp/B08FNXXH5J/ref=sr_1_1?dchild=1&keywords=ps4&qid=1622815646&sr=8-1")
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

# driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name('q')
# print(search_bar.get_attribute('placeholder'))

# documentation_link = driver.find_element_by_css_selector('.documentation-widget a') 
# '''if u want to find something under a css element eg. user documentation-widget class look for a anchor [a] tag'''
# print(documentation_link.text)

# ele = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# '''Find the element by the path to the element. Go to the element and inspect it and then right click and copy xpath'''
# print(ele.text)

#get the event table in python.org site
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
#
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         'time' : event_times[n].text,
#         'event_name' : event_names[n].text
#     }
#
# print(events)


#interaction
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# art_count = driver.find_element_by_css_selector('#articlecount a')
# # print(art_no.text) #(get no of articles on wikioedia main page)
# art_count.click()  #click a link or something

# all_portal = driver.find_element_by_link_text('All portals') #find link by text
# all_portal.click()

# search = driver.find_element_by_name('search')   #get search bar
# search.send_keys('Python')    #type python in it
# search.send_keys(Keys.ENTER)   #Press ENTER to search

# #fill a form and submit
# driver.get("http://secure-retreat-92358.herokuapp.com/")
# fname = driver.find_element_by_name('fName')
# fname.send_keys('Kartik')
# lname = driver.find_element_by_name('lName')
# lname.send_keys('Chourasiya')
# email = driver.find_element_by_name('email')
# email.send_keys('kartik@gamil.com')
# submit = driver.find_element_by_css_selector('form button')
# submit.click()


# #cookie game
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
#
# cookie = driver.find_element_by_id('cookie')
# store_elements = driver.find_elements_by_css_selector("#store div")
# for elements in store_elements:
#     print(elements.text)
# money = driver.find_element_by_id('money')
# print(money.text)


# # twitter login
# DOWNLOAD_SPEED = 150
# UPLOAD_SPEED = 10
# TWITTER_NAME = YOUR twitter username
# TWITTER_PASSWORD = YOUR twitter password
#
# class SPEED_BOT:
#
#     def __init__(self, download_speed, upload_speed, twitter_name, twitter_password):
#         self.download_speed = download_speed
#         self.upload_speed = upload_speed
#         self.twitter_name = twitter_name
#         self.twitter_password = twitter_password
#
#     def int_speed_bot(self):
#         driver.get('https://www.speedtest.net/result/11553812991')
#         go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
#         go_button.click()
#         time.sleep(30)
#         ping = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
#         time.sleep(20)
#         dn_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
#         time.sleep(20)
#         up_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
#         if (float(dn_speed.text) < self.download_speed) or (float(up_speed.text) < self.upload_speed):
#             self.twitter_bot(ping.text, dn_speed.text, up_speed.text)
#
#     def twitter_bot(self, ping, dn_speed, up_speed):
#         driver.get("https://twitter.com/login?lang=en")
#         user_name = driver.find_element_by_xpath(
#             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
#         user_name.send_keys(self.twitter_name)
#         password = driver.find_element_by_xpath(
#             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
#         password.send_keys(self.twitter_password)
#         login_button = driver.find_element_by_xpath(
#             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
#         login_button.click()
#         text = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
#         text.send_keys(f'Ping: {ping}, Download_speed: {dn_speed}, Upload_speed: {up_speed}')
#
# speed_bot = SPEED_BOT(DOWNLOAD_SPEED, UPLOAD_SPEED, TWITTER_NAME, TWITTER_PASSWORD)
# speed_bot.int_speed_bot()


# #instagram bot
# SIMILAR_ACCOUNT = 'programmerplus'
# USERNAME = 'syntax_code'
# PASSWORD = 'syntax_01'
#
#
# class InstaFollower:
#
#     def __init__(self, path):
#         self.driver = webdriver.Chrome(executable_path=path)
#
#     def login(self):
#         self.driver.get("https://www.instagram.com/accounts/login/")
#         time.sleep(5)
#
#         username = self.driver.find_element_by_name(USERNAME)
#         password = self.driver.find_element_by_name(PASSWORD)
#
#         username.send_keys(USERNAME)
#         password.send_keys(PASSWORD)
#
#         time.sleep(2)
#         password.send_keys(Keys.ENTER)
#
#     def find_followers(self):
#         time.sleep(5)
#         self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
#
#         time.sleep(2)
#         followers = self.driver.find_element_by_xpath(
#             '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
#         followers.click()
#
#         time.sleep(2)
#         modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
#         for i in range(10):
#             # In this case we're executing some Javascript, that's what the execute_script() method does.
#             # The method can accept the script as well as a HTML element.
#             # The modal in this case, becomes the arguments[0] in the script.
#             # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
#             self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
#             time.sleep(2)
#
#     def follow(self):
#         all_buttons = self.driver.find_elements_by_css_selector("li button")
#         for button in all_buttons:
#             try:
#                 button.click()
#                 time.sleep(1)
#             except ElementClickInterceptedException:
#                 cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
#                 cancel_button.click()
#
#
# bot = InstaFollower(chrome_driver_path)
# bot.login()
# bot.find_followers()
# bot.follow()

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7"
}



class RentalScrapper:
    def __init__(self):
        response = requests.get(
            "https://www.zillow.com/new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22newyork%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.86922236914063%2C%22east%22%3A-73.08669063085938%2C%22south%22%3A39.4116501476456%2C%22north%22%3A41.97548463263613%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D",
            headers=header)
        self.soup = BeautifulSoup(response.content, "html.parser")

    def get_link(self):
        all_link_elements = self.soup.select(".list-card-top a")
        all_links = []
        for link in all_link_elements:
            href = link["href"]
            if "http" not in href:
                all_links.append(f"https://www.zillow.com{href}")
            else:
                all_links.append(href)
        return all_links

    def get_price(self):
        all_price_elements = self.soup.select(".list-card-price")
        all_prices = []
        for price in all_price_elements:
            all_prices.append(price.text)
        return all_prices

    def get_addr(self):
        all_address_elements = self.soup.select(".list-card-addr")
        all_address = []
        for address in all_address_elements:
            all_address.append(address.text)
        return all_address

rental_scrapper = RentalScrapper()
links = rental_scrapper.get_link()
addrs = rental_scrapper.get_addr()
prices = rental_scrapper.get_price()



for x in range(len(links)):
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfz91OqLQWPBTfqXsftUQIFwjCUnCmWN6gwzXFOFX3hBo2emg/viewform')
    time.sleep(2)
    form_price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_addr = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    form_price.send_keys(str(prices[x]))
    form_addr.send_keys(str(addrs[x]))
    form_link.send_keys(str(links[x]))
    submit.click()
    time.sleep(5)

# driver.close()   #close particular tab
driver.quit()    #shutdown total browser
