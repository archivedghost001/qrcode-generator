import qrcode
from datetime import datetime

print("Input your URL Link or texts to generate the QR Code!!")

user_input = str(input("Put your URL here: "))

QR = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15, border=4
)

QR.add_data(user_input)
QR.make(fit=True)

img = QR.make_image(fill_color="black", back_color="white")

img.save("output/result-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

print(QR.data_list)
