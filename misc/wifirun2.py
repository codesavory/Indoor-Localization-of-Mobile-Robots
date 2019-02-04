from gi.repository import NetworkManager, NMClient

nmc = NMClient.Client.new()
devs = nmc.get_devices()

for dev in devs:
    if dev.get_device_type() == NetworkManager.DeviceType.WIFI:
        for ap in dev.get_access_points():
            print ap.get_ssid()
