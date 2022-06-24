#kursy walut v2
from tkinter import *
from tkinter import messagebox
import json
import requests

#API URL
url='http://api.nbp.pl/api/exchangerates/rates/a/'

root = Tk()
root.title('Kantor') #nazwa aplikacji
root.geometry('900x600+300+100') #rozmiar aplikacji

label = Label(root,text='Kursy wymiany walut!',font=20,fg='white', bg='#3d3a3e',pady=15,justify=LEFT)
label.pack(fill='x')
label2 = Label(root, text="Wpisz wartość (PLN)",font=16,pady=10)
label2.pack()
e = Entry(root, width=20,font=20,bd=2,justify=LEFT)
e.pack(side='top', padx=10)

def checkinput(inputValue):
    try:
        if(float(inputValue)>0):
            return True
    except:
        return False 

def APIconnection(url): 
    try:
        requests.get(url)
        return True
    except:
        return False

def currency_rate():
    inputValue=e.get()
    if(checkinput(inputValue)): #sprawdzanie poprawności wartości inputa
        cantor=Tk()
        cantor.title('Wymiana walut')
        value = float(e.get())
        if(w1.get()==1): #sprawdzanie czy checkbox jest zaznaczony
            newURL=url+'USD'
            if(APIconnection(newURL)): #sprawdzenie poprawności połączenia z serwerem NBP
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Dolar amerykański\nKurs: {rates}zł\nWartość wymiany: "+str(exchange)+" USD",bg="#833ab4",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w2.get()==1):
            newURL=url+'GBP'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Funt brytyjski\nKurs: {rates}zł\nWartość wymiany: " + str(exchange)+" GBP",bg="#be2e9b",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w3.get()==1):
            newURL=url+'EUR'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Euro\nKurs: {rates}zł\nWartość wymiany: "+str(exchange) +" EUR",bg="#c52a62",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w4.get()==1):
            newURL=url+'CHF'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Frank szwajcarski\nKurs: {rates}zł\nWartość wymiany: "+str(exchange) +" CHF",bg="#fd1d1d",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w5.get()==1):
            newURL=url+'RUB'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Rubel\nKurs: {rates}zł\nWartość wymiany: "+str(exchange) +" RUB",bg="#fd4327",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w6.get()==1):
            newURL=url+'JPY'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Jen japoński\nKurs: {rates}zł\nWartość wymiany: "+str(exchange) +" JPY",bg="#b36f51",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w7.get()==1):
            newURL=url+'SEK'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Korona Szwedzka\nKurs: {rates}zł\nWartość wymiany: "+str(exchange) +" SEK",bg="#5da281",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w8.get()==1):
            newURL=url+'CAD'
            if(APIconnection(newURL)):
                response = requests.get(newURL).json()
                rates=response['rates'][0]['mid']
                exchange = round(value *(1/rates),2)
                label = Label(cantor,text=f"Dolar kanadyjski\nKurs: {rates}zł\nWartość wymiany: "+str(exchange) +" CAD",bg="#2ac19e",pady=40,padx=5)
                label.pack(anchor=W,side=LEFT,fill='both')
            else:
                cantor.destroy()
                messagebox.showerror('Connection Error','Brak połączenia z serwerem')
        if(w1.get()==0 and w2.get()==0 and w3.get()==0 and w4.get()==0 and w5.get()==0 and w6.get()==0 and w7.get()==0 and w8.get()==0):
            cantor.destroy()
            messagebox.showerror('Uwaga!','Waluta nie została wybrana')
    else:
        messagebox.showerror('Błąd!','Podana wartość jest błędna')

label3 = Label(root,text="► Zaznacz walutę, sprawdź jej kurs oraz wartość wymiany ◄",font=12,padx=10,pady=15)
label3.pack(side=TOP,anchor=NW,fill='x')

w1,w2,w3,w4,w5,w6,w7,w8 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

v1 = Checkbutton(root,text="Dolar amerykański",font=12,variable=w1, onvalue="1",offvalue="0",bg="#833ab4")
v1.pack(anchor=W,fill='x')
v2 = Checkbutton(root,text="Funt brytyjski",font=12,variable=w2,bg='#be2e9b')
v2.pack(anchor=W,fill='x')
v3 = Checkbutton(root,text="Euro",font=12,variable=w3,bg='#c52a62')
v3.pack(anchor=W,fill='x')
v4 = Checkbutton(root,text="Frank szwajcarski",font=12,variable=w4,bg="#fd1d1d")
v4.pack(anchor=W,fill='x')
v5 = Checkbutton(root,text="Rubel",font=12,variable=w5,bg="#fd4327")
v5.pack(anchor=W,fill='x')
v6 = Checkbutton(root,text="Jen japoński",font=12,variable=w6,bg="#b36f51")
v6.pack(anchor=W,fill='x')
v7 = Checkbutton(root,text="Korona szwedzka",font=12,variable=w7,bg='#5da281')
v7.pack(anchor=W,fill='x')
v8 = Checkbutton(root,text="Dolar kanadyjski",font=12,variable=w8,bg='#2ac19e')
v8.pack(anchor=W,fill='x')

btn = Button(root,text="Sprawdź",width=8,font=4,justify=LEFT,command=currency_rate)
btn.pack(side='top',pady=15)

root.mainloop()
