from typing import Tuple, Dict
import os
import socket


class Get():
    

    def handle_request(self) -> Tuple[Dict[str, any], int]:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/page.html", "r", encoding='utf-8') as f:
            content = f.read()
        content = content.replace("##URL##", f"{s.getsockname()[0]}:{os.getenv('PORT')}")
        return content
