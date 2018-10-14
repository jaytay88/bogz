from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Homework@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(120))
    blog_entry = db.Column(db.String(1000))

    def __init__(self, blog_name, blog_entry):
        self.blog_name = blog_name
        self.blog_entry = blog_entry

@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name = request.form['blog_name']
        blog_entry = request.form['blog_entry']
        new_blog = Blog(blog_name, blog_entry)
        db.session.add(new_blog)
        db.session.commit()

    blog_names = Blog.query.all()
    blog_entries = Blog.query.all()
    return render_template('blog.html',title="Add a Blog Entry", blog_names=blog_names, blog_entries=blog_entries)

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        blog_name = request.form['blog_name']
        blog_entry = request.form['blog_entry']
        new_blog = Blog(blog_name, blog_entry)
        db.session.add(new_blog)
        db.session.commit()

    blog_names = Blog.query.all()
    blog_entries = Blog.query.all()
    return render_template('newpost.html',title="Add a Blog Entry", blog_names=blog_names, blog_entries=blog_entries)
    

if __name__ == "__main__":
    app.run()