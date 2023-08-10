from typing import Tuple, Dict, Any
import mouse
import pyautogui
import json
import keyboard


class Control():
    

    def handle_request(self, input: Any) -> Tuple[Dict[str, any], int]:
        input = json.loads(input)
        oper: Dict[str, any] = input.get("oper")
        data: Dict[str, any] = input.get("data")
        if oper == "move":
            try:
                mouse.move(data.get("x") * 4, data.get("y") * 4, absolute=False)
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
        
        if oper == "click":
            try:
                pyautogui.click(button="right" if data.get("side") == "r" else "left")
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
        
        if oper == "mouse_down":
            try:
                pyautogui.mouseDown()
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
            
        if oper == "mouse_up":
            try:
                pyautogui.mouseUp()
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}

        if oper == "scroll":
            try:
                pyautogui.scroll(-1 if data.get("y") > 0 else 1)
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
            
        if oper == "key":
            try:
                keyboard.press_and_release(data.get("key"))
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
        
        