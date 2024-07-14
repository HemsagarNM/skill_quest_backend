from typing import Any
import requests
class Github_scraper():
    def __init__(self,username):
        self.username=username
        self.user_repos_info_link=f"https://api.github.com/users/{username}/repos"
        self.user_followers=f"https://api.github.com/users/{username}/followers"
        self.follower_count=0
        try:
            
            self.user_details=requests.get(self.user_repos_info_link)
            if self.user_details.status_code==404:
                self.user_details=None
            else:
                self.user_details=self.user_details.json()
                self.follower_count=len(list(requests.get(self.user_followers).json()))
            
        except:
            self.user_details=None
    def get_total_forks(self):
        count=0
        for repos in self.user_details:
            count+=int(repos['forks_count'])
        return count
    def get_total_watches(self):
        count=0
        for repos in self.user_details:
            count+=int(repos['watchers_count'])
        return count
    def get_total_stars(self):
        count=0
        for repos in self.user_details:
            count+=int(repos['stargazers_count'])
        return count
    # def get_repo_stars(self,repo_name):
    #     for repo in self.user_details:
    #         pass
            
    # def get_followers(self):
    #     pass
    # def get_languages(self):
    #     pass

    def get_user_rating(self):
        try:
            return self.user_details.json()['result'][0]['rating']
        except:
            return 0

    def get_percentile(self):
        try:
            if self.user_details==None:
                return 0
            else:
                forks=self.get_total_forks()
                watches=self.get_total_watches()
                stars=self.get_total_stars()
                if stars>=100 or forks>=50:return 100
                elif watches>=500:return 100
                elif stars==0:return 5
                elif self.follower_count>=100:return 100
                else:return max(15,stars)
        except:

            return 0



if __name__=="__main__": 
    username="harshithcodes"
    z=Github_scraper(username)
    print(z.get_percentile())


