from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box_params = ['общий', '2 кат.', 'нестанд.', 'отходы', 'осыпь']
        self.box_weight = TextInput(text='1', multiline=False, readonly=False, halign="center")
        self.id_box = [[['0', '0'], ['0', '1'], ['0', '2'], ['0', '3'], ['0', '4']],
                       [['1', '0'], ['1', '1'], ['1', '2'], ['1', '3'], ['1', '4']],
                       [['2', '0'], ['2', '1'], ['2', '2'], ['2', '3'], ['2', '4']],
                       [['3', '0'], ['3', '1'], ['3', '2'], ['3', '3'], ['3', '4']],
                       [['4', '0'], ['4', '1'], ['4', '2'], ['4', '3'], ['4', '4']],
                       [['5', '0'], ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4']],
                       [['6', '0'], ['6', '1'], ['6', '2'], ['6', '3'], ['6', '4']],
                       [['7', '0'], ['7', '1'], ['7', '2'], ['7', '3'], ['7', '4']],
                       [['8', '0'], ['8', '1'], ['8', '2'], ['8', '3'], ['8', '4']],
                       [['9', '0'], ['9', '1'], ['9', '2'], ['9', '3'], ['9', '4']],
                       [['10', '0'], ['10', '1'], ['10', '2'], ['10', '3'], ['10', '4']],
                       [['11', '0'], ['11', '1'], ['11', '2'], ['11', '3'], ['11', '4']],
                       [['12', '0'], ['12', '1'], ['12', '2'], ['12', '3'], ['12', '4']],
                       [['13', '0'], ['13', '1'], ['13', '2'], ['13', '3'], ['13', '4']],
                       [['14', '0'], ['14', '1'], ['14', '2'], ['14', '3'], ['14', '4']]]
        self.result_box = [['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0'],
                           ['0', '0', '0', '0', '0']]
        self.button_list = []
        self.result_inputs = []
        self.total_inputs = []

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        left = BoxLayout(orientation='vertical')
        leftGrid = GridLayout(cols=1, padding=20)
        leftGrid.bind(minimum_height=leftGrid.setter('height'))
        top_box = BoxLayout(orientation="horizontal")

        header_box = BoxLayout()
        header_box.add_widget(Label(text='', size_hint=(0.5, 1)))
        header_box.add_widget(Label(text='Вес тары'))

        for i in range(4):
            header_box.add_widget(Label(text='%'))
        leftGrid.add_widget(header_box)

        result = BoxLayout()
        self.box_weight.bind(text=self.on_text)
        self.box_weight.spec_number = 'box_weight'
        result.add_widget(Label(text='', size_hint=(0.5, 1)))
        result.add_widget(self.box_weight)

        for i in range(4):
            result_input = TextInput(text='', multiline=False, readonly=True, halign="center")
            self.result_inputs.append(result_input)
            result.add_widget(result_input)

        leftGrid.add_widget(result)

        label1 = Label(text="", size_hint=(0.5, 1))
        top_box.add_widget(label1)

        for i in range(5):
            label1 = Label(text=self.box_params[i])
            top_box.add_widget(label1)
        leftGrid.add_widget(top_box)
        for x in range(15):
            box = BoxLayout(orientation="horizontal")
            label = Label(text=str(x + 1), size_hint=(0.5, 1))
            box.add_widget(label)
            for i in range(5):
                num_input = TextInput(text='', multiline=False, readonly=False, halign="right",
                                           input_filter='float')
                num_input.spec_number = self.id_box[x][i]
                num_input.bind(text=self.on_text)
                self.button_list.append(num_input)
                box.add_widget(num_input)

            leftGrid.add_widget(box)

        self.button_list.extend(self.result_inputs)

        total_box = BoxLayout(orientation="horizontal")

        clear_btn = Button(text='C', size_hint=(0.5, 1))
        clear_btn.bind(on_press=self.clear_btn)
        total_box.add_widget(clear_btn)

        for i in range(5):
            total_input = TextInput(text='0', multiline=False, readonly=True, halign="center")
            self.total_inputs.append(total_input)
            total_box.add_widget(total_input)

        leftGrid.add_widget(total_box)
        left.add_widget(leftGrid)
        main_layout.add_widget(left)

        return main_layout

    def clear_btn(self, instance):
        print(self.button_list)
        for btn in self.button_list:
            btn.text = ''

    def on_text(self, instance, value):
        print(instance.spec_number)
        if instance.spec_number != 'box_weight':
            x, y = int(instance.spec_number[0]), int(instance.spec_number[1])
            if value != '':
                self.result_box[x][y] = value
            else:
                self.result_box[x][y] = '0'
        else:
            if value != '':
                instance.text = value
            else:
                instance.text = '0'

        product_weights = [0, 0, 0, 0, 0]

        for box in self.result_box:
            if box[0] != '0':
                product_weights[0] += eval(f'{box[0]} - {self.box_weight.text}')
            product_weights[1] += eval(f'{box[1]}')
            product_weights[2] += eval(f'{box[2]}')
            product_weights[3] += eval(f'{box[3]}')
            product_weights[4] += eval(f'{box[4]}')

        if product_weights[0] != 0:
            for i, el in enumerate(self.result_inputs):
                el.text = f'{round(product_weights[i+1] / product_weights[0] * 100, 1)}%'
                print(i)

        for i, el in enumerate(self.total_inputs):
            el.text = f'{product_weights[i]:.2f}'

        print(product_weights)


if __name__ == "__main__":
    start_app = MainApp()
    start_app.run()
