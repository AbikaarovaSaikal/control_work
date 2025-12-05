import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text('История приветствий:')

    favorite_list = []
    favorite_text = ft.Text('Избранные имена: ')

    time_list = []
    morning_text = ft.Text('Утренние приветствия:')
    evening_text = ft.Text('Вечерние приветствия:')


    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            now = datetime.now()
            time_now = now.strftime("%Y:%m:%d - %H:%M:%S:")
            greeting_text.value = f'{time_now}: Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'История приветствий: \n' + '\n'.join(greeting_history)
            time_list.append((name, now.hour))
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def favorite_name(_):
        if greeting_text.value.startswith("Hello "):
            name = greeting_text.value.replace("Hello ", "").strip()
            favorite_list.append(name)
        favorite_text.value = 'Избранные имена: \n' + '\n'.join(favorite_list)
        page.update()
    favorite_button = ft.IconButton(icon=ft.Icons.HEART_BROKEN_SHARP, on_click=favorite_name)

    def morning_name(_):
        filtered = [f"{name} (утром)" for name, hour in time_list if hour <= 12]
        morning_text.value = "Утренние приветствия:\n" + "\n".join(filtered)
        page.update()
    morning_button = ft.IconButton(icon=ft.Icons.SUNNY, on_click=morning_name)

    def evening_name(_):
        filtered = [f"{name} (вечером)" for name, hour in time_list if hour > 12]
        evening_text.value = "Вечерние приветствия:\n" + "\n".join(filtered)
        page.update()
    evening_button = ft.IconButton(icon=ft.Icons.NIGHT_SHELTER, on_click=evening_name)

    page.add(greeting_text, ft.Row([name_input, elevated_button, clear_button, favorite_button]), history_text, favorite_text, morning_button, morning_text, evening_button, evening_text)

ft.app(target=main)