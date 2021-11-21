
import requests


class Checker: 

    def __init__(self, user, file, url):
        self.user = user
        self.url = url
        self.file = file

    def check_user(self):
        data = { 
            'log': self.user,
            'pwd': 'random_password',
            'wp-submit': 'Log In'
        }
        
        try:
            req = requests.post(self.url, data=data)

            if 'The password you entered for the username' in req.text: 
                return True 
            return False
        except: 
            return False


    def check_file(self): 
        try:
            with open(self.file, 'r') as wordlist: 
                return True 
        except: 
            return False 


    def check_url(self):
        try: 
            requests.get(self.url, timeout=5)
            return True
        except: 
            return False

