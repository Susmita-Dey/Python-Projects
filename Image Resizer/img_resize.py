# install pillow
# import pillow
# open up image we want to resize using python
# print the current size of that image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image


def resize_image(size1, size2):
    image = Image.open('logo.png')

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('resized_logo-'+str(size1)+'-'+str(size2)+'.png')


width = int(input("Enter Width of Image: "))
height = int(input("Enter Height of Image: "))
resize_image(width, height)
