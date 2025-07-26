from rich.console import Console
from PIL import Image, ImageDraw
import qrcode

from config import PageText

# * Creation of class objects
pagetxt = PageText()
console = Console()

class QRCode:
    def __init__(self):
        self.img_qr = None  # * Initialize the attribute for storing the QR code

    def addCorners(self, im, rad):
        # * Ringes the angles of the image
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        
        im.putalpha(alpha)
        return im

    def qrSettings(self):
        # * Generates the basic QR code
        self.qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )

        path = console.input("[bold cyan]Enter the link (or press Enter to escape): [/]")
        self.qr.add_data(path)
        self.qr.make(fit=True)

        self.img_qr = self.qr.make_image(fill_color="black", back_color="white").convert('RGBA')
        self.img_qr = self.addCorners(self.img_qr, rad=60)

    def generate(self):
        # * The main generation method of the QR code
        pagetxt.titleQRGen()

        self.qrSettings()
        output_path = "QRCode.png"
        self.img_qr.save(output_path)
        console.print(f"[bold green]QR code successfully saved as {output_path}[/]")

        return output_path