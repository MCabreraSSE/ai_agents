# Agente de IA para Scrapear y Traducir Posts de Reddit

Este proyecto es un agente de IA que scrapea posts del subreddit `r/AI_Agents`, los traduce al español y los muestra en una aplicación web local usando Streamlit.

---

## Características principales

1. **Scrapeo de Reddit**: Usa la librería PRAW para obtener los posts más recientes del subreddit `r/AI_Agents`.
2. **Traducción automática**: Traduce el título y el contenido de cada post al español usando la librería `googletrans`.
3. **Interfaz web**: Muestra los posts traducidos en una aplicación web interactiva usando Streamlit.

---

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior.
- `pip` para instalar las dependencias.

---

## Configuración

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2.  Configura las credenciales de Reddit:
    Crea una aplicación en Reddit https://www.reddit.com/prefs/apps para obtener tus credenciales (client_id, client_secret, y user_agent).
    Abre el archivo app.py y reemplaza los siguientes valores con tus credenciales:
        
        reddit = praw.Reddit
            (
            client_id="TU_CLIENT_ID",
            client_secret="TU_CLIENT_SECRET",
            user_agent="TU_USER_AGENT"
            )


## Ejecución
pip install -r requirements.txt
streamlit run app.py
