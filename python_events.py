import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# For wait to page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LearnSelenium:
    def __init__(self):
        current_directory = os.getcwd()
        chrome_driver_path =  os.path.join(current_directory, "chromedriver.exe")
        chrome_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
    

    def getEventsFromPython(self):
        events = dict()
        self.driver.get(r"https://www.python.org")
        events_times = self.driver.find_elements(By.CSS_SELECTOR, ".blog-widget time")
        events_names = self.driver.find_elements(By.CSS_SELECTOR, ".blog-widget li a")
        for n in range(len(events_times)):
            events[events_times[n].text] = events_names[n].text

        save_to_file =os.path.join(os.getcwd(), 'events.txt')
        with open(save_to_file, 'w') as file:
            for event in events.keys():
                file.write(f"{event} : {events[event]}\n")
        print(events)
        self.driver.close()



selenium = LearnSelenium()
selenium.getEventsFromPython()

