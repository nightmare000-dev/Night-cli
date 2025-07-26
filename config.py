from pyfiglet import Figlet
from rich.console import Console

console = Console()

class PageText:
    def __init__(self):
        self.console = Console()
    
    # * Text and its font for the main page
    def pageMain(self, font="larry3d", text="NIGHT", position="center", color="[magenta]"):
        mainFiglet = Figlet(font=font)
        ascii_text = mainFiglet.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)

    # * Main page invitation color
    def inviteMain(self, color="[magenta]"):
        self.invMainColor = color + "[bold]"
        
    # * Text and its font for a page with tools
    def pageTools(self, font="slant", text="NIGHT TOOLS", position="center", color="[magenta]"):
        toolsFiglet = Figlet(font=font)
        ascii_text = toolsFiglet.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)

    # * Tools page invitation color
    def inviteTools(self, color="[magenta]"):
        self.invToolsColor = color + "[bold]"

    # * Text and font for the Settings page
    def pageSettings(self, font="slant", text="NIGHT SETTINGS", position="center", color="[magenta]"):
        settingsFiglet = Figlet(font=font)
        ascii_text = settingsFiglet.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)

    # * Settings page invitation color
    def inviteSettings(self, color="[magenta]"):
        self.invSettingsColor = color + "[bold]"

    # * Translator title
    def titleTranslator(self, font="slant", text="NIGHT TRANSLATOR", position="center", color="[cyan]"):
        translatorFiglet = Figlet(font=font)
        ascii_text = translatorFiglet.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)

    # * Password generator title
    def titlePassGen(self, font="slant", text="NIGHT PASSWORD GENERATOR", position="center", color="[cyan]"):
        passGenFiglet = Figlet(font=font)
        ascii_text = passGenFiglet.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)

    # * QR Code Generation title
    def titleQRGen(self, font="slant", text="NIGHT QRCODE GENERATOR", position="center", color="[cyan]"):
        qrGenFiglet = Figlet(font=font)
        ascii_text = qrGenFiglet.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)

    # * Main Config
    def titleMainConfig(self, font="slant", text="NIGHT QRCODE GENERATOR", position="center", color="[cyan]"):
        MainConfig = Figlet(font=font)
        ascii_text = MainConfig.renderText(text)

        self.console.print(f"{color}{ascii_text}[/]", justify=position)