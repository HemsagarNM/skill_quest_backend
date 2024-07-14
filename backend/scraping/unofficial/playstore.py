from google_play_scraper import app

class Playstore_scraper:
    def __init__(self,appname):
        self.username=appname
        self.user_details=app(appname)

    def get_percentile(self):
        install_count=self.get_install_count()
        if install_count>=1000:return 100
        else:
            return (install_count/1000)*100
    '''
    get_install_count will fail if it has 10k,10k+ 10M ,100M 1B etc
    rectify in the future
    '''
    def get_install_count(self):
        splits=self.user_details['installs'].split(',')
        count=''
        for x in splits:
            count+=x
        if count[-1]=='+':
            count=count[:-1]
        return int(count)
    

if __name__=="__main__": 
    z=Playstore_scraper("com.spotify.music")
    print(z.get_percentile())

