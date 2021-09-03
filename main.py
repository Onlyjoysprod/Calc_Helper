from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        self.text_input_history = []
        self.reset_state = 0
        self.step_count = 0
        self.box_data = [[]]
        self.box_count = 0
        self.box_params = ['общий', 'пустой', '2 кат.', 'нестанд.', 'отходы', 'общий']
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=40
        )
        self.input_text = TextInput(
            multiline=False, readonly=True, halign="right", font_size=40
        )
        main_layout.add_widget(self.solution)
        main_layout.add_widget(self.input_text)
        buttons = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [".", "0", "C"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        r_layout = BoxLayout()

        self.box_info = Label(text=f'Ящик {self.box_count + 1}\n'
                                   f'{self.box_params[0]}', halign="center")
        r_layout.add_widget(self.box_info)

        equals_button = Button(
            text="Назад", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_back)
        next_button = Button(
            text="Далее", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        next_button.bind(on_press=self.on_next_btn)
        r_layout.add_widget(equals_button)
        r_layout.add_widget(next_button)
        main_layout.add_widget(r_layout)

        return main_layout

    def on_next_btn(self, instance):
        if self.input_text.text != "" and self.input_text.text != "Подтв. сброс":
            if self.step_count < 5:
                self.step_count += 1
                if self.step_count == 1 and self.box_count > 0:
                    self.box_data[self.box_count].append(self.input_text.text)
                    self.input_text.text = self.box_data[0][1]
                else:
                    self.box_data[self.box_count].append(self.input_text.text)

                self.text_input_history.append(self.input_text.text)
                self.input_text.text = ""
                self.box_info.text = f'Ящик {self.box_count + 1}\n' \
                                     f'{self.box_params[self.step_count]}'
            if self.step_count >= 5:
                self.box_count += 1
                self.box_data.append([])
                self.box_info.text = f'Ящик {self.box_count + 1}\n' \
                                     f'{self.box_params[self.step_count]}'
                self.step_count = 0
            MainApp.solution(self)

            print(self.box_data)
            print(self.text_input_history)
            print(self.step_count)
            print(self.box_count)

    def on_back(self, instance):
        if len(self.text_input_history) > 0:
            self.input_text.text = self.text_input_history[-1]

        if len(self.box_data[0]) > 0:
            self.step_count -= 1

            if self.step_count < 0:
                self.step_count = 4
                self.box_count -= 1
                self.box_data.pop()
                if self.box_count < 0:
                    self.box_count = 0
            self.text_input_history.pop()
            (self.box_data[self.box_count]).pop()
            self.box_info.text = f'Ящик {self.box_count + 1}\n' \
                                 f'{self.box_params[self.step_count]}'

            print(self.box_data)
            print(self.text_input_history)
            print(self.step_count)
            print(self.box_count)
        MainApp.solution(self)

    def on_button_press(self, instance):
        current = self.input_text.text
        button_text = instance.text

        if button_text == "C":
            if self.input_text.text != "" and self.input_text.text != "Подтв. сброс":
                self.input_text.text = ""
            else:
                self.reset_state += 1
                print(self.reset_state)
                if self.reset_state == 1:
                    self.input_text.text = "Подтв. сброс"
            if self.reset_state == 2:
                self.reset_state = 0
                self.input_text.text = ""
                self.solution.text = ""
                self.step_count = 0
                self.box_count = 0
                self.box_data = [[]]
                self.text_input_history = []
                self.box_info.text = f'Ящик {self.box_count + 1}\n' \
                                     f'{self.box_params[self.step_count]}'
        else:
            if self.input_text.text != "Подтв. сброс":
                new_text = current + button_text
                if new_text == '0':
                    self.input_text.text = ""
                elif new_text == '.':
                    self.input_text.text = "0."
                else:
                    self.input_text.text = new_text
                MainApp.solution(self)
            else:
                self.reset_state = 0
                new_text = button_text
                if new_text == '0':
                    self.input_text.text = ""
                elif new_text == '.':
                    self.input_text.text = "0."
                else:
                    self.input_text.text = new_text

    def solution(self, *args):
        boxes = self.box_data
        product_weights = 0
        waste_weights = 0
        for i in range(self.box_count):
            product_weights += eval(f'{boxes[i][0]}-{boxes[i][1]}')
            waste_weights += eval(f'{boxes[i][2]}+{boxes[i][3]}+{boxes[i][4]}')
            print(product_weights)
            print(waste_weights)
            self.solution.text = f'{product_weights} -- {waste_weights} -- {round(waste_weights / product_weights * 100, 1)}%'


if __name__ == "__main__":
    app = MainApp()
    app.run()
