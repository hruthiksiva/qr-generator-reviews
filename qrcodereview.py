import qrcode

# Replace with your actual Place ID
place_id = "ChIJZ_0d_jRvqTsR6QzU3sb3ewo"

# Construct the Google review URL
url = f"https://search.google.com/local/writereview?placeid={place_id}"

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
