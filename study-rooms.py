from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import numpy as np
import datetime
import calendar
import time
import math

def trainer ():
    # Get the day a week from now
    date = datetime.date.today() + datetime.timedelta(days=7)
    # print(date)

    # Intialize the driver
    driver = webdriver.Chrome() 
    # Get website string format
    website_string = "https://webapp.library.uvic.ca/studyrooms/edit_entry.php?area=1&room=8&hour=13&minute=30&year="
    # Replace the room, year, month, day
    website_string = website_string + str(date.year) + "&month=" + str(date.month) + "&day=" + str(date.day)
    # These customizable 
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
            # print("trying room " + str(room_num))
            driver.get(website_string)
            if (room_num == 8):
                website_string = website_string.replace("room=15", "room=" + str(room_num))
            else:
                website_string = website_string.replace("room=" + str(room_num - 1), "room=" + str(room_num))
            room_num += 1

            study_group_name = driver.find_element_by_name("name")
            username = driver.find_element_by_name("netlinkid")
            password = driver.find_element_by_name("netlinkpw")
            submit_button = driver.find_element_by_xpath("//input[@type='button']")

            study_group_name.send_keys("<Group name>")
            username.send_keys("********")
            password.send_keys("********")
            driver.find_element_by_xpath("//select[@name='duration']/option[text()='2 hours']").click()
            submit_button.click()
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            if(soup.find('b', text="Request Denied:") == None and soup.find('b', text="Scheduling Conflict") == None):
                print("Successful booking!")
                print(website_string)
                return
        last_time = time_x
    print("No avaiable bookings")

def main ():
    main()

if __name__ == '__main__':
    trainer()
    print("End Program")
