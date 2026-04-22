import flet as ft
import random

def main(page: ft.Page):

    page.title = "La Bola Caliente"
    page.window_width = 400
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.DARK
    page.assets_dir = "assets"

    # =====================
    # ESTADO
    # =====================
    numeros = list(range(1, 100))
    girando = False

    # =====================
    # UI
    # =====================

    fondo = ft.Image(
        src="fondo.jpg",
        fit=ft.ImageFit.COVER,
        expand=True
    )

    bola = ft.Image(
        src="bola.gif",
        width=200,
        height=200
    )

    resultado = ft.Text(
        "Presiona para girar",
        size=22,
        weight=ft.FontWeight.BOLD,
        color="white"
    )

    sonido = ft.Audio(
        src="sonido.mp3"
    )

    page.overlay.append(sonido)

    # =====================
    # LOGICA SIN BLOQUEO
    # =====================

    def finalizar_giro():
        nonlocal girando

        numero = random.choice(numeros)
        resultado.value = f"🎉 Número ganador: {numero}"
        girando = False
        page.update()

    def girar(e):
        nonlocal girando

        if girando:
            return  # evita doble clic

        girando = True
        resultado.value = "🎰 Girando..."
        page.update()

        sonido.play()

        # simulación de giro sin congelar la app
        page.timer(2, lambda _: finalizar_giro())

    # =====================
    # BOTON
    # =====================

    boton = ft.ElevatedButton(
        text="GIRAR BOLA",
        on_click=girar
    )

    # =====================
    # UI
    # =====================

    page.add(
        ft.Stack([
            fondo,
            ft.Column(
                [
                    ft.Container(height=60),
                    bola,
                    resultado,
                    boton
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ])
    )

ft.app(target=main)            )

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
