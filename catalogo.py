import streamlit as st
import urllib.parse

# Configuración de la página para celulares
st.set_page_config(page_title="Mi Tienda Digital", page_icon="📱", layout="centered")

# Tu número de WhatsApp (código de país de Bolivia: 591 + tu número)
NUMERO_WHATSAPP = "5917XXXXXXX" 

st.title("🛍️ Catálogo Virtual Oruro")
st.write("Elegí tus productos y hacé tu pedido. Entrega inmediata en la ciudad.")
st.markdown("---")

# Base de datos simulada de tus productos (Podés cambiar fotos, nombres y precios)
productos = [
    {
        "id": 1,
        "nombre": "Audífonos Bluetooth Pro",
        "precio": 120,
        "descripcion": "Alta fidelidad, batería de 5 horas, ideal para estudiar o entrenar.",
        "imagen": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500"
    },
    {
        "id": 2,
        "nombre": "Cargador Carga Rápida 20W",
        "precio": 80,
        "descripcion": "Compatible con Android e iPhone. Incluye cable reforzado.",
        "imagen": "https://images.unsplash.com/photo-1619134547900-58079dfb830d?w=500"
    },
    {
        "id": 3,
        "nombre": "Soporte Ergonómico para Laptop",
        "precio": 95,
        "descripcion": "Aluminio regulable, evita el calentamiento de tu notebook.",
        "imagen": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"
    }
]

# Inicializar el carrito de compras en la sesión si no existe
if "carrito" not in st.session_state:
    st.session_state.carrito = {}

# Mostrar productos en pantalla
for prod in productos:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(prod["imagen"])
        
    with col2:
        st.subheader(prod["nombre"])
        st.write(prod["descripcion"])
        st.subheader(f"{prod['precio']} Bs.")
        
        # Botón para añadir/quitar del carrito
        id_prod = str(prod["id"])
        cant_actual = st.session_state.carrito.get(id_prod, 0)
        
        if st.button(f"Agregar al carrito", key=f"add_{id_prod}"):
            st.session_state.carrito[id_prod] = cant_actual + 1
            st.rerun()
            
    st.markdown("---")

# Sección del Carrito de Compras (Solo aparece si hay artículos)
if any(st.session_state.carrito.values()):
    st.header("🛒 Tu Pedido")
    total = 0
    resumen_pedido = "Hola! Quiero realizar el siguiente pedido:\n\n"
    
    for prod in productos:
        id_prod = str(prod["id"])
        cantidad = st.session_state.carrito.get(id_prod, 0)
        if cantidad > 0:
            subtotal = prod["precio"] * cantidad
            total += subtotal
            st.write(f"▪️ **{prod['nombre']}** (x{cantidad}) - {subtotal} Bs.")
            resumen_pedido += f"- {prod['nombre']} (x{cantidad}): {subtotal} Bs.\n"
            
    st.subheader(f"Total a Pagar: {total} Bs.")
    resumen_pedido += f"\n*Total: {total} Bs.*\n¿Me lo podés enviar?"
    
    # Botón para vaciar el carrito
    if st.button("Vaciar Carrito"):
        st.session_state.carrito = {}
        st.rerun()
        
    # Crear enlace directo a WhatsApp con el texto del pedido formateado
    texto_codificado = urllib.parse.quote(resumen_pedido)
    url_whatsapp = f"https://wa.me/{59172368411}?text={texto_codificado}"
    
    # Botón de confirmación que redirige a WhatsApp
    st.link_button("🚀 Confirmar Pedido por WhatsApp", url_whatsapp)