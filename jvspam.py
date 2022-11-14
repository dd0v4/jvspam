from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import requests
import time
import os



os.system("cls")
print("La Planque 2022.")
i = 0

topicmessage = (""" 
Hey, salut toi ! https://image.noelshack.com/fichiers/2019/50/2/1575969517-capture-d-ecran-2019-12-10-a-10-16-46.png

Tu veux être retiré du spam ? https://image.noelshack.com/fichiers/2021/43/4/1635454847-elton-john-tison-golem.png

Pour ça c'est simple, suffit de rejoindre et d'envoyer ton pseudo dans le salon fait pour ça https://image.noelshack.com/fichiers/2021/43/4/1635454847-elton-john-tison-golem.png

Mais si tu quittes ensuite, on retirera ton pseudo des exceptions https://image.noelshack.com/fichiers/2017/13/1490886827-risibo.png

Maintenant voici le message habituel https://image.noelshack.com/fichiers/2021/08/1/1613997318-zidane.png


Je viens d'atterrir dans tes messages privés alors j'en profite pour t'inviter sur notre nouveau serveur Discord. https://image.noelshack.com/fichiers/2017/21/1495488157-videur-bagarre.jpg

C'est le premier Discord communautaire du forum Blabla 18-25. La bonne ambiance est au rendez-vous et de nombreuses surprises t'attendent alors, qu'attends-tu pour nous rejoindre mon khey ? https://image.noelshack.com/fichiers/2017/21/1495488157-videur-bagarre.jpg


Lien du serveur : https://discord.gg/82f5AU4UMw https://image.noelshack.com/fichiers/2017/21/1495488157-videur-bagarre.jpg
""")
bypasslite = ['chocomint', 'Eyeless0', 'Proutette', 'Dopidu67', 'Bol2Glace', 'Bol2GlaceBis', 'GPaLuLeTopic', '[morty79]', 'Politicien', 'BarAEau', 'Proutingby', 'SamLosco', 'Place-Forte', 'PassionCambrien', 'parloir', 'MuguetLeHardie', 'Moderation76', 'MicrosoftNET', 'Lystrosaurus', 'IsseenSahTosah', 'depitdeprouting', 'CASHHHH', 'CASHHH1', '1Sucre2Gilberts', '1Sucre2Gilbert']
pseudojvc = input("Rentre ton pseudo jvc : ")
mdpjvc = input("Rentre le mot de passe de ton compte jvc : ")
topictitre = input("Entre le titre que tu veux mettre : ")
nombredepseudos = input("Entre le nombre de pseudos à mettre dans le spam : ")
topicplace = int(input("Numéro du topic après les épinglés : "))
topicplace = topicplace - 1
srv = Service("geckodriver.exe")
driver = webdriver.Firefox(service=srv)
driver.get("https://www.jeuxvideo.com/login")
loginpseudo = driver.find_element(by=By.NAME, value="login_pseudo")
loginpseudo.send_keys(pseudojvc)
mdp = driver.find_element(by=By.NAME, value="login_password")
mdp.send_keys(mdpjvc)
login = driver.find_element(by=By.CLASS_NAME, value="btn.btn-valid-form.js-g-recaptcha")
login.click()

urlmsg = False
while urlmsg == False:
    if driver.current_url == "https://www.jeuxvideo.com/":
        urlmsg = True

time.sleep(2)
while True:
    try:
        messagejava = driver.find_element(by=By.CLASS_NAME, value="jad_cmp_paywall_button.jad_cmp_paywall_button-cookies.jad_cmp_paywall_cookies.didomi-components-button.didomi-button.didomi-dismiss-button.didomi-components-button--color.didomi-button-highlight.highlight-button")
        messagejava.click()
        break
    except NoSuchElementException:
        continue

coniunctio = driver.get_cookie("coniunctio")
dlrowolleh = driver.get_cookie("dlrowolleh")
euconsent = driver.get_cookie("euconsent-v2")
didomi_token = driver.get_cookie("didomi_token")

while True:
    compteur = 0
    driver.get("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
    topic = driver.find_elements(by=By.CLASS_NAME, value="xXx.lien-jv")
    topic[topicplace].click()
    posts = driver.find_elements(by=By.CLASS_NAME, value="xXx.bloc-pseudo-msg.text-user")
    pseudos = []
    while len(pseudos) != int(nombredepseudos):
        pareil = False
        driver.get("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
        topic = driver.find_elements(by=By.CLASS_NAME, value="xXx.lien-jv")
        topic[topicplace].click()
        time.sleep(0.5)
        posts = driver.find_elements(by=By.CLASS_NAME, value="xXx.bloc-pseudo-msg.text-user")
        for psd in pseudos:
            try:
                if psd == posts[len(posts) -1].text:
                    print("Pseudo déjà présent dans la liste.")
                    pareil = True
                    break
            except IndexError:
                continue
        if pareil == True:
            continue
        compteur = compteur + 1
        if compteur == 1:
            print("1 er pseudo ajouté.")
        else:
            print(f"{compteur} ème pseudo ajouté.")
        try:
            pseudos.append(posts[len(posts) -1].text)
        except IndexError:
            continue
    compt = 0
    for pseudd in pseudos:
        if pseudd in bypasslite:
            del pseudos[compt]
        compt = compt + 1
    print(pseudos)

    time.sleep(1)
    driver.get("https://www.jeuxvideo.com/messages-prives/nouveau.php")
    urlpassed = False
    while urlpassed == False:
        if driver.current_url == "https://www.jeuxvideo.com/messages-prives/nouveau.php":
            urlpassed = True

    jquery = requests.get("https://code.jquery.com/jquery-1.12.4.min.js").text
    driver.execute_script(jquery)
    for pseudo in pseudos:
        driver.execute_script(f"$(\".form-control-tag-inner\").append('<span class=\"label label-default\"><span class=\"text-\">' + \"{pseudo}\" + '</span><span class=\"close close-tag\" aria-hidden=\"true\">\u00d7</span><input type=\"hidden\" name=\"participants[' + \"{pseudo}\" + ']\" value=\"' + \"{pseudo}\" + '\"></span>')")

    conv_titre = driver.find_element(by=By.ID, value="conv_titre")
    conv_titre.send_keys(topictitre)
    message = driver.find_element(by=By.CLASS_NAME, value="area-editor.js-focus-field")
    message.send_keys(topicmessage)
    poster = driver.find_element(by=By.CLASS_NAME, value="btn.btn-poster-msg.js-post-message")
    poster.click()
    finisend = False
    while finisend == False:
        if driver.current_url != "https://www.jeuxvideo.com/messages-prives/nouveau.php":
            finisend = True
        else:
            try:
                driver.find_element(by=By.CLASS_NAME, value="alert.alert-warning.alert-dismissible.fade.show")
                driver.find_element(by=By.CLASS_NAME, value="btn.btn-poster-msg.js-post-message").click()
            except NoSuchElementException:
                continue
            except ElementClickInterceptedException:
                time.sleep(1)
                continue  
        
    time.sleep(2)
    driver.get(driver.current_url)
    fermer = driver.find_element(by=By.CLASS_NAME, value="btn.btn-quitter.icon-enter")
    fermer.click()
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    del pseudos
    del posts
