from backend.scraping.official import leetcode,codeforces,github
from backend.scraping.unofficial import codechef,playstore,microsoftstore
from backend.CollegeData.CollegeClusters import college_clusters
from urllib.parse import urlparse
import re
websites=['leetcode.com','codechef.com','codeforces.com']
cluster_weights=[0,.16,.30,.50,.80]
def get_website_score(website,username):
    if website=='leetcode.com':
        return leetcode.Leetcode_scraper(username).get_percentile()
    elif website=='codeforces.com':
        return codeforces.Codeforces_scraper(username).get_percentile()
    elif website=='codechef.com':
        return codechef.Codechef_scraper(username).get_percentile()
    else:
        return 0



def remove_special_characters(string):
    col=re.sub(r'[^A-Za-z0-9]', '', string)
    return col.lower()
def get_username(link):
    if link[-1]=='/':
        link = link[:-1]
    return link[link.rfind('/')+1:]
def get_domain(link):
    if link[:5]=='https':
        link = link[8:]
    domain=link[:link.find('/')]
    return domain



class ScoreGenerator:
    def __init__(self,resume):
        self.resume = resume

    def _competitive_websites_score(self):
         stats = {}
         if self.resume.codingPlatformLinks:
             cpl = self.resume.codingPlatformLinks

             for link in cpl:
                 if  link[1]:
                     website = get_domain(link[1])
                     username = get_username(link[1])
                     score = get_website_score(website,username=username)
                     stats[link[0]] = score
         return max(stats.values()) if stats.values() else 0,stats

                  
                    
 
    def _education_score(self):
         stats = {}
         try:
            bin_college = None
            cluster_number=-1
            marks=-1
            if self.resume.education:
               education = self.resume.education
               for edu in education:
                  if education[edu].institution:
                     if education[edu].institution.name:
                        stats['institution'] = education[edu].institution.name
                        bin_college = remove_special_characters(education[edu].institution.name)
                     try:
                        if  edu=='UG' and education[edu].marks!=None:
                            marks = float(education[edu].marks)
                     except Exception as e :
                        print(e)
                        marks = -1
                     for college in college_clusters:
                        if bin_college in college_clusters[college]:
                           cluster_number = college
                        #    stats['institution'] = bin_college

            return 0 if marks==-1 else float(marks),1 if cluster_number==-1 else cluster_number,stats
         except Exception as exc:
            print(exc)
            print("error: ",exc)
            print("error file info: ",exc.__traceback__.tb_frame)
            print("error line#: ",exc.__traceback__.tb_lineno)
            return "unknown error"
    

    def get_score(self):
      stats = {}
      cp,stats_cp = self._competitive_websites_score()
      stats['CP'] = stats_cp
      marks,cluster,stats_edu = self._education_score()
      stats['education'] = stats_edu
      stats['score'] = 0 + cluster_weights[cluster]*marks +(1-cluster_weights[cluster])*cp
      return stats
      


if __name__=="__main__":
    resume={'personalInfo': 
            {'name': 'MANISHA ABDAR', 
             'phoneNumber': '+91 83559 30972', 
             'gitHub': None, 
             'email': 'manisha.abdar07@gmail.com', 
             'dob': None, 
             'address': 
                {'city': 'Pune', 
                'state': None, 
                'pinCode': None, 
                'country': None
                }
            }, 
            'education': 
                {'UG': 
                    {'institution': 
                        {'name': 'Mumbai University', 
                         'address': None
                        }, 
                         'board': None, 
                         'marks': '82.5%', 
                         'duration': None, 
                         'start': '2017', 
                         'end': '2020'
                    }
                }, 
                'projects': [], 
                'certifications': [],
                  'experience': 
                  [
                      {
                            'company': 'PARAGYTA TECHNOLOGIES', 
                            'role': 'Java Developer', 
                            'project': None, 
                            'duration': '2.4+ years', 
                            'start': 'Jun 2020', 
                            'end': 'Till date'
                        }
                    ], 
                    'codingPlatformLinks': {}, 
                    'skills': ['Spring Boot', 'Hibernate', 'Microservices']
            }
# print(ScoreGenerator(resume).get_score())
