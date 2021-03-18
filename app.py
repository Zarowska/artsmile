from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/user/<string:name>/<int:id>')
def use(name,id):
    return "User page: " + name + " - " + str(id)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/disabled')
def price():
    return render_template("disabled.html")

@app.route('/services')
def services():
    return render_template("services.html")


if __name__ == '__main__':
    app.run(debug=True)


