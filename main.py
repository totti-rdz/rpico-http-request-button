import wifi
from picozero import Button
import urequests

from secrets import PASSWORD, SSID, URL

def createRequest(url):
    def request():
        print("button pressed")
        response = urequests.get(url)
        response.close()
    return request

button = Button(14)
#button2 = Button(10) # second button connected to GPIO 10

try:
    ip = wifi.connect(SSID, PASSWORD)
    button.when_pressed = createRequest(URL)

except KeyboardInterrupt:
    machine.reset()