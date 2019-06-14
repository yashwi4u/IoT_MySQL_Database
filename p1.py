import urllib3
import json

baseURL = "https://yashaswi-iot.000webhostapp.com/iot/get_home.php"
http = urllib3.PoolManager()
r=http.request('GET',baseURL)
data = r.data.decode('utf-8')
data = json.loads(data)
p=[]
for i in range(0,len(data)):
    p.append(data[i]['username'])

print(p)
print(data[0]['username'])
