import socket
import qrcode
import PySimpleGUI as sg
import threading
import base64
import io
import os


class QRCodeDisplay():

    def show(self):
        url: str = self.get_url()
        qr: str = self.get_qr(url)
        thread = threading.Thread(target=self.display, args=(url, qr), name=f'Thread QR code')
        thread.start()
    

    def display(self, url: str, qr: str):
        sg.theme("DarkBlack1")
        layout = [
            [sg.Text("To access the control either enter the following URL on your browser or read the QR code.", size=(
                40, None), justification="center", font=("Arial", 14))],
            [sg.Text(url, size=(40, None),
                        justification="center", font=("Arial", 15))],
            [sg.Image(qr, expand_x=True, expand_y=True)],
        ]
        window = sg.Window(
            'Champignon', layout, icon=f"{os.getcwd()}/src/assets/logo.png", size=(450, 450), element_justification='c')
        window.read()


    def get_url(self) -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return f"http://{s.getsockname()[0]}:{os.getenv('PORT')}/champignon"


    def get_qr(self, url: str) -> str:
        img = qrcode.make(url, border=1)
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue())
