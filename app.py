from flask import Flask
from flask_cors import CORS
from src.views.views_list import View_List
from src.utils.qr_code_view import QRCode
from src.ws_views.control.control import Control
from flask_sock import Sock
from dotenv import load_dotenv
from os import getenv


class App():
    app: Flask = Flask(__name__)
    sock: Sock = Sock(app)

    
    def __init__(self) -> None:
        CORS(self.app)
        self.cadastrar_rotas()
        self.run_App()
    

    def cadastrar_rotas(self):
        for view in View_List().list:
            self.app.add_url_rule(view.rota, view_func=view.as_view(view.name))
        @self.sock.route('/control')
        def control(sock):
            c = Control()
            while True:
                res = c.handle_request(sock.receive())
                sock.send(res)


    def run_App(self)->None:
        self.app.run(host='0.0.0.0', port=getenv("PORT"), debug=False)


if __name__ == "__main__":
    load_dotenv()
    QRCode().show(getenv("PORT"))
    App()