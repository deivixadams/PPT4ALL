from flask import Flask, request, redirect, make_response, render_template # importa request junto con Flask

app = Flask(__name__)  # crea una instancia de la clase Flask, que representa la aplicación web.

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a productor']  # lista de tareas pendientes
#crear un diccionario hipotetico para el contexto
context2 = {
    'perro':'Firulais',
    'gato': 'Michi',
    'loro': 'Paco',
    'tortuga': 'donatello'
}

#crear una variable de tipo string que contenga dos parráfos
str1 = """
Lorem ipsum dolor sit amet consectetur adipisicing elit.
Doloremque, magni. Quos, quae. Quisquam, quod. Quia, quos. Quae, voluptatem. Quam, quibusdam.
Quisquam, voluptatem. Quam, quibusdam.
Quisquam, voluptatem. Quam, quibusdam.afPERo
Lorem ipsum dolor sit amet consectetur adipisicing elit.
"""

#vamos a definir el index de la aplicación web
@app.route('/')  # es un decorador que se usa para definir la ruta de la URL en la que se ejecutará la función que está debajo.
def index():
   user_ip = request.remote_addr  # obtiene la dirección IP del cliente que hizo la solicitud.
   response = make_response(redirect('/hello'))
   response.set_cookie('user_ip', user_ip)
   return response

@app.route('/hello')  # es un decorador que se usa para definir la ruta de la URL en la que se ejecutará la función que está debajo.
def hello_world():
    #crear un contexto tipo diccionario
    context = {
        'user_ip':request.cookies.get('user_ip'),
        'todos': context2,
        'cadena': str1
    }
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', **context) # ** para expandir un diccionario


if __name__ == '__main__':
    app.run(debug = True)  # ejecuta la aplicación web.
