from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

class ArtificialPancreasApp(App):
    def build(self):
        self.title = "Artificial Pancreas Simulator"
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Light gray background

        # Glucose level slider
        self.glucose_label = Label(text="Glucose Level (mg/dL)", font_size=18, color=(0, 0, 0, 1))
        self.glucose_slider = Slider(min=50, max=300, value=100)
        self.glucose_value_label = Label(text=f"{int(self.glucose_slider.value)} mg/dL", font_size=16, color=(0, 0, 0, 1))
        self.glucose_slider.bind(value=self.update_glucose_value)
        self.layout.add_widget(self.glucose_label)
        self.layout.add_widget(self.glucose_slider)
        self.layout.add_widget(self.glucose_value_label)

        # Age input
        self.age_label = Label(text="Age", font_size=18, color=(0, 0, 0, 1))
        self.age_input = TextInput(hint_text="Enter your age", font_size=16)
        self.layout.add_widget(self.age_label)
        self.layout.add_widget(self.age_input)

        # Gender checkboxes
        self.gender_layout = BoxLayout(orientation="horizontal", spacing=10)
        self.gender_label = Label(text="Gender", font_size=18, color=(0, 0, 0, 1))
        self.male_checkbox = CheckBox(active=False, group="gender", size_hint=(None, None), size=(30, 30), color=(0, 0, 0, 1))
        self.male_label = Label(text="Male", font_size=16, color=(0, 0, 0, 1))
        self.female_checkbox = CheckBox(active=False, group="gender", size_hint=(None, None), size=(30, 30), color=(0, 0, 0, 1))
        self.female_label = Label(text="Female", font_size=16, color=(0, 0, 0, 1))
        self.gender_layout.add_widget(self.gender_label)
        self.gender_layout.add_widget(self.male_checkbox)
        self.gender_layout.add_widget(self.male_label)
        self.gender_layout.add_widget(self.female_checkbox)
        self.gender_layout.add_widget(self.female_label)
        self.layout.add_widget(self.gender_layout)

        # Insulin dosage label
        self.insulin_label = Label(text="Insulin Dosage (units): 0", font_size=18, color=(0, 0, 0, 1))
        self.layout.add_widget(self.insulin_label)

        # Calculate button
        self.calculate_button = Button(text="Calculate Insulin Dosage", font_size=16)
        self.calculate_button.bind(on_press=self.calculate_insulin)
        self.layout.add_widget(self.calculate_button)

        return self.layout

    def update_glucose_value(self, instance, value):
        self.glucose_value_label.text = f"{int(value)} mg/dL"

    def calculate_insulin(self, instance):
        glucose_level = self.glucose_slider.value
        age = self.age_input.text
        gender = "Male" if self.male_checkbox.active else "Female"

        # Modify the calculation method based on age and gender
        if age and gender:
            if int(age) < 18:
                insulin_dosage = max(0, (glucose_level - 100) / 50)
            else:
                insulin_dosage = max(0, (glucose_level - 100) / 40)
        else:
            insulin_dosage = max(0, (glucose_level - 100) / 50)

        self.insulin_label.text = f"Insulin Dosage (units): {insulin_dosage:.2f}"

if __name__ == "__main__":
    ArtificialPancreasApp().run()
