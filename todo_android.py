from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from datetime import datetime, timedelta

class ToDoApp(App):
    def build(self):
        self.tasks = []

        layout = BoxLayout(orientation='vertical')

        task_label = Label(text="Task:")
        layout.add_widget(task_label)

        self.task_entry = TextInput()
        layout.add_widget(self.task_entry)

        time_label = Label(text="Time (YYYY-MM-DD HH:MM):")
        layout.add_widget(time_label)

        self.time_entry = TextInput()
        layout.add_widget(self.time_entry)

        add_button = Button(text="Add Task")
        add_button.bind(on_press=self.create_task)
        layout.add_widget(add_button)

        self.task_list = RecycleView()
        layout.add_widget(self.task_list)

        return layout

    def create_task(self, instance):
        task = self.task_entry.text
        time = self.time_entry.text

        if task and time:
            try:
                task_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
                current_time = datetime.now()

                if task_time < current_time:
                    self.show_popup("Invalid Time", "Please enter a future time for the task.")
                else:
                    self.tasks.append((task, task_time))
                    self.update_task_list()
            except ValueError:
                self.show_popup("Invalid Format", "Please enter time in the format YYYY-MM-DD HH:MM.")
        else:
            self.show_popup("Missing Information", "Please fill in both task and time fields.")

    def update_task_list(self):
        self.task_list.data = [{'text': f"{task} - {time.strftime('%Y-%m-%d %H:%M')}", 'font_size': 14} for task, time in self.tasks]

    def check_alerts(self, dt):
        current_time = datetime.now()
        for task, time in self.tasks:
            if current_time + timedelta(minutes=1) >= time >= current_time:
                self.show_popup("Task Alert", f"It's time for: {task}")

    def on_start(self):
        self.update_task_list()
        Clock.schedule_interval(self.check_alerts, 60)  # Check every minute

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    ToDoApp().run()
