import requests
import http
import wave
import struct

#Requesting random numbers ranging from 1 to 200
l = []
for i in range(1,1000):
    r1 = requests.get("https://www.random.org/integers/?num=8000&min=1&max=200&col=1&base=10&format=plain&rnd=new")
    a = r1.content
    b = a.decode("utf-8")

    s = b.split()
    s = list(map(int,s))
    l = l + s
print(l)


f = wave.open('wavfile.wav', 'w')
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(6000)
#f.setparams(2,1,2000,0, 'NONE', 'nothing')

for rand_num in l:
    f.writeframes(struct.pack('h', rand_num))


f.close()

