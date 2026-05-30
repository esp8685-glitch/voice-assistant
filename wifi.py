import network
import time
from config import WIFI_SSID, WIFI_PASS

def connect():

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        return wlan

    wlan.connect(WIFI_SSID, WIFI_PASS)

    timeout = 20

    while timeout:

        if wlan.isconnected():
            return wlan

        timeout -= 1
        time.sleep(1)

    raise Exception("WiFi failed")