# Imports
from flask import Flask, request, jsonify, send_from_directory
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Configurações do NLTK
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
stop_words = set(stopwords.words('portuguese'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(tokens)

# Carregar o vetorizador e o classificador Naive Bayes
with open('data/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open('data/nb_classifier.pkl', 'rb') as f:
    nb_classifier = pickle.load(f)

# Iniciar o Flask
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'static/index.html')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'Falta o campo "text" no JSON.'}), 400

    text = data['text']
    processed_text = preprocess_text(text)
    text_vectorized = tfidf_vectorizer.transform([processed_text])
    prediction = nb_classifier.predict(text_vectorized)
    return jsonify({'category': prediction[0]})

if __name__ == '__main__':
    # tornar a API Flask acessível de fora do contêiner
    app.run(host='0.0.0.0', port=5000, debug=True)

