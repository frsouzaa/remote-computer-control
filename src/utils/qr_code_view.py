import socket
import qrcode
import PySimpleGUI as sg
import threading
import base64
import io


class QRCode():


    def show(self, port: str):
        def display():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            img = qrcode.make(f'http://{s.getsockname()[0]}:{port}/champignon')
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue())
            layout = [
                [sg.Image(img_str),],
            ]
            window = sg.Window('Champignon', layout)
            window.read()
        thread = threading.Thread(target=display, name=f'Thread QR code')
        thread.start()
