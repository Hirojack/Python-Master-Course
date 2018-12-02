from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render_templates() devolverá el código html dentro de un archivo HTML
    # Dicho archivo debe estar almacenado en una carpeta llamada "templates"
    return render_template("home.html")
    
@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)