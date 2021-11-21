from termcolor import colored

def banner(): 
	print(colored("""
    ┬ ┬┌─┐   ┬ ┬┌─┐┌─┐┬─┐   ┌─┐┌─┐┌─┐┌─┐
    │││├─┘───│ │└─┐├┤ ├┬┘───├─┘├─┤└─┐└─┐ (by sha-16)
    └┴┘┴     └─┘└─┘└─┘┴└─   ┴  ┴ ┴└─┘└─┘
    """, 'red'))

def helper(url):
        print(colored("[*] ", 'blue') + f"Use: {url} <valid-user> <dictionary> <url>")
        print(f"\n~ Examples:\n")
        print(f"\t$ {url} john /usr/share/wordlist/rockyou.txt http://domain.net/wp-login.php")
        print(f"\t$ {url} admin passwords.txt http://10.10.30.30/main/wp-login.php")
        print(f"\t$ {url} administrator dictionary.txt http://10.10.30.30/wordpress/wp-login.php")
        print(f"\t$ {url} manager psswd.txt http://admin.domain.net/wp/wp-login.php")
        print(colored("\n[*] Happy Hacking!", 'red'))
