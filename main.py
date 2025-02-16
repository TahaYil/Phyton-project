from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup
import smtplib
import time


url = "https://www.amazon.com.tr/Apple-13-inch-MacBook-Air-MGN63TU/dp/B08NGQDBWX/ref=asc_df_B08NGQDBWX/?tag=trshpngglede-21&linkCode=df0&hvadid=510229854367&hvpos=&hvnetw=g&hvrand=12318295865311039950&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012785&hvtargid=pla-1176897723066&psc=1&mcid=dee344f03e6f38c99f82bb3a70f09471"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"}

def sendEmail(sender,reciver,pwd,title,url) :
    try :

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(sender,pwd)
        subject = title + " İstediğin fiyata düştüü!!"
        body = "Bu linkten gidebilirsin ==>" + url
        #mailContent = f"to : {reciver} \n from : {sender} \n Subject : {subject} \n\n {body}"


        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = reciver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        server.send_message(msg)
        print("Mail iletildi!!!")
    except smtplib.SMTPException as e :
        print(e)
    finally:
        server.quit()
def checkPrice(url,headers) :
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,"html.parser")
    title = soup.find(id="productTitle").get_text().strip()

    print(title)

    span=soup.find(class_="a-price-whole").get_text()
    span = span.strip().replace(",","")
    price = float(span)
    print(price)
    if (price<35.000) :
        sender = "***"
        reciver = "***"
        pwd = "***"
        sendEmail(sender,reciver,pwd,title,url)





while(1) :

    checkPrice(url,headers)
    time.sleep(60*1)
