## 🛫 Asistente de Viajes con IA
Esta aplicación de Streamlit es un Asistente de Viajes impulsado por IA que genera itinerarios de viaje personalizados utilizando OpenAI GPT-4. Automatiza el proceso de investigación, planificación y organización de tus vacaciones soñadas, permitiéndote explorar destinos emocionantes con facilidad.

### Features
- Investiga y descubre destinos de viaje, actividades y alojamientos emocionantes.
- Personaliza tu itinerario según el número de días que desees viajar.
- Utiliza el poder de GPT-4 para generar planes de viaje inteligentes y personalizados.

### How to get Started?

1. Clone the GitHub repository

```bash

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Get your OpenAI API Key

- Sign up for an [OpenAI account](https://platform.openai.com/) (or the LLM provider of your choice) and obtain your API key.

4. Get your SerpAPI Key

- Sign up for an [SerpAPI account](https://serpapi.com/) and obtain your API key.

5. Run the Streamlit App
```bash
streamlit run travel_agent.py
```

### How it Works?
El Asistente de Viajes con IA tiene dos componentes principales:
- Investigador: Es responsable de generar términos de búsqueda en función del destino del usuario y la duración del viaje, y de buscar en la web actividades y alojamientos relevantes utilizando SerpAPI.
- Planificador: Toma los resultados de la investigación y las preferencias del usuario para generar un itinerario preliminar personalizado que incluye actividades sugeridas.