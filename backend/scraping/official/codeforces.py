from typing import Any
import requests
class Codeforces_scraper():
    def __init__(self,username):
        self.username=username
        user_info_link=f"https://codeforces.com/api/user.info?handles={username}&checkHistoricHandles=false"
        try:
            self.user_details=requests.get(user_info_link)
        except:
            self.user_details=None
    def get_top_rating(self):
        return 3700
    def get_user_rating(self):
        try:
            return self.user_details.json()['result'][0]['rating']
        except:
            return 0

    def get_percentile(self):
        return (self.get_user_rating()/self.get_top_rating())*100



if __name__=="__main__": 
    username="Benq"
    z=Codeforces_scraper("Benq")
    print(z.get_percentile())


