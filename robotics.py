from RPA.Browser.Selenium import Selenium
from selenium.common.exceptions import StaleElementReferenceException
PR = Selenium()
import time

class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)
        print("I am DHRUV, your robotic researcher.")
        print("I am here to assist you in finding key information about important scientists.")
        print("When I run, I will navigate to the Wikipedia page of each scientist in the list.")
        print("I will retrieve their birth and death dates, calculate their age, and provide a summary.")
        print("Finally, I will display all of this information to you in an easily understood manner.")
        with open('paragraph.txt', 'w') as file:
            file.write(f"Hello, I am {self.name}, your robotic researcher.\nI am here to assist you in finding key information about important scientists.\nWhen I run, I will navigate to the Wikipedia page of each scientist in the list.\nI will retrieve their birth and death dates, calculate their age, and provide a summary.\n \n" )

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        PR.open_available_browser(webpage)
        
    def type_text(self, scientist):
        for _ in range(3):  # Retry 3 times
            try:
                PR.input_text('xpath://input[@id="searchInput"]',scientist)
                break  # If no exception, break out of the loop
            except StaleElementReferenceException:
                time.sleep(1)

    def press_key(self, k):
        PR.press_keys('xpath://input[@id="searchInput"]', k)

    def reading(self,rd):
        print(PR.get_text(rd))
        return PR.get_text(rd)