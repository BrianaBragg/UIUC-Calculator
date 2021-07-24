from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('./CalculatorApp.kv')
Window.size = (350, 550)

# ^^This creates the window size dimensions of the app. Left = width, right=height


class CalculatorWidget(Widget):
    def clear(self):

        # ^^def " " is what you put in once you go to kv and implement what it does when you click the  button.

        self.ids.input_box.text = '0'

        # ^^id identifies the 0 text in kv

    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "PurDON'T do that" in prev_number:
            prev_number = ''

            # ^^this stops it from typing more numbers into the final evaluated answer

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

            # ^^code allows for multiple numbers to show on top

    def signs(self, sing):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sing}"

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]

        # ^^removing last character of the previous number

        self.ids.input_box.text = prev_number

        # ^^now we're showing the updated previous number on text input

    def results(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)

            # ^^eval evaluates equation for us. bottom code shows result of calculation on top of calculator

            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "PurDON'T do that"

    def positive_negative(self):

        # ^^function for -/+ sign

        prev_number = self.ids.input_box.text

        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"

    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number)

        if ("+" in prev_number or "-" in prev_number or "/" in prev_number or "*" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number

        elif "." in prev_number:
            pass

        else:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
