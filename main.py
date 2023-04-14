from datetime import datetime
import qrcode

input_url = input('write your url to continue : ')

QR = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=15, 
    border=4,
    )

QR.add_data(input_url)
QR.make(fit=True)

img = QR.make_image(fill_color="black",back_color="white")
img.save("url_qr-code-%s.png"%datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

print(QR.data_list)