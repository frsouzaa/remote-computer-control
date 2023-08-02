from typing import Tuple, Dict, Any
import mouse
import pyautogui
import json


class Control():
    

    def handle_request(self, input: Any) -> Tuple[Dict[str, any], int]:
        input = json.loads(input)
        print(input)
        if input.get("oper") == "move":
            try:
                mouse.move(input.get("data").get("x") * 8, input.get("data").get("y") * 8, absolute=False)
                return {"msg": "Sucesso"}, 200
            except Exception as e:
                return {"msg": "Erro"}, 500
        
        if input.get("oper") == "click":
            try:
                pyautogui.click()
                return {"msg": "Sucesso"}, 200
            except Exception as e:
                return {"msg": "Erro"}, 500
