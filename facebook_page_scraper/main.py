from facebook_page_scraper import Facebook_scraper
import os.path
import sqlite3

#instantiate the Facebook_scraper class

# ADPolytechnic   this is not page but profile
# pages_list = [
# "AbuDhabiUni",
# "ZayedUniversity",
# "AbuDhabiSchoolOfManagement", "AAU.UAE","KIC.UAE","ECAEinfo","ectuae","eibfs","khalifauniversity",
# "UniversityOfStrathclyde","UAEUNews",
# "mynyit", "sorbonnead",
# "INSEAD" , "hctuae",
# "Fatima-College-of-Nursing-and-Health-Sciences-105860528214576"
# ]
pages_list = ["NYUAD"] #"NYUAD"
posts_count = 10
browser = "firefox"
keywords = ['research', 'faculty', 'curriculum', 'campus',
           'students', 'alumni', 'industry', 'events',
           'products', 'image', 'reputation', 'announcements', 'and others']
providers = ['facebook']
requiredPage = 'NYU Abu Dhabi'
start = '2021-03-01'
end = '2021-03-15'
if __name__ == '__main__':
     page = "NYUAD"
     print('Start Export Data {}'.format(page))
     facebook_ai = Facebook_scraper(page, posts_count, browser)
     facebook_ai.export_database_to_csv(providers, keywords, start, end, requiredPage)
     print('END Export Data {}'.format(page))
     for page in pages_list:
          # print('Start Scrapping {}'.format(page))
          # facebook_ai = Facebook_scraper(page,posts_count,browser)
          # '''this is to scrap data into database'''
          # facebook_ai.scrap_to_database()

          ''' this is to scrap data and disply dirctly '''
          # call the scrap_to_json() method
          # json_data = facebook_ai.scrap_to_json()
          # print(json_data)

          # ''' this is to scarp data into csv'''
          # filename = "{} facebook".format(page)  # file name without CSV extension,where data will be saved
          # ROOT_DIR = os.path.dirname(__file__)
          # directory = os.path.join(ROOT_DIR, 'outputs')  # directory where CSV file will be saved
          # # # print(directory)
          # # # print(os.path.exists(directory))
          # if not os.path.exists(directory):
          #      os.makedirs(directory)
          # os.chdir(directory)  # change working directory to given directory
          # facebook_ai.scrap_to_csv(filename, directory)
          print('Finished Scrapping Posts From Page {}'.format(page))