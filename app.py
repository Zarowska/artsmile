from urllib import request

from flask import Flask, render_template, url_for, make_response

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

@app.route('/aits')
def services():
    return render_template("aits.html")


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash, make_response
#...
@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res
#...


#...
@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res
#...


# ...
@app.route('/aits/', methods=['POST', 'GET'])
def aits():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60 * 60 * 24 * 15)
        res.headers['location'] = url_for('aits')
        return res, 302

    return render_template('aits.html')
# ...