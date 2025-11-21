import flet as ft

def main(page: ft.Page):
    container = ft.Container(
       content=ft.Image(
            src="https://flet.dev/img/docs/controls/container/container-diagram.png",  # caminho ou URL da imagem
            # width=200,
            # height=200,
            fit=ft.ImageFit.CONTAIN
        ),
        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=ft.margin.only(top=100, left=10, right=30, bottom=10),
        border = ft.border.only(
            top = ft.BorderSide(width=15, color=ft.Colors.PINK),
            left = ft.BorderSide(width=15, color=ft.Colors.ORANGE),
            right = ft.BorderSide(width=10, color=ft.Colors.GREEN),
            bottom = ft.BorderSide(width=1, color=ft.Colors.BLUE),
        )


    )
    page.add(container)
ft.app(target=main)