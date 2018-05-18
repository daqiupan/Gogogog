import requests
import re

# s=requests.session()
# url='http://192.168.1.21:8120/mock/36/api/user'
# headers={"Content-Type":"application/json"}
# data="phone=15708466072&pwd=zh12345678"
# r=s.post(url,headers=headers,data=data)
# print(r.text)

s=requests.session()
url='http://192.168.1.21:8120/mock/36/api/user/login'
headers={"Content-Type":"application/json"}
data=""
"""data="phone=15708466072&pwd=zh12345678"""
r=s.post(url,headers=headers,data=data)
c=r.text

r=re.findall("reg\'(.*)\'/>",c)
print(r)