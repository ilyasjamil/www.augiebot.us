from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionTellEvents(Action):

    def name(self) -> Text:
        return "action_tell_events"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'https://www.augustana.edu/about-us/events'
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('log-level=3')
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.set_page_load_timeout(20)
        driver.maximize_window()

        events = driver.find_elements(By.CLASS_NAME, 'post__title')
        dates = driver.find_elements(By.CLASS_NAME, 'post__metadata')
        dict = {}
        for i in range(len(events)):
            dict[events[i].text]= dates[i].text
        msg = ''
        for key in dict:
            msg = msg + f'{key} at {dict[key]}<br>'
        dispatcher.utter_message(text=msg)

        return []

class ActionTellNumberOfDiners(Action):

    def name(self) -> Text:
        return "action_tell_number_dining"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.augustana.edu/student-life/residential-life/dining"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('log-level=3')
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.set_page_load_timeout(20)
        driver.maximize_window()
        iframe = driver.find_element(By.XPATH, "./html/body/div[1]/div[4]/main/div/div[2]/div[1]/p/iframe")
        driver.switch_to.frame(iframe)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.MuiTypography-root.jss10.MuiTypography-body1' )))
        numbers = driver.find_elements(By.CSS_SELECTOR, '.MuiTypography-root.jss10.MuiTypography-body1' )

        msg = f'There are currently {numbers[0].text} people eating at the dining hall.'
        dispatcher.utter_message(text=msg)

        return []

class ActionTellMenu(Action):

    def name(self) -> Text:
        return "action_tell_menu"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'https://augustana.net/csldining/new_app/#augustana-public-menu/?view_11_filters=%5B%7B%22text%22%3A%22Today%22%2C%22field%22%3A%22field_3%22%2C%22operator%22%3A%22is%20today%22%2C%22value%22%3A%7B%22all_day%22%3Afalse%2C%22date%22%3A%2206%2F16%2F2021%22%7D%2C%22key%22%3A%2210%22%7D%5D&view_11_page=1&view_11_per_page=10'
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('log-level=3')
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.set_page_load_timeout(20)
        driver.maximize_window()
        station = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'col-1')))
        mealType = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'col-2')))
        meals = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'col-3')))
        mealsList = []
        for i in range(len(meals)):
            mealsList.append(meals[i].text.replace('\n',', '))
        msg = ""
        for el,el2, el3 in zip(station,mealType, mealsList):
            msg = msg + f'{el.text} ({el2.text}): {el3}<br>'
        dispatcher.utter_message(text=msg)

        return []
