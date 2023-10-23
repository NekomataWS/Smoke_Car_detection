import requests
import sys

url = "https://api.aiforthai.in.th/lpr-v2"
payload = {'crop': '0', 'rotate': '0'}
files = {'image': open('LicensePlateCar/ToyotaLicense1.jpg', 'rb')}

head = {
    'Apikey': "5ivdOfLHPr4V8lreO3ucAYxM7xK1osuE"
}

res = requests.post( url, files=files, data=payload, headers=head)
response = res.json()
print(response[0]['lpr'])
response_text = res.text  # Get the raw response text as a string
print(response_text)