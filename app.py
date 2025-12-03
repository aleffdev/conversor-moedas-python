from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    data = request.get_json()
    moeda_origem = data.get('moeda_origem')
    moeda_destino = data.get('moeda_destino')
    try:
        valor = float(data.get('valor', 0))
    except (TypeError, ValueError):
        return jsonify({"erro": "Valor inválido"}), 400

    try:
        url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_origem}&to={moeda_destino}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dados = resp.json()
        # Frankfurter retorna rates: { "USD": 1.23 }
        resultado = dados.get('rates', {}).get(moeda_destino)
        # opcional: calcular taxa (resultado/valor) se quiser mostrar
        rate = None
        if resultado is not None and valor != 0:
            rate = resultado / valor
        if resultado is not None:
            return jsonify({"resultado": round(resultado, 2), "rate": rate})
        else:
            return jsonify({"erro": "Conversão indisponível."}), 500
    except Exception as e:
        print("Erro na API:", e)
        return jsonify({"erro": "Erro na conexão. Tente novamente."}), 500

if __name__ == '__main__':
    app.run(debug=True)