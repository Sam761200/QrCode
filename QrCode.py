import qrcode

# Entrer l'URL ou le lien que vous souhaitez convertir en code QR
url = input("Entrez l'URL ou le lien à convertir en code QR : ")

# Créer l'objet QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Ajouter les données dans l'objet QR code
qr.add_data(url)
qr.make(fit=True)

# Créer l'image du code QR
img = qr.make_image(fill='black', back_color='white')

# Enregistrer l'image du code QR dans un fichier
img.save('codeQR.png')

print("Le code QR a été créé avec succès !")
