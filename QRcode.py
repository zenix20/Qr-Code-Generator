import qrcode

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 20,
                   border = 2)

qr.add_data("www.linkedin.com/in/zainab-qureshi-43731a2a6")
qr.make(fit = True)

img = qr.make_image(fill_color= "brown", back_color = "pink")
img.save("Qrcode.png")