import qrcode

# The URL of your Google review page
url = "https://www.google.com/maps/place/DHARANI+CARDS/@11.339303,77.7221801,16.97z/data=!3m1!5s0x3ba96f44c6aa88a9:0x23e178a87efc5d3f!4m12!1m2!2m1!1sdharani+cards!3m8!1s0x3ba96f34fe1dfd67:0xa7bf7c6ded40ce9!8m2!3d11.3391921!4d77.7281173!9m1!1b1!15sCg1kaGFyYW5pIGNhcmRzkgEbaW52aXRhdGlvbl9wcmludGluZ19zZXJ2aWNl4AEA!16s%2Fg%2F12hsfnp1w?authuser=2&entry=ttu"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("google_review_qr.png")
