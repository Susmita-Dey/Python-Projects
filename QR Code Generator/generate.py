# install all the libraries needed
# create a function that collects the text and converts it into qr code

import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save("qrimg1.png")


url = input("Enter your url: ")
# generate_qrcode("https://bio.link/susmitadey")
generate_qrcode(url)
