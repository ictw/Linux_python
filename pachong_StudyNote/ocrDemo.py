import pytesseract
from PIL import Image
from urllib import request

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1553598750&di=bab619a12b0d0fc2dbe86cb7b8df7f1e&src=http://image.bubuko.com/info/201804/20180407143214979378.png'

request.urlretrieve(url, './Other/test.png')

image = Image.open('./Other/test.png')
# image = Image.open('/home/suofeiya/NEW_SPACE/ocr_test/ocr_test01.png')

print(pytesseract.image_to_string(image).strip())
