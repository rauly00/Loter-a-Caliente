import flet as ft
import random
import asyncio

def main(page: ft.Page):
    page.title = "La Bola Caliente"
    page.bgcolor = "#111111"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    historial = []
    contador = {}

    titulo = ft.Text(
        "🔥 LA BOLA CALIENTE 🔥",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#FFD700"
    )

    estado = ft.Text("Listo para jugar", color="white")

    bola = ft.Container(
        content=ft.Text(
            "00",
            size=55,
            weight=ft.FontWeight.BOLD,
            color="white"
        ),
        width=170,
        height=170,
        alignment=ft.alignment.center,
        bgcolor="#FF0000",
        border_radius=100,
        shadow=ft.BoxShadow(
            blur_radius=25,
            color="#FF0000",
            spread_radius=5
        )
    )

    historial_lista = ft.Column()
    calientes_lista = ft.Column()

    sonido = ft.Audio(src="sonido.mp3")
    page.overlay.append(sonido)

    def actualizar_historial():
        historial_lista.controls.clear()
        for n in reversed(historial[-10:]):
            historial_lista.controls.append(
                ft.Text(f"🎯 {str(n).zfill(2)}", color="white")
            )

    def actualizar_calientes():
        calientes_lista.controls.clear()
        top = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:5]
        for n, veces in top:
            calientes_lista.controls.append(
                ft.Text(f"🔥 {str(n).zfill(2)} ({veces})", color="#FF4444")
            )

    async def generar(e):
        estado.value = "Girando..."
        page.update()

        sonido.play()

        for _ in range(25):
            bola.content.value = str(random.randint(0, 99)).zfill(2)
            page.update()
            await asyncio.sleep(0.04)

        numero = random.randint(0, 99)

        bola.content.value = str(numero).zfill(2)

        historial.append(numero)
        contador[numero] = contador.get(numero, 0) + 1

        actualizar_historial()
        actualizar_calientes()

        estado.value = "Número generado"
        page.update()

    boton = ft.ElevatedButton(
        text="🎰 GIRAR",
        on_click=generar,
        style=ft.ButtonStyle(
            bgcolor="#FFD700",
            color="black",
            padding=20
        )
    )

    page.add(
        titulo,
        bola,
        estado,
        boton,
        ft.Divider(),
        ft.Text("Historial", color="white"),
        historial_lista,
        ft.Divider(),
        ft.Text("Números Calientes", color="#FF4444"),
        calientes_lista
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
