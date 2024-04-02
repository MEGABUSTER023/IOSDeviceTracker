import time

from pyicloud import PyiCloudService
api = PyiCloudService('', '')
device = api.devices[1]
location = device.location()

while True:
# sleep time so we dont get flagged by ios
    time.sleep(5)
# chcek if person is close using longitude
    if 9.814251 < location['longitude'] :
        print("Far")
    else:
        print('Near')

