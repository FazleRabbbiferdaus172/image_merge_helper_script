from PIL import Image
import os
from crop_image import crop_windows_10, crop_ubuntu

url = "your_url"
image_name_list = os.listdir(url)
url += '/'
raw_image_list = []
raw_image_max_height = raw_image_max_widht = 0
for i_name in image_name_list:
    # im = crop_windows_10(Image.open(url+i_name))
    im = Image.open(url+i_name)
    raw_image_list.append(im)
    current_image_size = raw_image_list[-1].size
    raw_image_max_widht = max(raw_image_max_widht, current_image_size[0])
    raw_image_max_height = max(raw_image_max_height, current_image_size[1])

for i in range(len(raw_image_list)):
    raw_image_list[i] = raw_image_list[i].resize((raw_image_max_widht, raw_image_max_height))

merged_image = Image.new('RGB',(raw_image_max_widht, len(raw_image_list)*raw_image_max_height), (250,250,250))

for ind,image in enumerate(raw_image_list):
    merged_image.paste(image,(0,ind*raw_image_max_height))
merged_image.save("you_new_image_name","JPEG")