import os
from PIL import Image, ImageDraw, ImageFont

def add_watermark(img_path, watermark_text):
    file_name, file_ext = os.path.splitext(img_path)
    new_img_path = file_name + "_watermark" + file_ext
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
    draw.text((0,0), watermark_text, fill=black, font=font)
    img.show()
    img.save(new_img_path)

if __name__ == '__main__':
    img_file_name = 'tenerife.jpg'
    add_watermark(img_file_name, 'watermark by python')
