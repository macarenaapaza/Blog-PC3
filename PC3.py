# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1 (no instalar)

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos'] , 
        icons=['0-circle','1-circle', '2-circle'], menu_icon="Flower1", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
#selected = option_menu(
   # menu_title="Selecciona una sección: ", 
    #options=['Inicio', 'Experiencia', 'Gráficos'], 
   # icons=['person-heart', 'globe-americas', 'pencil-square'], 
    #menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Mi mundo</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("fotomaca.jpeg", caption='Maca', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Hola!! Bienvenido a mi blog, como puedes ver me llamo macarena 
    pero amo cuando me dicen maca o maquita. 
    Soy una estudiente de periodismo, con mucha curiosidad por el mundo
    Soy Peruana y Limeña aunque por mi familia tengo raices arequipeñas.
    Si me preguntaran ¿Qué te gusta de tu carrera?, creo que diria la libertad
    que me da para descubrir, probar e intentar muchas cosas.
    En el futuro me gustaria viajar mucho y tomar fotos de muchas coss
    En mi tiempo libre disfruto estar con mis amigos o familia, jugar
    con mi perrito (chimmy <3), o ultimamente disfruto leer un libro. 
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia ':
    st.markdown("<h1 style='text-align: center;'>Mi nuevo descubrimiento 💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    La verdad que nunca habia escuchado acera de python o 
    los pograma que se usan para programar, asi que al inicio
    me senti mas perdida que nunca, aun que no puedo negar que
    me parecia super novedoso todo. La programación me ha enseñado
    que realmente se puede hacer MUCHO y para cada ocasión, aparte 
    que lo puedes usar como una herramienta a tu favor para organizarte,
    apoyarte, etc. Por ejemplo, lo que me gusta de programar es que en base
    a lo que voy a crear puedo personalizarlo segun mis colores favoritos, mis fonts,
    etc, ya que hay muchas librerias que me lo permiten.
    En el futuro, creo que me gustaria combinar mis trabajos de investigación periodistica 
    con la programación para tener analisis mas dinamicos y certeros.
    Sin duda creo que la todo lo aprendido acerca de programación no solo podre usarlo en mi
    vida personal, sino que tambien para ordenar datos, lugares o etc que tenga que exponer acerca
    de una noticia periodistica. 
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Sabes que es un string? o una lista? 🧐")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/14vpeZgm5JuNGzwovOQmzyfVTxssTYNml/view?usp=sharing"
        )
    # Agrega una breve descripción del video.
    st.markdown("""
         En este video te enseñare ejemplos y definiciones acerca de la diferencia entre los strings y las listas,
        asi como comprender inmutabilidad vs. mutabilidad, aprender la modificación de datos y ver como convertir cadenas de listas
        para el análisis de información 
    """)

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("Bucles for and while? que es eso?!🤯")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1yPv9XYkR0A5uquRnbZbNubbzKbev-quS/view?usp=sharing"
        )
    # Agrega una breve descripción del video.
    st.markdown("""
        Tranquii, al inicio tambien no tenia idea pero aqui te enseño un poco acerca de sus diferencias, 
        como aprendas a iterar sobre las listas usando (for) y como implementar condiciones de parada dinamica 
        usando (while). 
    """) 

elif opciones == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Resultados</h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Lenguas aisladas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Aquí debe ir una breve interpretación de tu gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "imagen 1.png",
                width=800
            )

    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa 1: Distribución geográfica")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa1.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
