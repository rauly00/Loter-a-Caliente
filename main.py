import flet as ft
import random

def main(page: ft.Page):
    page.title = "La Bola Caliente"
    page.scroll = "auto"

    titulo = ft.Text(
        "🔥 La Bola Caliente 🔥",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    resultado = ft.Text(
        "Presiona el botón para generar un número",
        size=18
    )

    historial = []

    historial_lista = ft.Column()

    def generar_numero(e):
        numero = random.randint(0, 99)

        resultado.value = f"Número generado: {numero}"
        historial.append(numero)

        historial_lista.controls.clear()

        for n in reversed(historial[-10:]):
            historial_lista.controls.append(
                ft.Text(f"🎯 {n}")
            )

        page.update()

    boton = ft.ElevatedButton(
        text="Generar número",
        on_click=generar_numero
    )

    page.add(
        titulo,
        ft.Divider(),
        resultado,
        boton,
        ft.Text("Últimos números:"),
        historial_lista
    )

ft.app(target=main)
