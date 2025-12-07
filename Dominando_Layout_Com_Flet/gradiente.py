import flet as ft
import math

def main(page: ft.Page):
    containers = [
      ft.Container(
          expand=True,
          gradient=ft.LinearGradient(
              begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
              colors=[ft.Colors.CYAN, ft.Colors.BLUE, ft.Colors.PURPLE],
                stops=[0.0, 0.3, 1.00],
                rotation=math.radians(270),
          )
      ),
      ft.Container(
          expand=True,
          gradient=ft.RadialGradient(
              colors=[ft.Colors.AMBER, ft.Colors.DEEP_ORANGE,  ft.Colors.PINK],
                stops=[0.0, 0.5, 1.00],
                center=ft.Alignment(x=-0.5, y=-0.5),
                radius=0.8
          )
      ),
        ft.Container(
            expand=True,
            gradient=ft.SweepGradient(
                colors=[ft.Colors.RED, ft.Colors.BLACK, ft.Colors.PINK],
                    stops=[0.0, 0.5, 1.00],
                    center=ft.Alignment(x=0.0, y=0.0),
                   rotation=math.radians(45),
            )
        ),
    ]

    page.add(*containers)

ft.app(target=main)