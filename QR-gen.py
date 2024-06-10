import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5,
)

while True:
    data = input("Please Enter the URL for the QR scan (or 'N' to quit): ")
    if data.lower() == 'n':
        print("Quitting...")
        break
    elif data:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img_name = input("Please Enter IMG Name: ")
        img.save(img_name + ".png")
        print(f"QR code saved as {img_name}.png")
        break  # Exit the loop if data is provided
    else:
        print("Please enter a valid URL or 'N' to quit.")
