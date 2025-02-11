## 💻 Agente de IA para Web Scraping
Esta aplicación de Streamlit te permite realizar web scraping en un sitio web utilizando la API de OpenAI y la biblioteca scrapegraphai. Simplemente proporciona tu clave de API de OpenAI, ingresa la URL del sitio web que deseas scrapear y especifica qué quieres que el agente de IA extraiga del sitio web.

### Features
- Scrapea cualquier sitio web proporcionando la URL
- Utiliza los modelos de lenguaje de OpenAI (GPT-3.5-turbo o GPT-4) para un scraping inteligente
- Personaliza la tarea de scraping especificando qué quieres que el agente de IA extraiga

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/MCabreraSSE/ai_agents.git
cd ai_agents/web_scrapping_ai_agent/
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Get your OpenAI API Key

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.

4. Run the Streamlit App
```bash
streamlit run ai_scrapper.py
```

### How it Works?

- La aplicación solicita que ingreses tu clave de API de OpenAI, que se utiliza para autenticar y acceder a los modelos de lenguaje de OpenAI.
- seleccionar el modelo de lenguaje deseado (GPT-3.5-turbo o GPT-4) para la tarea de scraping.
- Ingresar la URL del sitio web que deseas scrapear en el campo de texto proporcionado.
- Especificar qué quieres que el agente de IA extraiga del sitio web ingresando un prompt de usuario.
- La aplicación crea un objeto SmartScraperGraph utilizando la URL proporcionada, el prompt del usuario y la configuración de OpenAI.
- El objeto SmartScraperGraph scrapea el sitio web y extrae la información solicitada utilizando el modelo de lenguaje especificado.
- Los resultados del scraping se muestran en la aplicación para que los veas.