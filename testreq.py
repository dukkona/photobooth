import logging
import requests

from PIL import Image




# im = Image.open("/home/ddm/photobooth/screenshots/pastel_2.png") 
# 
# _auth = ("ddm", config.get('UploadWebdav', 'password'))
# 
# url = "www.dukkon.com/wedding/upload"
# print('Uploading picture as %s', url)
# 
# r = requests.post(url, data=picture.getbuffer(), auth=self._auth)
# 
# with RefererSession() as session:
#     r = requests.post('https://www.dukkon.com/setpin',headers=headers,data=payload, allow_redirects=True)
#     print(r.status_code)

headers = {'User-Agent': 'Mozilla/5.0'}




s = requests.session()
url_login = "https://www.dukkon.com/setpin"

payload = {
    "pin":"1994"
}

headers={"Content-Type":"text", "pin": "1994"}


req1 = s.get(url_login, headers=headers)
print(req1.status_code)
print(s.cookies)



# Now to make sure you do not get the "Access denied", use the same session variable for the request.

# req2 = s.get("https://www.dukkon.com/wedding/gallery")
# print(req2.status_code)


payload={}

files=[('file',('test.png', open('/home/ddm/photobooth/meghivo.PNG','rb'), 'image/png'))]

img =  open('/home/ddm/photobooth/meghivo.PNG','rb')

# response = s.request("POST", "https://www.dukkon.com/wedding/upload", headers=headers, data=img, headers={"Content-Type": "image/png"})

files = {'file': open('/home/ddm/photobooth/meghivo.PNG', 'rb')}
response = s.request("POST", "https://www.dukkon.com/wedding/upload_pb", files=files)
print(response.content)
print(response.status_code)