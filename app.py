from flask import Flask, redirect, render_template, send_from_directory

app = Flask(__name__)

app.url_map.strict_slashes = False

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/static/<path:filename>")
def staticfiles(path):
    return send_from_directory("static", path)

@app.route('/form')
def form():
    # redirect to home page
    return redirect("/")
    
@app.route('/form/<path:subpath>')
def form_subpath(subpath):
    return render_template("form.html")


@app.route('/admin', methods=['POST'])
def admin():
    return render_template("admin.html")

@app.route('/admin', methods=['GET'])
def adminLogin():
    return render_template("adminLogin.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)