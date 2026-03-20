import network
import time

SSID = "brisa-4274129"  # Substitua pelo nome da sua rede WiFi
PASSWORD = "1wk7z2rg"  # Substitua pela senha do seu WiFi

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Conectando ao WiFi...")

while not wifi.isconnected():
    time.sleep(1)

print("Conectado:", wifi.ifconfig())