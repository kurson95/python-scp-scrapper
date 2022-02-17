from bs4 import BeautifulSoup
import requests
import re
import os
from io import StringIO
import shutil

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def titles():
    url = 'https://scp-wiki.wikidot.com/scp-series'
    site = requests.get(url)
    soup = BeautifulSoup(site.text,"html.parser")
    titles = soup.find_all('li')
    print("Loading database...")
    cls()
    for title in titles:
        if title.a.text.find('SCP-') == 0:
             print(title.text)
    print('Ready!')

def article(scp):
    if os.path.isdir('database') == False:
        os.mkdir('database')
    path = ('database/scp-{}.txt'.format(scp))
    cls()
    
    if len(scp) ==3:
        if os.path.isfile(path) == True:
            with open(path) as f:
                contents = f.read()
                print(contents,'\n','Data loadaed from local file!')
        else:        
    
            url = 'https://scp-wiki.wikidot.com/scp-{}'.format(str(scp))
            site = requests.get(url)
            soup = BeautifulSoup(site.text,"html.parser")
            for script in soup(["script", "style"]):
                script.decompose()
            content = soup.find(id='page-content')
            articles = content.findChildren(recursive=False)
            try:
                soup.find('div', class_='licensebox').decompose()
            except:pass
            try:
                soup.find('div', class_='footer-wikiwalk-nav').decompose()
            except:pass
            try:
                soup.find('div', class_='menu-item').decompose()
            except:pass
            try:
                soup.find('div',class_='page-rate-widget-box').decompose()
            except:pass
            try:
                soup.find('div',class_='scp-image-block block-right').decompose()
            except:pass
            try:
                soup.findAll('a',class_='collapsible-block-link').decompose()
            except:pass
            try:
                soup.findAll('div',class_='collapsible-block-folded').decompose()
            except:pass
            try:
                soup.findAll('div',class_='collapsible-block-unfolded-link').decompose()
            except:pass
            try:
                soup.findAll('href',class_='collapsible-block-link').decompose()
            except:pass
            try:
                soup.findAll('div',class_='collapsible-block-unfolded').decompose()
            except:pass
            s = StringIO()

            for article in articles:

                    if len(article.get_text(strip=True)) != 0:
                        print(article.text,"",file=s)
            result = s.getvalue()
            print(result)
            print('Data loaded! Do you want to save it? Y/N')
            save = input()
            #if os.path.isfile(path) == True:
            #    print('File exist!')
            #else:
            if save.lower() == 'y':
                
                file = open(path,'w')
                file.write(result)
                file.close()
            
                
                
    else:
        print('Wrong entry number! ')
def logo():
    url = 'https://raw.githubusercontent.com/pi314/ascii-arts/master/scp-foundation.logo.asciiart'
    logo = requests.get(url)
    

    print(logo.text.center(shutil.get_terminal_size().columns))
    print("""
        WARNING: THE FOUNDATION DATABASE IS

                    CLASSIFIED

ACCESS BY UNAUTHORIZED PERSONNEL IS STRICTLY PROHIBITED
  PERPETRATORS WILL BE TRACKED, LOCATED, AND DETAINED
""".center(shutil.get_terminal_size().columns))
def menu(x):
    
    if x == 'database':
        titles()  
    elif x == 'exit':
        return True
    elif x.isdigit():
        article(x)
    elif x =='help':
        print('commands: database , help , exit , logo , clear' )
    elif x == 'logo':
        logo()
    elif x =='clear':
        cls()
    else:
        print('Wrong command!')
        deus()
def deus():
    print('Digital Environmental Universal System ver 0.2.18.95')
    while True:
        command = input('scp@deus:$ ')
        if command == 'ls':
            print(os.listdir("database/"))
        if command == 'logoff':
            break
        
logo()

print('Type \'database\' to show list of scp\'s or scp number (3 digits) to show database entry.\nTyping \'exit\' will close the program.')
while True :

    scp = input('>> ')
    
    if menu(scp) == True:
        print('Exiting program...')
        break


