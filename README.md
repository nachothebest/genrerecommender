<h1>🎬 Genre Recommender API</h1>

<p>Esta es una API REST basada en Flask que predice géneros de películas a partir de la <strong>sinopsis</strong> utilizando un modelo de machine learning entrenado previamente. El modelo emplea vectorización TF-IDF y clasificación multi-etiqueta para predecir probabilidades de cada género.</p>

<hr>

<h2>📁 Estructura del Proyecto</h2>

<pre>
├── api_genrerecommender.py       # Punto de entrada de la API Flask
├── deployment/
│   └── predict_genre.py          # Lógica de predicción de géneros
├── genrerecommender_clf.pkl      # Modelo de clasificación entrenado
├── vectorizer.pkl                # Vectorizador TF-IDF guardado
├── requirements.txt              # Dependencias del proyecto
</pre>

<hr>

<h2>🚀 Comenzando</h2>

<h3>1. Clona el repositorio</h3>
<pre><code>git clone https://github.com/nachothebest/genrerecommender.git
cd genrerecommender
</code></pre>

<h3>2. Crea y activa un entorno virtual</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate
</code></pre>

<h3>3. Instala las dependencias</h3>
<pre><code>pip install -r requirements.txt
python -m spacy download en_core_web_sm
</code></pre>

<hr>

<h2>🧠 ¿Cómo funciona?</h2>
<ul>
  <li>La API expone un endpoint <code>POST /recommend</code>.</li>
  <li>Recibe un JSON con una clave <code>plot</code> que contiene la <strong>sinopsis</strong> de la película.</li>
  <li>El texto es limpiado, lematizado, vectorizado y luego clasificado.</li>
  <li>Devuelve un diccionario con las probabilidades de cada género.</li>
</ul>

<hr>

<h2>📡 Ejemplo de Uso</h2>

<h3>Solicitud</h3>
<pre><code>
POST /recommend
Content-Type: application/json

{
  "plot": "Un joven mago asiste a una escuela de magia donde debe derrotar a un malvado hechicero."
}
</code></pre>

<h3>Respuesta</h3>
<pre><code>
{
  "result": {
    "p_Action": 0.14,
    "p_Adventure": 0.83,
    "p_Comedy": 0.02,
    "p_Drama": 0.76,
    "p_Fantasy": 0.80,
    ...
  }
}
</code></pre>

<hr>

<h2>⚙️ Ejecutar la API Localmente</h2>

<pre><code>python api_genrerecommender.py</code></pre>

<p>Una vez iniciada, la API estará disponible en:</p>
<pre><code>http://127.0.0.1:5000/recommend</code></pre>

<hr>

<h2>📦 Dependencias</h2>
<p>Estas están listadas en <code>requirements.txt</code>. Las principales son:</p>
<ul>
  <li>Flask</li>
  <li>flask-restx</li>
  <li>pandas</li>
  <li>numpy</li>
  <li>joblib</li>
  <li>spacy</li>
  <li><strong>scikit-learn</strong></li>
</ul>

<pre><code>python -m spacy download en_core_web_sm</code></pre>

<hr>

<h2>🔐 Notas</h2>
<ul>
  <li>Asegúrate de tener <code>genrerecommender_clf.pkl</code> y <code>vectorizer.pkl</code> en el directorio adecuado.</li>
  <li>El modelo <code>en_core_web_sm</code> de spaCy es obligatorio para el procesamiento de texto.</li>
  <li>Para producción, considera usar <code>gunicorn</code>, <code>tmux</code> o <code>systemd</code>.</li>
</ul>

<hr>

<h2>👨‍💻 Autor</h2>

<p><strong>Nacho</strong><br>
GitHub: <a href="https://github.com/nachothebest" target="_blank">nachothebest</a></p>

<hr>


</body>
</html>
