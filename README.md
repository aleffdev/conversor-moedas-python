# Conversor de Moedas — Python + Flask

Este é um conversor de moedas que utiliza Python, Flask e uma API pública (Frankfurter API) para converter valores entre diferentes moedas em tempo real.  
A interface é feita com HTML, CSS e JavaScript, e o back-end processa as requisições e retorna o valor convertido.

---

## Funcionalidades

- Conversão entre diversas moedas (USD, BRL, EUR, GBP etc.)
- Consome dados reais da API Frankfurter
- Interface simples e intuitiva
- Backend em Flask
- Retorno em JSON para o front-end

---

## Estrutura do Projeto

/seu-projeto
│-- app.py
│-- requirements.txt
│-- /templates
│ └── index.html
│-- /static
├── style.css
└── script.js


---

## Como rodar o projeto

1. Instale as dependências:

pip install -r requirements.txt


2. Execute o servidor:

python app.py


3. Abra o navegador e acesse:

http://127.0.0.1:5000

---

## API utilizada
Frankfurter — https://www.frankfurter.app  
API gratuita para conversão de moedas baseada no Banco Central Europeu.

---

## Licença
Este projeto é apenas para fins educacionais e pode ser utilizado livremente.


# Abaixo, um print do app rodando no navegador:
(images/flask_app.png)
