from typing import Tuple, Dict
import os
import socket
import base64
from pathlib import Path


class Get():
    

    def handle_request(self) -> Tuple[Dict[str, any], int]:
        path = Path(__file__)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        with open(f"{path.parent}/page.html", "r", encoding="utf-8") as f:
            html = f.read()
        with open(f"{path.parent.parent.parent.parent}/assets/logo.png", "rb") as f:
            icon = f.read()
        html = html.replace("##URL##", f"{s.getsockname()[0]}:{os.getenv('PORT')}")
        html = html.replace("##ICON##", base64.b64encode(icon).decode())
        return html
