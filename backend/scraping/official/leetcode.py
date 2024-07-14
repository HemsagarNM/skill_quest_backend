import requests
from bs4 import BeautifulSoup
import json
import re
class Leetcode_scraper:
    def __init__(self,username):
        self.username=username
        self.user_details=self.__leetcode_user_details()
    
    def __leetcode_user_details(self):
        try:
            query = """
            query {
                userContestRanking(username: "%s") {
                attendedContestsCount
                rating
                globalRanking
                totalParticipants
                topPercentage
                }
                userContestRankingHistory(username: "%s") {
                attended
                trendDirection
                problemsSolved
                totalProblems
                finishTimeInSeconds
                rating
                ranking
                contest {
                    title
                    startTime
                }
                }
            }
            """ % (self.username, self.username)
            url = "https://leetcode.com/graphql"
            headers = {"Content-Type": "application/json"}
            data = requests.post(url, json={"query": query}, headers=headers)
            data=data.json()
            return data
        except Exception as e:
            print(e)

    def get_percentile(self):
        if self.user_details ['data']['userContestRanking'] and self.user_details['data']['userContestRanking']['topPercentage']:
            return 100-self.user_details['data']['userContestRanking']['topPercentage']
        else:return 0


if __name__=="__main__": 
    z=Leetcode_scraper("hizinberg")
    print(z.get_percentile())