import requests

from google_play_scraper import app

class Microsoftstore_scraper:
    def __init__(self,appname):
        self.username=appname
        self.user_details=requests.get(appname)
        if self.user_details.status_code==404:
            self.user_details=None

    def get_percentile(self):
        if self.user_details:return 80
        else:return 0

    '''
    Fill in the future
    '''
    def get_install_count(self):
        print(self.user_details)
    

if __name__=="__main__": 
    z=Microsoftstore_scraper("https://apps.microsoft.com/detail/9pb3b81f8p8d?hl=en-us&gl=IN")
    print(z.get_percentile())

