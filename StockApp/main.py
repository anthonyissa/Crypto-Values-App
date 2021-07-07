import requests
from bs4 import BeautifulSoup
from tkinter import *
import time
from PIL import ImageTk, Image

master = Tk()
master.title('Stock App')
master.iconbitmap('logo.ico')
master.resizable(False, False)
master.config(bg='#3b3f45')
menu = Menu(master)


def getStock(crypto: str):
    if crypto == "btc":
        c = "btcusd"
        name = "Bitcoin USD"
    elif crypto == "eth":
        c = "ethusd"
        name = "Ethereum USD"
    elif crypto == "bth":
        c = "bchusd"
        name = "Bitcoin Cash USD"
    elif crypto == "xrp":
        c = "xrpusd"
        name = "Ripple USD"
    elif crypto == "xmr":
        c = "xmrusd"
        name = "Monero USD"
    elif crypto == "ltc":
        c = "ltcusd"
        name = "Litecoin USD"

    url = f"https://www.marketwatch.com/investing/cryptocurrency/{c}"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    var_in_percents = soup.find('span', class_="change--percent--q").text
    var_in_points = soup.find('span', class_="change--point--q").text
    if var_in_points[0]!='-':
        var_in_points = "+"+var_in_points

    curr_price = soup.find('h3', class_="intraday__price").text
    last_update = soup.find('span', class_="timestamp__time").text
    curr_price = curr_price.replace('\n', ' ')

    title.config(text=name)
    points.config(text=var_in_points)
    percents.config(text=var_in_percents)
    price.config(text=curr_price)
    update.config(text=last_update)
    b = Button(master, relief=FLAT, text="REFRESH", font=("Calibri bold", 15))
    b.grid(row=4, padx=100, pady=5)
    b.config(command=lambda:getStock(crypto))




stockbar = Menu(menu, tearoff=0)
stockbar.add_command(label="Bitcoin", command=lambda: getStock("btc"))
stockbar.add_command(label="Ethereum", command=lambda: getStock("eth"))
stockbar.add_command(label="Bitcoin Cash", command=lambda: getStock("bth"))
stockbar.add_command(label="Ripple", command=lambda: getStock("xrp"))
stockbar.add_command(label="Monero", command=lambda: getStock("xmr"))
stockbar.add_command(label="Litecoin", command=lambda: getStock("ltc"))

menu.add_cascade(label="Select Cryptocurrency", menu=stockbar)

title = Label(master, font=("Calibri bold", 20), bg='#3b3f45', fg='white')
title.grid(row=0, padx=100)

points = Label(master, font=("Calibri bold", 15), bg='#3b3f45', fg='white')
points.grid(row=1, sticky='W', padx=20)

percents = Label(master, font=("Calibri bold", 15), bg='#3b3f45', fg='white')
percents.grid(row=1, sticky='E', padx=20)

price = Label(master, font=("Calibri bold", 20), bg='#3b3f45', fg='white')
price.grid(row=2, padx=100)

update = Label(master, font=("Calibri bold", 8), bg='#3b3f45', fg='white')
update.grid(row=3, padx=100)


master.config(menu=menu)
master.mainloop()
