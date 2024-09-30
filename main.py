import wifi

from secrets import SSID, PASSWORD

try:
    ip = wifi.connect(SSID, PASSWORD)

except KeyboardInterrupt:
    machine.reset()