import flet as ft
import random

def main(page: ft.Page):
    page.title = "La Bola Caliente"
    page.bgcolor = "#121212"
    page.scroll = "auto"
    page.horizontal_alignment = "center"

    titulo = ft.Text(
        "🔥 La Bola Caliente 🔥",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="white"
    )

    resultado = ft.Text(
        "Presiona el botón",
        size=20,
        color="white"
    )

    historial = []
    historial_lista = ft.Column()

    def generar_numero(e):
        numero = random.randint(0, 99)

        resultado.value = f"Número: {numero}"
        historial.append(numero)

        historial_lista.controls.clear()

        for n in reversed(historial[-10:]):
            historial_lista.controls.append(
                ft.Text(f"🎯 {n}", color="white")
            )

        page.update()

    boton = ft.ElevatedButton(
        text="GENERAR",
        on_click=generar_numero
    )

    page.add(
        titulo,
        ft.Divider(),
        resultado,
        boton,
        ft.Text("Historial:", color="white"),
        historial_lista
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
