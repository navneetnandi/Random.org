import requests
import http

#Requesting 128 random numbers ranging from 1 to 56
r1 = requests.get("https://www.random.org/integers/?num=128&min=1&max=56&col=1&base=10&format=plain&rnd=new")

a = r1.content

#print(r1.content)

b = a.decode("utf-8")

s = b.split()
s = list(map(int, s))
print(s)
