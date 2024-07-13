import qrcode

link = 'https://github.com/mgibbons989'

qr = qrcode.QRCode(version = 1, box_size = 7, border = 2)
qr.add_data(link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('MyGithub.png')
