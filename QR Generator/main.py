import qrcode
from PIL import Image
import random
import string

#This Line Of Code Is For Picking Random Name To Our QR Code
qrName = ''.join(random.choices(string.ascii_lowercase, k=6))

#In This We Decided Structure Of Qr Code
qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
        )

print("Enter the subject to create the QR code")
subject = input()
qr.add_data(subject)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save(f"{qrName}.png")