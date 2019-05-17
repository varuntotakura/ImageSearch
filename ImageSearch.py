import requests
import webbrowser

filePath = 'E:/Camera/Girls/Drugs/Love.jpg'
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchU = response.headers['Location']
testUrl = fetchU.split('=')
fetchUrl = 'https://www.google.com/search?tbs='+testUrl[1]
webbrowser.open(fetchUrl)
