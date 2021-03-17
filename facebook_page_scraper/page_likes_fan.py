from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sqlite3
from datetime import datetime
import csv


class FacebookPageCommunity():
    def __init__(self, browser='Chrome'):
        ROOT_DIR = os.path.dirname(__file__)
        databasepath = os.path.join(ROOT_DIR, 'db.sqlite')
        self.conn = sqlite3.connect(databasepath)
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
        self.conn.close()

    def goToCommunity(self,page):
        try:
            print("go to {} page".format(page))
            link = "https://www.facebook.com/pg/{}/community".format(page)
            self.driver.get(link)
            items = self.driver.find_elements_by_class_name("_3xom")
            likes = []
            for item in items:
                likes.append(item.text)

            if len(likes):
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                c = self.conn.cursor()
                c.execute(
                    "insert into pages (page, follows, likes, created_at) values (?, ?, ?, ?)",
                    [page, likes[0], likes[1], dt_string])
                self.conn.commit()
                print('after insert record')

            # self.close_driver()
        except Exception as ex:
            self.close_driver()
            print("error at close_driver method : {}".format(ex))



def export_database_to_csv():
        try:
            ROOT_DIR = os.path.dirname(__file__)
            databasepath = os.path.join(ROOT_DIR, 'db.sqlite')
            conn = sqlite3.connect(databasepath)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            query = "SELECT * FROM pages "
            cur.execute(query)
            rows = cur.fetchall()
            # print('here')
            # headers of the CSV file
            fieldnames = ['Page Name', 'Total Follows', 'Total Likes']
            # open and start writing to CSV files
            filename = os.path.join(ROOT_DIR, 'likes.csv')
            with open(filename, 'w', newline='', encoding="utf-8") as data_file:
                writer = csv.DictWriter(data_file,
                                        fieldnames=fieldnames)  # instantiate DictWriter for writing CSV file
                writer.writeheader()  # write headers to CSV file
                # iterate over entire dictionary, write each posts as a row to CSV file
                for record in rows:
                    row = {
                            'Page Name': record['page'],
                            'Total Follows': record['follows'],
                            'Total Likes': record['likes'],
                           }
                    writer.writerow(row)  # write row to CSV file
            data_file.close()  # after writing close the file
        except Exception as ex:
            print(ex)
            return False

if __name__ == '__main__':
    export_database_to_csv()

    # pages_list = [
    #     "NYUAD",
    #     "AbuDhabiUni",
    #     "ZayedUniversity",
    #     "AbuDhabiSchoolOfManagement", "AAU.UAE","KIC.UAE","ECAEinfo","ectuae","eibfs","khalifauniversity",
    #     "UniversityOfStrathclyde","UAEUNews",
    #     "mynyit", "sorbonnead",
    #     "INSEAD" , "hctuae",
    #     "Fatima-College-of-Nursing-and-Health-Sciences-105860528214576"
    # ]
    # fb = FacebookPageCommunity(browser='Firefox')
    # for page in pages_list:
    #     fb.goToCommunity(page)