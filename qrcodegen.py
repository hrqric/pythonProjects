import qrcode

data = input('Digite uma URL para transformar em QRCODE: \n')

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img.save('C:/Users/cricardo/OneDrive - Chemyunion Ltda/Área de Trabalho/Projetos/0.2. Projetos Python/resources/qrcode/meuqrcode1.png')