# from datetime import date
# from flet import Text, TextField

import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    # greeting_text.value = 'Привет мир'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello {name}'
            greeting_text.color = None
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)

    icon_button = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)

    def icon_change_theme(_):
        if age.theme_mode == ft.ThemeMode.LIGHT:
            age.theme_mode = ft.ThemeMode.DARK
        else:
            age.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    
    icon_theme = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=icon_change_theme)

    page.add(greeting_text, name_input, text_button, elevated_button, icon_button, icon_theme)

ft.app(target=main, view=ft.WEB_BROWSER)
