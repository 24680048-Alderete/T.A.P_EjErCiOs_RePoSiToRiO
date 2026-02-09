# T.A.P_EjErCiOs_RePoSiToRiO
## Calculadora 📟🐍
Desarrollo de una interfaz de calculadora utilizando el framework Flet para Python. Este documento describe el proceso de configuración del entorno de desarrollo y la implementación inicial de la interfaz.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
### 
> [!CAUTION]
>   Requisitos **Python🐍 3.10** o anterioes.
>
> Git Bash.
> 
> Pues checar tu versión de Python usando `python --doctor`.
> 
Para el uso de la interfaz de la calcualdora tendremos que crear un entorno virtual con la ayuda `Git Bash`, generaremos una carpeta de la siguiente manera:

```bash
mkdir Calculadora
cd Calculadora
```
A continuación, crea y activa el entorno virtual:
```bash
py -m venv .venv
source .venv/Scrips/activate
```
## Instalar Flet
Para instalar Flet y agregarlo a las dependencias del proyecto, haga lo siguiente desde Gti Bash:
```bash
pip install 'flet[all]'
```
## Verificación De Instalación
Para asegurarnos de que `Flet` se haya instalado correctamente, podemos verificar su versión usando  `--doctor` comando:
```bash
flet doctor
```
Despues de crear la dependencia aislada de Flet, se abre Visual Studio Code en la carpeta que creamos previamente donde ahi esta importado Flet.
Inicialmente, se generara la interfaz donde se mostrara la calculadora:
```bash
import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20
```
Aqui se definiran los valores del ancho y alto que tendra la ventana emergente y su titulo que mostrara, en este caso sera el titulo sera `"Calculadora TAP"` y la distancia que tendran nuestros botones con la ventana.   
Esta sección implementa el área de visualización principal donde se muestran los números y resultados durante la interacción con la calculadora:
```bash
   # 1. Definición del componente de texto
display_text = ft.Text("0", color=ft.Colors.WHITE, size=30)

# 2. Creación del contenedor del display
display = ft.Container(
    content=display_text,
    bgcolor=ft.Colors.BLACK12,
    border_radius=8,
    alignment=ft.alignment.Alignment(1, 0),
    padding=10,
    width=210,
    height=70,
)
```
En este módulo se construye un panel interactivo compuesto por una pantalla (display) y botones de control.
1. Configuración Inicial: Se define la variable que contendrá el texto a mostrar, junto con sus atributos tipográficos.
2. Construcción de la Pantalla: Se instancia el componente display, configurando su geometría (ancho, alto), paleta de colores y se le asigna el texto inicial.
3. Lógica de Interacción: Se programan los botones. Cada uno tiene un manejador de eventos (event listener) que, al hacer clic, calcula o asigna un nuevo valor y actualiza dinámicamente el contenido del display con dicho resultado.
```bash
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
```
Esta sección implementa la funcionalidad interactiva de los botones, gestionando eventos, procesamiento de datos y actualización de la interfaz.
1. Obtención del Valor:
   Se extrae el valor asociado al botón desde e.control.data. Este valor fue previamente asignado a la propiedad data de cada botón durante su creación.
2. Depuración (Debug):
   La línea print permite monitorear en la terminal qué botón fue presionado, facilitando el desarrollo y la verificación del comportamiento esperado.
3. Estructura Condicional:
   Caso Especial "AC" (All Clear): Reinicia completamente el contenido del display, estableciendo su valor a "0".
   Casos Numéricos (1, 2, 3): Añade el dígito correspondiente al final del valor actual en el display, permitiendo la construcción de números de varios dígitos.
4. Actualización de la Interfaz:
   page.update() es fundamental para aplicar los cambios realizados en display_text.value y reflejarlos visualmente en la pantalla del usuario. Sin esta llamada, los cambios no serían visibles.
En esta sección se implementa el sistema de disposición de botones utilizando un componente `GridView`, que organiza los botones en una cuadrícula para crear el teclado de la calculadora.
```bash
# Configuración del GridView para organización de botones
  ft.GridView(
    runs_count=2,        # Define dos columnas
    spacing=10,          # Espacio horizontal entre elementos
    run_spacing=10,      # Espacio vertical entre filas
    width=300,           # Ancho fijo (coincide con el display)
    height=500,          # Alto fijo para control de dimensiones
    expand=False         # Evita expansión automática
)
```

