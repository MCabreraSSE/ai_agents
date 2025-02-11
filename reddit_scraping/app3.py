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
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
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
        return text

# Función para generar resúmenes (usando OpenAI o sumy)
def summarize_content(post):
    """
    Genera un resumen del post y sus comentarios.
    """
    # Resumen del post
    post_content = post.selftext
    post_summary = summarize_with_openai(post_content)  # O usar summarize_text

    # Resumen de los comentarios
    comments = post.comments.list()
    comments_text = " ".join([comment.body for comment in comments])
    comments_summary = summarize_with_openai(comments_text)  # O usar summarize_text

    return post_summary, comments_summary

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

        # Botón para generar resumen
        if st.button(f"Generar resumen del post y comentarios", key=post.id):
            post_summary, comments_summary = summarize_content(post)
            st.subheader("Resumen del post:")
            st.write(post_summary)
            st.subheader("Resumen de los comentarios:")
            st.write(comments_summary)

        st.write("-" * 40)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()