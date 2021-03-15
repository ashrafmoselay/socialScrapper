from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

LOGIN_URL = 'https://www.facebook.com/login.php'


class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1)  # Wait for some time to load

    def login(self):
        # email_element = self.driver.find_element_by_id('email')
        # email_element.send_keys(self.email)  # Give keyboard input
        #
        # password_element = self.driver.find_element_by_id('pass')
        # password_element.send_keys(self.password)  # Give password as input too
        #
        # login_button = self.driver.find_element_by_id('loginbutton')
        # login_button.click()  # Send mouse click
        #
        # time.sleep(2)  # Wait for 2 seconds for the page to show up
        print('go to AXA page')

        self.driver.get('https://web.facebook.com/pg/NYUAD/posts')

        commentaires = self.driver.find_elements_by_class_name("commentable_item")

        print('nombre de commentaires trouvés')

        for com in commentaires:
            print(com.text)



if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin(email='ashrafhassan42@yahoo.com', password='Ashraf@1010', browser='Firefox')
    fb_login.login()