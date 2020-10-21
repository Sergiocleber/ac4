import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def sequencia():
   proximo = 1
   anterior = 0
   cont = 0
   resposta = "0,"
   while (cont < 50):
       temp = proximo
       proximo = proximo + anterior
       anterior = temp
       cont=cont+1
       resposta+= str(proximo) + ","


   return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
