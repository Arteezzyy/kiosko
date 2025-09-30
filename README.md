Proyecto Kiosko de Autoservicio - Resultado del Primer Sprint
Contexto del Proyecto
Este repositorio contiene el resultado del Primer Sprint de desarrollo para un sistema de gestión de pedidos de un restaurante. El objetivo principal de este sprint fue implementar las historias de usuario (US) más críticas del taskboard inicial para construir un Producto Mínimo Viable (MVP) funcional.

La aplicación web fue desarrollada utilizando Python con el framework Flask y una base de datos PostgreSQL.

🎯 Objetivo del Sprint
El objetivo de este primer sprint fue: "Establecer la funcionalidad base del sistema, permitiendo a los clientes realizar pedidos desde un kiosko y a los administradores gestionar el inventario y el estado de dichos pedidos de forma centralizada."

✅ Funcionalidades Completadas en este Sprint
Se implementaron las siguientes historias de usuario, cubriendo el flujo principal desde el pedido hasta la gestión:

US Nº26 - Pedido en el local (autoservicio):

[x] Visualización del menú completo.

[x] Selección de productos y cantidades.

[x] Generación de un número de orden único al confirmar.

US Nº28 - Seguimiento de pedido:

[x] Página de estado para que el cliente consulte su pedido.

[x] El administrador puede actualizar el estado del pedido ("En preparación", "En camino", "Entregado").

US Nº29 - Promociones personalizadas (Versión Simplificada):

[x] Muestra de promociones generales en la página principal para todos los clientes.

US Nº30 - Gestión de inventario:

[x] Descuento automático del inventario al realizar un pedido.

[x] Panel de administración con alertas visuales para productos con bajo stock.

[x] Funcionalidad para que el administrador pueda reabastecer el inventario.

📋 Backlog y Próximos Pasos (Futuros Sprints)
Las siguientes funcionalidades fueron intencionalmente dejadas en el backlog para ser abordadas en futuros sprints, tal como se definió en el "Taskboard Inicial":

US Nº27 - Pedido en línea (pick-up): Implementación de la aplicación móvil.

Integración con pasarelas de pago.

Implementación de notificaciones push.

Sistema de calificación y reseñas de pedidos.

Generación de reportes de ventas.

Gestión avanzada de usuarios y permisos.

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

Abre la Query Tool y ejecuta los scripts SQL para crear las tablas e insertar los datos de ejemplo.

6. Configurar la Conexión:

Abre el archivo app.py y en la función get_db_connection() reemplaza "tu_contraseña" con tu contraseña real de PostgreSQL.

7. Ejecutar la aplicación:

flask --app app run

La aplicación estará disponible en http://127.0.0.1:5000.

📖 Uso de la Aplicación
Vista del Cliente (Kiosko): Accede a http://127.0.0.1:5000/

Panel de Administración: Accede a http://127.0.0.1:5000/admin

👥 Autores
AYAVIRI QUISPE YURI DANIEL -202002508@est.umss.edu- Desarrollo del proyecto - @Arteezzyy

REYES CORANI WILMER -202001835@est.umss.edu- Colaborador - @Wilmer740

Proyecto realizado para la materia SISTEMAS DE INFORMACIÓN II - UNIVERSIDAD MAYOR DE SAN SIMÓN - 2025
DOCENTE: ING. FLORES SOLIZ JUAN MARCELO
