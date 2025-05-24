import pandas as pd
import numpy as np
import joblib
import os
import spacy
import re
import string
nlp = spacy.load("en_core_web_sm")

#  ----->ESTO SE AGREGO PARA EL MODELO 2
def clean_text(text):

    text = text.lower()  # pasar a minúsculas
    text = re.sub(r'\d+', '', text)  # eliminar números
    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)  # quitar puntuación
    text = re.sub(r'\s+', ' ', text).strip()  # eliminar espacios extras
    return text

def lemmatize_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.lemma_ != '-PRON-'])

def predecir_genero(input_data):
    # Cargar modelo y scaler (asegúrate de guardar y cargar scaler si es necesario)
    modelo_path = os.path.join(os.path.dirname(__file__), 'genrerecommender_clf.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')
    vectorizer = joblib.load(vectorizer_path)
    recommender = joblib.load(modelo_path)


    # Crear DataFrame con 1 fila
    df_input = pd.DataFrame([input_data])
    df_input['clean_plot'] = df_input['plot'].apply(clean_text)
    df_input['lemmatized_plot'] = df_input['clean_plot'].apply(lemmatize_text)
    vectorizer_input = vectorizer.transform(df_input['lemmatized_plot'])
    df_input = pd.DataFrame(vectorizer_input.toarray(), columns=vectorizer.get_feature_names_out())


    # Predicción
    cols = ['p_Action', 'p_Adventure', 'p_Animation', 'p_Biography', 'p_Comedy', 'p_Crime', 'p_Documentary', 'p_Drama', 'p_Family',
        'p_Fantasy', 'p_Film-Noir', 'p_History', 'p_Horror', 'p_Music', 'p_Musical', 'p_Mystery', 'p_News', 'p_Romance',
        'p_Sci-Fi', 'p_Short', 'p_Sport', 'p_Thriller', 'p_War', 'p_Western']
    prediccion = recommender.predict_proba(df_input)[0]
    res = pd.DataFrame([prediccion], columns=cols)

    return res

# Uso desde consola
if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) == 1:
        print('Por favor ingresa un JSON con los datos de la sinopsis de la pelicula.')
    else:
        input_json = sys.argv[1]
        input_data = json.loads(input_json)

        pred = predecir_genero(input_data)
        print(f'Predicción de Genero: {pred:.2f}')