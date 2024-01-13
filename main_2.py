#programa para ayudarte al registro de ahorro
#savings challenge
import flet as ft

def main(page: ft.Page):
    ## Inicializar la ventana
    page.window_width = 720
    page.window_height = 1280
    page.window_resizable = False
    page.padding = 0
    page.margin = 0
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    colum_general = ft.Column(
        spacing=0, 
        controls=[
            header,
            center,
            bottom,
        ]
    )
    contenedor = ft.Container(
        width = 720, 
        height = 1280, 
        bgcolor=ft.colors.RED, 
        alignment=ft.alignment.top_center
    )
    main_container = 
    page.add(

        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)