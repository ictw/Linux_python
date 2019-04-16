# -*-coding:utf-8-*-
import tesserocr
from PIL import Image

IMAGE_LOCATION = r'/home/suofeiya/Downloads/checkcode.jpg'


def demo1():
    image_url = 'http://my.cnki.net/elibregister/CheckCode.aspx'

    image = Image.open(IMAGE_LOCATION)
    image.show()
    image_text = tesserocr.image_to_text(image)
    print(image_text)
    # 不推荐用此方法，识别度较低
    # print(tesserocr.file_to_text(IMAGE_LOCATION))


# 对验证码进行二值化和灰度处理
def demo():
    image = Image.open(IMAGE_LOCATION)
    image.show()
    # image = image.convert('L')
    # image.show()
    # image = image.convert('1')
    # image.show()
    image = image.convert('L')
    threshold = 150
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show()


if __name__ == '__main__':
    demo()
