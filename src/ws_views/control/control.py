from typing import Tuple, Dict, Any
from math import copysign
import mouse
import pyautogui
import json
import keyboard
import platform

class Control():
    def accelerate(self, value, multiplier, max_mov_value):
        min_input, max_input = 0, 10 
        min_output, max_output = 0, 5
        exponent = 2

        sign = copysign(1, value)

        input_range = max_input - min_input
        output_range = max_output - min_output

        normalized_value = (value - min_input) / input_range
        accelerated_value = normalized_value ** exponent
        mapped_value = min_output + (accelerated_value * output_range)
        mapped_value = min(mapped_value * multiplier, max_mov_value)

        mapped_value *= sign
        return mapped_value

    def handle_request(self, input: Any) -> Tuple[Dict[str, any], int]:
        input = json.loads(input)
        oper: Dict[str, any] = input.get("oper")
        data: Dict[str, any] = input.get("data")
        if oper == "move":
            try:
                x_raw_mov = data.get("x")
                y_raw_mov = data.get("y")
                final_x_mov = self.accelerate(x_raw_mov, 5, 120)
                final_y_mov = self.accelerate(y_raw_mov, 5, 120)
                mouse.move(final_x_mov, final_y_mov, absolute=False)
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
                if platform.system().upper() == "WINDOWS":
                    pyautogui.scroll(-100 if data.get("y") > 0 else 100)
                else:
                    pyautogui.scroll(-5 if data.get("y") > 0 else 5)
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
            
        if oper == "key":
            try:
                keyboard.press_and_release(data.get("key"))
                return {"status": 200, "msg": "Sucesso"}
            except Exception as e:
                return {"status": 500, "msg": "Erro"}
