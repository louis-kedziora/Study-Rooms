from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import datetime
import calendar
import time
import math
import os

def login(driver, website_string):
    driver.get(website_string)
    login_button = driver.find_element_by_xpath("//input[@value='Log in']")
    login_button.click()
    username_box = driver.find_element_by_xpath("//input[@name='username']")
    password_box = driver.find_element_by_xpath("//input[@name='password']")
    submit_button = driver.find_element_by_xpath("//input[@name='form-submit']")
    username_box.send_keys(os.environ['SRUSER'])
    password_box.send_keys(os.environ['SRPASS'])
    submit_button.click()


def find_study_room():

    # Get the day a week from now
    date = datetime.date.today() + datetime.timedelta(days=7)
    print(date)
    options = Options()
    # Change to False for debug to see pages
    options.headless = True

    # Intialize the driver
    driver = webdriver.Chrome(options=options)
    website_string = "https://webapp.library.uvic.ca/studyrooms/edit_entry.php?area=1&room=8&hour=13&minute=30&year="
    # Replace the room, year, month, day
    website_string = website_string + str(date.year) + "&month=" + str(date.month) + "&day=" + str(date.day)
    login(driver, website_string)
    # Room 8 - 15
    # Hour 13
    # Minute 30
    time_x = 13.0
    last_time = 13.5
    while time_x < 18.5:
        time_x += 0.5
        if (math.modf(time_x)[0] == 0):
            website_string = website_string.replace("minute=30", "minute=00")
        else:
            website_string = website_string.replace("minute=00", "minute=30") 
        website_string = website_string.replace("hour=" + str(int(last_time)), "hour=" + str(int(time_x)))
        room_num = 8
        while room_num < 16:
            driver.get(website_string)
            if (room_num == 8):
                website_string = website_string.replace("room=15", "room=" + str(room_num))
            else:
                website_string = website_string.replace("room=" + str(room_num - 1), "room=" + str(room_num))
            room_num += 1

            study_group_name = driver.find_element_by_name("name")
            submit_button = driver.find_element_by_name("save_button")

            study_group_name.send_keys(os.environ['SRGROUP'])
            select = Select(driver.find_element_by_name('end_seconds'))
            select.select_by_index(3)
            submit_button.click()
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            if(soup.find('h2', text="Scheduling Conflict") == None):
                print("Successful booking!")
                print(website_string)
                return
        last_time = time_x
    print("No avaiable bookings")

def main ():
    main()

if __name__ == '__main__':
    find_study_room()
    print("End Program")
