from bs4 import BeautifulSoup
import requests
import re

def titles():
    url = 'https://scp-wiki.wikidot.com/scp-series'
    site = requests.get(url)
    soup = BeautifulSoup(site.text,"html.parser")
    titles = soup.find_all('li')
    for title in titles:
        if title.a.text.find('SCP-') == 0:
             print(title.text)
def article(scp):
    url = 'https://scp-wiki.wikidot.com/scp-{}'.format(str(scp))
    site = requests.get(url)
    soup = BeautifulSoup(site.text,"html.parser")
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
    for article in articles:
        if len(article.get_text(strip=True)) != 0:
            print(article.text,"")

print (r"""
.------------------------------------------------------------------------------------------.
|                                                         ,#############,                  |
|  ____                                                   ##           ##                  |
| / ___|  ___  ___ _   _ _ __ ___                     m####             ####m              |
| \___ \ / _ \/ __| | | | '__/ _ \                 m##*'        mmm        '*##m           |
|  ___) |  __/ (__| |_| | | |  __/_              ###'         mm###mm         '###         |
| |____/ \___|\___|\__,_|_|  \___(_)           ###        m#############m        ###       |
|                                             ##       m####*'  ###  '*####        ##      |
|                                            ##      m####      ###      ####m      ##     |
|   ____            _        _              ##      ####      #######      ####      ##    |
|  / ___|___  _ __ | |_ __ _(_)_ __        m#      ###'        #####        '###      #m   |
| | |   / _ \| '_ \| __/ _` | | '_ \       ##     ####           #           ####     ##   |
| | |__| (_) | | | | || (_| | | | | |_     ##     ###    wwwwwwww wwwwwwww    ###     ##   |
|  \____\___/|_| |_|\__\__,_|_|_| |_(_)    ##     ###m    ######   ######    m###     ##   |
|                                        ,###     '### m#######     #######m ###'     ###, |
|                                        ##'      m######'   *       *   '######m      '## |
|  ____            _            _         ##     *#*'######             ######'*#*     ##  |
| |  _ \ _ __ ___ | |_ ___  ___| |_        ##         '#######m     m#######'         ##   |
| | |_) | '__/ _ \| __/ _ \/ __| __|        *#m          '###############'          m#*    |
| |  __/| | | (_) | ||  __/ (__| |_ _         ##m ,m,        ''*****''        ,m, m##      |
| |_|   |_|  \___/ \__\___|\___|\__(_)         *##'*###m                   m###*'##*       |
|                                                    '*#######m     m#######*'             |
|                                                           '*#######*'                    |
'------------------------------------------------------------------------------------------'""") 
print("Loading database...")
titles()
print('Ready!')
print("""
        WARNING: THE FOUNDATION DATABASE IS

                    CLASSIFIED

ACCESS BY UNAUTHORIZED PERSONNEL IS STRICTLY PROHIBITED
  PERPETRATORS WILL BE TRACKED, LOCATED, AND DETAINED
""")
print('Select database entry by typing  numbers or type \'exit\' to close database: ')
while True:  
    scp = input()   
    
    
     
    if scp.lower() != 'exit' and len(scp)==3:   
            print("=======================ENTRY=======================") 
            article(scp)
            print("=======================END=======================")
            print("Select another entry or type \'exit\' to close database:")
    
    else:
        print('Exiting program...')
        break  

