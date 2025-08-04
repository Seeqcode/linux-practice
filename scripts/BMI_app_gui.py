from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BMICalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.weight_input = TextInput(hint_text="Enter weight (kg)", input_filter='float', multiline=False)
        self.height_input = TextInput(hint_text="Enter height (m)", input_filter='float', multiline=False)
        self.result_label = Label(text="Your BMI will appear here")

        calc_button = Button(text="Calculate BMI")
        calc_button.bind(on_press=self.calculate_bmi)

        self.add_widget(self.weight_input)
        self.add_widget(self.height_input)
        self.add_widget(calc_button)
        self.add_widget(self.result_label)

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height = float(self.height_input.text)
            if weight <= 0 or height <= 0.4:
                self.result_label.text = "Please enter valid positive values."
                return

            bmi = weight / (height ** 2)
            if bmi < 18.5:
                status = "Underweight"
                advice = "Try to gain some healthy weight"
            elif bmi <= 24.9:
                status = "Normal"
                advice = "You're doing well!"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
                advice = "Exercise and healthy eating are key"
            else:
                status = "Obese"
                advice = "Talk to a doctor"

            self.result_label.text = f"BMI: {bmi:.2f} ({status})\nAdvice: {advice}"
        except ValueError:
            self.result_label.text = "Please enter numbers only."


class BMIApp(App):
    def build(self):
        return BMICalculator()


if __name__ == '__main__':
    BMIApp().run()
