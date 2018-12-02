from flask import Flask

# Se crea una instancia de la clase Flask para la aplicación
app = Flask(__name__)

# Se define una función para la aplicación.
# El decorador inicial indica que esta función está mapeada en el directorio home 'localhost:5000'
# Definir la ruta como '/about/' hará que la función se ejecute al ingresar a localhost:5000/about/
@app.route('/')
def home():
    return "Contenido del sitio"

# Finalmente, se ejecuta la aplicación al ejecutar el script
# Si el script se importa desde otro script, la aplicación no correrá
if __name__ == "__main__":
    app.run(debug=True)