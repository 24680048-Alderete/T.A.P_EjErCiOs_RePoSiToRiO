import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

   # 1. Definición del componente de texto
display_text = ft.Text("0", color=ft.Colors.WHITE, size=30)

# 2. Creación del contenedor del display
display = ft.Container(
    content=display_text,
    bgcolor=ft.Colors.BLACK12,
    border_radius=15,
    alignment=ft.alignment.Alignment(1, 0),
    padding=10,
    width=210,
    height=70,
)
    def button_clicked(e: ft.ControlEvent):
    # 1. Captura del valor del botón
    value = e.control.data
    print(f"Button clicked with data = {value}")
    
    # 2. Lógica condicional según el botón presionado
    if value == "AC":
        # Limpieza completa: restablece el display a "0"
        display_text.value = "0"
    elif value == "1":
        # Concatenación del dígito "1" al valor actual
        display_text.value += "1"
    elif value == "2":
        # Concatenación del dígito "2" al valor actual
        display_text.value += "2"
    elif value == "3":
        # Concatenación del dígito "3" al valor actual
        display_text.value += "3"
    
    # 3. Actualización de la interfaz
    page.update()
        # Configuración del GridView para organización de botones
  ft.GridView(
    runs_count=2,        # Define dos columnas
    spacing=10,          # Espacio horizontal entre elementos
    run_spacing=10,      # Espacio vertical entre filas
    width=300,           # Ancho fijo (coincide con el display)
    height=500,          # Alto fijo para control de dimensiones
    expand=False         # Evita expansión automática
)
# Botón número 1
grid.controls.append(
    ft.Container(
        ft.Button("1", data="1", on_click=button_clicked),
        height=25, 
        bgcolor=ft.Colors.PURPLE_100, 
        border_radius=8
    )
)

# Botón número 2
grid.controls.append(
    ft.Container(
        ft.Button("2", data="2", on_click=button_clicked),
        height=25,
        bgcolor=ft.Colors.LIGHT_BLUE_100, 
        border_radius=8
    )
)

# Botón número 3
grid.controls.append(
    ft.Container(
        ft.Button("3", data="3", on_click=button_clicked),
        height=25, 
        bgcolor=ft.Colors.AMBER_100,
        border_radius=8
    )
)

# Botón AC (All Clear)
grid.controls.append(
    ft.Container(
        ft.Button("AC", data="AC", on_click=button_clicked),
        height=25,
        bgcolor=ft.Colors.GREEN_100,
        border_radius=8
    )
)
# 1. Creación del Layout Principal
layout_principal = ft.Column(
    controls=[
        display,  # Componente superior: área de visualización
        grid      # Componente inferior: rejilla de botones
    ],
    tight=True  # Configuración de espaciado compacto
)

# 2. Adición del Layout a la Página
page.add(layout_principal)

# 3. Actualización Inicial de la Interfaz
page.update()

# 4. Inicio de la Aplicación
ft.app(target=main)
