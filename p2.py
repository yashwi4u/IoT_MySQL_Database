import urllib3
import json
from tkinter import *
from tkinter import messagebox

def popo():
    l=e1.get()
    n=e2.get()
    baseURL = "https://yashaswi-iot.000webhostapp.com/iot/get_home.php"
    http = urllib3.PoolManager()
    r=http.request('GET',baseURL)
    data = r.data.decode('utf-8')
    data = json.loads(data)
    i=len(data)+1
    w = http.request("GET","https://yashaswi-iot.000webhostapp.com/iot/update_home.php?Sr="+str(i)+"&username="+l+"&password="+n+")
    w.close()
    messagebox.showinfo(title=)



http=urllib3.PoolManager()

w.close()
