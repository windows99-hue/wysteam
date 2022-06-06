import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

def random_str(length=4):
    """ 随机字符串 默认长度 4

    :param length: 默认长度 4
    :return:
    """
    return ''.join(random.sample(string.ascii_letters, length))

def random_color(s=1, e=255):
    """ 随机 RGB 颜色

    :param s:  起始值, 0-255
    :param e:  结束时, 0-255
    :return:  (r, g, b)
    """
    return random.randint(s, e), random.randint(s, e), random.randint(s, e)

def veri_code(length=4, width=160, height=40, size=28):
    """ 生成验证码图片

    :param length:  验证码字符串长度
    :param width:  图片宽度
    :param height:  图片高度
    :param size:  字体大小
    :return:  (验证码图片, 验证码字符串)
    """
    
    # 创建Image对象
    image = Image.new('RGB', (width, height), (255, 255, 255))
    
    # 创建Font对象
    file = os.path.dirname(os.path.abspath(__file__))
    font = ImageFont.truetype(f'{file}/captcha_font.ttf', size)
    
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    
    # 随机颜色填充每个像素
    for x in range(0, width, 2):
        for y in range(height):
            draw.point((x, y), fill=random_color(64, 255))
            
    # 验证码
    code = random_str(length)
    
    # 随机颜色验证码写到图片上
    for t in range(length):
        draw.text((40 * t + 5, 5), code[t], font=font, fill=random_color(32, 127))
        
    # 模糊滤镜
    image = image.filter(ImageFilter.BLUR)
    return image, code

if __name__ == '__main__':
    img, code = veri_code()
    with open('test.png', 'wb') as f:
        img.save(f)
        
