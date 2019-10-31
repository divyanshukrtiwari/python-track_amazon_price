import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Wild-Stone-Forest-Spice-Perfume/dp/B00DRDZ80O/ref=pd_sbs_194_1/257-2664271-1109830?_encoding=UTF8&pd_rd_i=B00DRDZ80O&pd_rd_r=e0b0214d-b8c6-44f0-805e-a9f63c6e6d99&pd_rd_w=uixNf&pd_rd_wg=NyMLz&pf_rd_p=fbf43daf-8fb3-47b5-9deb-ae9cce3969a9&pf_rd_r=Q33KWM543XVS9AB86JCS&psc=1&refRID=Q33KWM543XVS9AB86JCS"
headers = {"User-agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="title").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])


    if converted_price < 210 : 
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email', 'password')

    subject = 'Amazon product details'
    body = 'Yay! Price dropped \n Checkout this link https://www.amazon.in/Wild-Stone-Forest-Spice-Perfume/dp/B00DRDZ80O/ref=pd_sbs_194_1/257-2664271-1109830?_encoding=UTF8&pd_rd_i=B00DRDZ80O&pd_rd_r=e0b0214d-b8c6-44f0-805e-a9f63c6e6d99&pd_rd_w=uixNf&pd_rd_wg=NyMLz&pf_rd_p=fbf43daf-8fb3-47b5-9deb-ae9cce3969a9&pf_rd_r=Q33KWM543XVS9AB86JCS&psc=1&refRID=Q33KWM543XVS9AB86JCS'

    msg = "Subject: {}\n\n{}".format(subject, body)

    server.sendmail('from', 'to', msg)
    print('the mail has been sent.')
    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60)
