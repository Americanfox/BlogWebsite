from flask import Flask, render_template, request
import requests

def get_data():
    response = requests.get("https://api.npoint.io/08f94d8e14a204390a45")
    return response.json()




app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<blog_id>')
def post(blog_id):
    id_of_blog = int(blog_id) - 1
    return render_template("post.html", blog=blogs[id_of_blog])

@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

blogs = get_data()



if __name__ == '__main__':
    app.run(debug=True)