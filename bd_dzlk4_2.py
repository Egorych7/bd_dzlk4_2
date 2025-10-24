# user_profile.py
# Import necessary modules
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp


class ProfileLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [dp(25), dp(20)]  # Увеличил отступы по бокам
        self.spacing = dp(20)  # Увеличил интервал между элементами
        self.create_profile_interface()

    def create_profile_interface(self):
        # Set window size
        Window.size = (420, 750)  # Немного увеличил окно

        # Profile Image
        profile_image_path = r"C:\Users\vem16\Downloads\Telegram Desktop\photo_2025-10-25_01-42-46.jpg"
        if os.path.exists(profile_image_path):
            profile_image = Image(
                source=profile_image_path,
                size_hint=(None, None),
                size=(dp(130), dp(130)),  # Увеличил фото
                pos_hint={'center_x': 0.5}
            )
            self.add_widget(profile_image)
        else:
            error_label = Label(
                text="Фото профиля не найдено",
                size_hint_y=None,
                height=dp(40)
            )
            self.add_widget(error_label)

        # User Name
        user_label = Label(
            text="Егор Вольников",
            font_size=dp(26),  # Увеличил шрифт
            bold=True,
            size_hint_y=None,
            height=dp(45),  # Увеличил высоту
            pos_hint={'center_x': 0.5}
        )
        self.add_widget(user_label)

        # Biography Section
        bio_title = Label(
            text="Биография",
            font_size=dp(20),  # Увеличил шрифт
            bold=True,
            size_hint_y=None,
            height=dp(35)  # Увеличил высоту
        )
        self.add_widget(bio_title)

        bio_text = Label(
            text="Я студент 2 курса Московского Авиационного Института. Кафедра 317 - 'Инноватика.'",
            font_size=dp(15),  # Увеличил шрифт
            text_size=(Window.width - dp(50), None),  # Увеличил ширину текста
            size_hint_y=None,
            height=dp(90),  # Увеличил высоту
            halign='left',
            valign='top'
        )
        bio_text.bind(size=bio_text.setter('text_size'))
        self.add_widget(bio_text)

        # Skills Section
        skills_title = Label(
            text="Умения",
            font_size=dp(20),  # Увеличил шрифт
            bold=True,
            size_hint_y=None,
            height=dp(35)  # Увеличил высоту
        )
        self.add_widget(skills_title)

        skills_content = Label(
            text="• Python\n• MySQL\n• Git и системы контроля версий",
            font_size=dp(14),  # Увеличил шрифт
            text_size=(Window.width - dp(50), None),  # Увеличил ширину текста
            size_hint_y=None,
            height=dp(80),  # Уменьшил высоту (меньше текста)
            halign='left',
            valign='top'
        )
        skills_content.bind(size=skills_content.setter('text_size'))
        self.add_widget(skills_content)

        # Experience Section
        experience_title = Label(
            text="Опыт работы",
            font_size=dp(20),  # Увеличил шрифт
            bold=True,
            size_hint_y=None,
            height=dp(35)  # Увеличил высоту
        )
        self.add_widget(experience_title)

        experience_content = Label(
            text="Подсобный рабочий\nиюнь 2023 - август 2023\n\nФриланс проекты\nавгуст 2024 - декабрь 2024",
            font_size=dp(14),  # Увеличил шрифт
            text_size=(Window.width - dp(50), None),  # Увеличил ширину текста
            size_hint_y=None,
            height=dp(120),  # Уменьшил высоту (меньше текста)
            halign='left',
            valign='top'
        )
        experience_content.bind(size=experience_content.setter('text_size'))
        self.add_widget(experience_content)


class UserProfileApp(App):
    def build(self):
        self.title = "Профиль пользователя"
        return ProfileLayout()

    def on_start(self):
        # Set window position
        Window.top = 80
        Window.left = 100


if __name__ == '__main__':
    UserProfileApp().run()