Proyecto Kiosko de Autoservicio para Restaurante
Este es un proyecto universitario que simula un sistema de gestión de pedidos para un restaurante. La aplicación web fue desarrollada utilizando Python con el framework Flask y una base de datos PostgreSQL para manejar la persistencia de datos.

El sistema permite a los clientes realizar pedidos a través de una interfaz de kiosko, mientras que los administradores pueden gestionar el inventario y el estado de los pedidos desde un panel de control.

🚀 Funcionalidades Implementadas
El proyecto implementa las funcionalidades clave descritas en las siguientes historias de usuario:

US Nº26 - Pedido en el local (autoservicio):

[x] Visualización del menú completo desde la base de datos.

[x] Selección de la cantidad de productos a ordenar.

[x] Confirmación del pedido y generación de un número de orden único.

US Nº28 - Seguimiento de pedido:

[x] Página de confirmación para el cliente donde puede ver el estado actual de su pedido.

[x] El administrador puede actualizar el estado del pedido ("En preparación", "En camino", "Entregado").

US Nº29 - Promociones personalizadas:

[x] Muestra de promociones generales en la página principal para todos los clientes.

US Nº30 - Gestión de inventario:

[x] Descuento automático del inventario al realizar un pedido.

[x] Panel de administración que muestra el stock actual.

[x] Alertas visuales para productos con inventario bajo (por debajo del umbral mínimo).

[x] Funcionalidad para que el administrador pueda reabastecer el inventario.

🛠️ Tecnologías Utilizadas
Backend: Python 3

Framework Web: Flask

Base de Datos: PostgreSQL

Conector de BD: pg8000

Frontend: HTML5 y CSS3 con plantillas Jinja2

⚙️ Instalación y Configuración Local
Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1. Prerrequisitos:

Tener Python 3 instalado.

Tener PostgreSQL instalado.

2. Clonar el repositorio:

git clone [https://github.com/Arteezzyy/kiosko.git](https://github.com/Arteezzyy/kiosko.git)
cd kiosko

3. Crear y activar un entorno virtual:

# En Windows
python -m venv venv
.\venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

4. Instalar las dependencias:

pip install -r requirements.txt

5. Configurar la Base de Datos:

Abre pgAdmin 4 y crea una nueva base de datos llamada restaurante_db.

Abre la herramienta de consultas (Query Tool) y ejecuta los scripts SQL necesarios para crear las tablas (productos, pedidos, insumos, promociones) e insertar los datos de ejemplo.

6. Configurar la Conexión:

Abre el archivo app.py.

Busca la función get_db_connection() y reemplaza "tu_contraseña" con tu contraseña real de PostgreSQL.

7. Ejecutar la aplicación:

flask --app app run

La aplicación estará disponible en http://127.0.0.1:5000.

📖 Uso de la Aplicación
Vista del Cliente (Kiosko): Accede a http://127.0.0.1:5000/ para ver el menú y realizar un pedido.

Panel de Administración: Accede a http://127.0.0.1:5000/admin para gestionar el inventario y los pedidos.

👥 Autores
AYAVIRI QUISPE YURI DANIEL - Desarrollo del proyecto - @Arteezzyy

CORANI REYES WILMER - Colaborador - @Wilmer740

Proyecto realizado para la materia SISTEMAS DE INFORMACIÓN II - UNIVERSIDAD MAYOR DE SAN SIMÓN - 2025
