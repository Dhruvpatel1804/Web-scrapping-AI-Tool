from robotics import Robot
from datetime import datetime
import time

# List of scientists whose information you would like to print.
SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Aryabhata"]
robot = Robot("DHRUV")

def introduce_yourself():
    robot.say_hello()

def goodbye():
    robot.say_goodbye()

def navigate_to_wikipedia_page(scientist):
    robot.open_webpage("https://en.wikipedia.org/")
    time.sleep(2)
    robot.type_text(scientist)
    robot.press_key("ENTER")


def retrieve_information(scientist):
    birth_date = robot.reading('xpath://*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[3]/td')
    death_date = robot.reading('xpath://*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[4]/td')
    
    for i in birth_date.split():
        if i.isdigit() and len(i)== 4:
            birth_date = int(i)
    
    for i in death_date.split():
        if i.isdigit() and len(i)== 4:
            death_date = int(i)
    
    age = calculate_age(birth_date, death_date)
    summary = robot.reading('xpath://*[@id="mw-content-text"]/div[1]/p[2]')
    return birth_date, death_date, age, summary


def calculate_age(birth_date, death_date):
    current_year = datetime.now().year
    if death_date > current_year:
        death_date = current_year  # To handle living scientists with no death date
    age = death_date - birth_date
    return age


def display_information(scientist, birth_date, death_date, age, summary):
    print("Scientist:", scientist)
    print("Birth Date:", birth_date)
    print("Death Date:", death_date)
    print("Age:", age)
    print("Summary:", summary)
    with open('paragraph.txt', 'a',encoding='utf-8') as file:
        file.write(f"'Scientist:' {scientist}\n" + f"'Birth Date:' {birth_date}\n" + f"'Death Date:' {death_date}\n" + f"'Age:' {age}\n" + f"'Summary:' {summary}\n \n")
        
def main():
    introduce_yourself()
    
    for scientist in SCIENTISTS:
        navigate_to_wikipedia_page(scientist)
        birth_date, death_date, age, summary = retrieve_information(scientist)
        display_information(scientist, birth_date, death_date, age, summary)
    goodbye()

if __name__ == "__main__":
    main()
