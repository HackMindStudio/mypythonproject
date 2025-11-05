import qrcode
from PIL import Image
import datetime
import os

while True:
    data = input("Enter text or link for QR (or 'exit' to quit): ")
    if data.lower() == "exit":
        print("👋 Exiting QR Generator...")
        break

  
    if not os.path.exists("Generated_QRs"):
        os.makedirs("Generated_QRs")

 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    color = input("Enter QR color (e.g., 'black'): ") or "black"
    bg_color = input("Enter background color (e.g., 'white'): ") or "white"

    img = qr.make_image(fill_color=color, back_color=bg_color).convert("RGB")


    add_logo = input("Add logo? (y/n): ").lower()
    if add_logo == "y":
        logo_path = input("Enter logo file name (e.g., logo.png): ")
        try:
            logo = Image.open(logo_path)
            basewidth = 80
            wpercent = basewidth / float(logo.size[0])
            hsize = int((float(logo.size[1]) * float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos)
        except Exception as e:
            print(f"⚠️ Error adding logo: {e}")

    
    file_name = input("Enter file name (or press Enter for auto name): ")
    if not file_name.strip():
        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"qr_{time_stamp}.png"
    else:
        if not file_name.lower().endswith(".png"):
            file_name += ".png"

    save_path = os.path.join("Generated_QRs", file_name)
    img.save(save_path)
    print(f"✅ QR Code saved as {save_path}\n")