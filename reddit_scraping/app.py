import praw
from googletrans import Translator
import streamlit as st
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de PRAW para Reddit
def setup_reddit():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),  # Obtiene el client_id desde .env
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),  # Obtiene el client_secret desde .env
        user_agent=os.getenv("REDDIT_USER_AGENT")  # Obtiene el user_agent desde .env
    )
    return reddit

# Función para traducir texto
def translate_text(text, dest_language='es'):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        st.error(f"Error al traducir: {e}")
        return text  # Devuelve el texto original si hay un error

# Función principal de la aplicación
def main():
    # Título de la aplicación
    st.title("Posts de r/AI_Agents traducidos al español")

    # Configurar PRAW
    reddit = setup_reddit()

    # Obtener los posts más recientes del subreddit r/AI_Agents
    subreddit = reddit.subreddit("AI_Agents")
    posts = subreddit.new(limit=10)  # Limita a 10 posts para evitar sobrecarga

    # Mostrar cada post traducido
    for post in posts:
        # Traducir el título y el contenido
        translated_title = translate_text(post.title)
        translated_content = translate_text(post.selftext)

        # Mostrar en la aplicación Streamlit
        st.header(translated_title)
        st.write(translated_content)
        st.write(f"**Autor:** {post.author}")
        st.write(f"**Fecha:** {post.created_utc}")
        st.write(f"**Número de comentarios:** {post.num_comments}")
        st.write("-" * 40)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()