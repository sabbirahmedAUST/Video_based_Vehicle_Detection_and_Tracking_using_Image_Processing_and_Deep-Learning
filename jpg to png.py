from PIL import Image
import os

directory = r'E:/4.2/Vehicles/GTI_Far'
directory1 = r'E:/4.2/Vehicles/New folder'
c = 1
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".jpg"):
        fname = directory + '/' + filename
        im = Image.open(fname)
        name = directory1 + 'img' + str(c) + '.png'
        rgb_im = im.convert('RGB')
        rgb_im.save(name)
        c += 1
        print(os.path.join(directory, filename))
        continue
    else:
        continue
