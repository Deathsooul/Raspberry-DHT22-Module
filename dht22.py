import pigpio
import DHT22
from time import sleep

pi = pigpio.pi()

dht22 = DHT22.sensor(pi, 17) 
dht22.trigger()

sleepTime = 3

def readDHT22():
    dht22.trigger()
    humidity  = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return (humidity, temp)

while True:
    humidity, temperature = readDHT22()
    print("Humidity is: " + humidity + "%")
    print("Temperature is: " + temperature + "C")
    sleep(sleepTime)