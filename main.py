from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

blog_names = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name = request.form['blog_name']
        blog_names.append(blog_name)

    return render_template('blogs.html',title="Add a Blog Entry", blog_names=blog_names)


app.run()