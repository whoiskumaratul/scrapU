#!/usr/bin/python
header = """

  ______                                                          __    __
 /      \                                                        /  |  /  |
/$$$$$$  |  _______   ______   ______    ______    ______        $$ |  $$ |
$$ \__$$/  /       | /      \ /      \  /      \  /      \       $$ |  $$ |
$$      \ /$$$$$$$/ /$$$$$$  |$$$$$$  |/$$$$$$  |/$$$$$$  |      $$ |  $$ |
 $$$$$$  |$$ |      $$ |  $$/ /    $$ |$$ |  $$ |$$    $$ |      $$ |  $$ |
/  \__$$ |$$ \_____ $$ |     /$$$$$$$ |$$ |__$$ |$$$$$$$$/       $$ \__$$ |
$$    $$/ $$       |$$ |     $$    $$ |$$    $$/ $$       |      $$    $$/
 $$$$$$/   $$$$$$$/ $$/       $$$$$$$/ $$$$$$$/   $$$$$$$/        $$$$$$/
                                       $$ |
                                       $$ |
                                       $$/

"""
try:
    print(header + "                             by KumarAtulJaiswal (@whoiskumaratul)\n")
except:
    print(header + "                                   by @whoiskumaratul\n")


import sys                     #we can access system specific parameters like command line arguments that are passed to the script
import pyperclip               #copy paste - clipboard module
import requests                #making HTTP requests
import pprint                  #pretty print with vertical line
import os                      #interacting with the operating system
from bs4 import BeautifulSoup                   #BeautifulSoup for parsing HTML
import csv                     #write that textual information into CSV file


try: 
    #UPDATING
    update = input("[?] Install/Update dependencies? Y/n: ")
    update = update.lower()
    if update == "y" or update == "":
       print("[I] checking/Installing dependencies, please wait...")
       os.system("sudo pip install requests")
       os.system("virtualenv websc")
       os.system("sudo pip install beautifulsoup4")
except:  
     print("")


try:
   if len(sys.argv) > 1:
       #Get address from command line.
       address = ' '.join(sys.argv[1:])
   else:
       #Get address from clipboard.
       address = pyperclip.paste()
       #sys.exit()

       print("\nPlease Wait a Few Seconds... \n")
       r = requests.get(address) 
       print(r, '- The HTTP 200 OK success status \n')
       pprint.pprint(r.text[:200])
      

       #Retrieve the links on the page
       soup = BeautifulSoup(r.text, 'lxml')

       f = csv.writer(open('scrapU.csv' ,'w'))
       f.writerow([r]) #response code status
       f.writerow(['Title'])
       f.writerow([soup.title.text])
       f.writerow([soup.text])
       print('File successfully created') 
       print('\nThank you for using our tool')
       #pprint.pprint(r.text[600:])
       #print(r.text[:500])
      
except: 
     print('Please Copy a Link first')
     print('Thank you for using our tool :-)')







