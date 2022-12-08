# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap_if.config(essid='TA_ESP32', authmode=2, password='12345678')
# sta_if = network.WLAN(network.STA_IF)
# sta_if.active(True)
# sta_if.connect('Gary\u2019s iPhone', "00000000")
import webrepl
webrepl.start()
