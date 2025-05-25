#QR CODE CREATE

import code 
from PIL import image 

qr = qrcode.QRcode(version = 1,
     error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size =10,
                   border =4,)

qr.add_data("https://youtube.com/")
qr.make(fit = True)
img = qr.make_image(fill_color = "black", back_color = "yellow")
img.save("lofi music.png")


