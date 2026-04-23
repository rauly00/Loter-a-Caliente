import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "La Bola Caliente"
    page.bgcolor = "#0f0f0f"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = "auto"

    historial = []
    contador = {}

    # 🎯 Título
    titulo = ft.Text(
        "🔥 LA BOLA CALIENTE 🔥",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#FFD700"
    )

    # 🎰 Bola animada
    bola = ft.Container(
        content=ft.Text(
            "00",
            size=50,
            weight=ft.FontWeight.BOLD,
            color="white"
        ),
        width=150,
        height=150,
        alignment=ft.alignment.center,
        bgcolor="#FF0000",
        border_radius=100,
        animate_rotation=ft.animation.Animation(300, "easeInOut"),
    )

    rotacion = 0

    estado = ft.Text("Listo para jugar", color="white")

    historial_lista = ft.Column(spacing=5)
    calientes_lista = ft.Column(spacing=5)

    # 📊 Historial
    def actualizar_historial():
        historial_lista.controls.clear()
        for n in reversed(historial[-10:]):
            historial_lista.controls.append(
                ft.Text(f"🎯 {n}", color="white")
            )

    # 🔥 Números calientes
    def actualizar_calientes():
        calientes_lista.controls.clear()
        top = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:5]
        for n, veces in top:
            calientes_lista.controls.append(
                ft.Text(f"🔥 {n} ({veces})", color="#FF4444")
            )

    # 🎲 Generar número con animación
    def generar(e):
        nonlocal rotacion

        estado.value = "Girando..."
        page.update()

        # Giro rápido
        for _ in range(15):
            rotacion += 0.5
            bola.rotate = rotacion
            bola.content.value = str(random.randint(0, 99)).zfill(2)
            page.update()
            time.sleep(0.05)

        # Desaceleración
        for _ in range(10):
            rotacion += 0.2
            bola.rotate = rotacion
            bola.content.value = str(random.randint(0, 99)).zfill(2)
            page.update()
            time.sleep(0.08)

        # Resultado final
        numero = random.randint(0, 99)
        bola.content.value = str(numero).zfill(2)

        historial.append(numero)
        contador[numero] = contador.get(numero, 0) + 1

        actualizar_historial()
        actualizar_calientes()

        estado.value = "Número generado"
        page.update()

    # 🔘 Botón
    boton = ft.ElevatedButton(
        text="GIRAR",
        on_click=generar,
        style=ft.ButtonStyle(
            bgcolor="#FFD700",
            color="black",
            padding=15
        )
    )

    # 📐 Layout
    layout = ft.Column(
        [
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
        ],
        horizontal_alignment="center"
    )

    page.add(layout)

# 🚀 IMPORTANTE PARA ANDROID
ft.app(target=main, view=ft.AppView.FLET_APP)        weight=ft.FontWeight.BOLD,
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
