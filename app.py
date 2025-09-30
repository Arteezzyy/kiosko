from flask import Flask, render_template, request, redirect, url_for
import pg8000.dbapi
import time

# Inicializa la aplicación Flask
app = Flask(__name__)

# --- Configuración de la conexión a la base de datos ---
def get_db_connection():
    """Establece la conexión con la base de datos PostgreSQL."""
    conn = pg8000.dbapi.connect(
        user="postgres",
        password="yuridaniel0310", # IMPORTANTE: ¡Recuerda poner tu contraseña aquí!
        host="localhost",
        database="restaurante_db"
    )
    return conn

# --- Rutas del Cliente ---
@app.route('/')
def kiosko():
    """Muestra el menú de productos y las promociones al cliente."""
    conn = get_db_connection()
    cur = conn.cursor()
    # Obtiene todos los productos para mostrar en el menú
    cur.execute('SELECT * FROM productos ORDER BY id;')
    productos = cur.fetchall()
    # Obtiene todas las promociones para mostrar
    cur.execute('SELECT * FROM promociones;')
    promociones = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('kiosko.html', productos=productos, promociones=promociones)

@app.route('/realizar_pedido', methods=['POST'])
def realizar_pedido():
    """Procesa un nuevo pedido enviado por el cliente desde el kiosko."""
    conn = get_db_connection()
    cur = conn.cursor()
    # Crea un número de pedido único basado en el tiempo actual
    numero_pedido = f"PEDIDO-{int(time.time())}"
    cur.execute("INSERT INTO pedidos (numero_pedido) VALUES (%s) RETURNING id", [numero_pedido])
    pedido_id = cur.fetchone()[0]

    # Revisa el formulario para encontrar los productos y cantidades pedidas
    for key, value in request.form.items():
        if key.startswith('cantidad_') and int(value) > 0:
            producto_id = key.split('_')[1]
            cantidad_pedida = int(value)
            # Descuenta la cantidad pedida del inventario (US Nº30)
            cur.execute(
                "UPDATE insumos SET cantidad = cantidad - %s WHERE nombre_producto = (SELECT nombre FROM productos WHERE id = %s)",
                [cantidad_pedida, producto_id]
            )

    conn.commit() # Guarda todos los cambios en la base de datos
    cur.close()
    conn.close()
    # Redirige al cliente a la página para ver el estado de su pedido (US Nº28)
    return redirect(url_for('ver_pedido', pedido_id=pedido_id))

@app.route('/pedido/<int:pedido_id>')
def ver_pedido(pedido_id):
    """Muestra el estado de un pedido específico al cliente."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pedidos WHERE id = %s", [pedido_id])
    pedido = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('pedido.html', pedido=pedido)


# --- Rutas del Administrador ---
@app.route('/admin')
def panel_admin():
    """Muestra el panel de administración con el inventario y los pedidos."""
    conn = get_db_connection()
    cur = conn.cursor()
    # Obtiene el estado del inventario para mostrar las alertas (US Nº30)
    cur.execute("SELECT * FROM insumos ORDER BY nombre_producto")
    insumos = cur.fetchall()
    # Obtiene la lista de pedidos para gestionar (US Nº28)
    cur.execute("SELECT * FROM pedidos ORDER BY fecha DESC")
    pedidos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin.html', insumos=insumos, pedidos=pedidos)

@app.route('/admin/reabastecer/<int:insumo_id>', methods=['POST'])
def reabastecer(insumo_id):
    """Actualiza la cantidad de un insumo en el inventario."""
    nueva_cantidad = request.form['nueva_cantidad']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE insumos SET cantidad = %s WHERE id = %s", [nueva_cantidad, insumo_id])
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('panel_admin'))

@app.route('/admin/actualizar_estado/<int:pedido_id>', methods=['POST'])
def actualizar_estado(pedido_id):
    """Actualiza el estado de un pedido (ej. 'En camino', 'Entregado')."""
    nuevo_estado = request.form['nuevo_estado']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE pedidos SET estado = %s WHERE id = %s", [nuevo_estado, pedido_id])
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('panel_admin'))


# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)