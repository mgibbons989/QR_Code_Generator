import qrcode

print('Welcome to my QR code generator!')

link = input('Where do you want this qr code to lead? (Type a whole link) ')
ver = int(input('How big do you want it to be? (Type 1-40, 1 being a 21 x 21 matrix) '))
box = int(input('How many pixels should each box in the code be? '))
bord = int(input('How many boxes thick should the border be? '))

qr = qrcode.QRCode(version = ver, box_size = box, border = bord)
qr.add_data(link)
qr.make()

fill = input('What color do you want the boxes to be? ')
back = input('What color should the background be? ')

img = qr.make_image(fill_color = fill , back_color = back )
name = input('Waht do you want the image name to be? ') + '.png'
img.save(name)

print('Your QR code should be saved to your computer now!')
