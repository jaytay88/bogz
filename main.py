from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Homework@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

blogs = []

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(120), unique=True)
    blog_entry = db.Column(db.String(2500))

    def __init__(self, blog_name, blog_entry):
        self.blog_name = blog_name
        self.blog_entry = blog_entry

    def __repr__(self):
        return '<Title %r>'  % self.blog_name

def get_current_bloglist():
    return Blog.query.all()


@app.route("/newpost", methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        blog_name = request.form['blog_name']
        blog_entry = request.form['blog_entry']
        name_error = ''
        entry_error = ''

        if not blog_name:
            name_error = "Please fill in the blog name"
        if not blog_entry:
            entry_error = "Please fill in your blog entry"
        if not blog_name or not blog_entry:
            return render_template('newpost.html', name_error=name_error, entry_error=entry_error)

        blog = Blog(blog_name, blog_entry)
        db.session.add(blog)
        db.session.commit()
        blog_redirect = "./blog?id=" + str(blog.id)

        return redirect(blog_redirect)
    
    return render_template('newpost.html', title="Add a Blog!")


@app.route("/blog", methods=['POST', 'GET'])
def index():
    if request.args:
        id = request.args.get("id")
        blog = Blog.query.get(id)
        blog_name = blog.blog_name
        blog_entry = blog.blog_entry
        return render_template('entry_blog.html', blog_name=blog_name, blog_entry=blog_entry)

    return render_template('blog.html', title="Build-a-Blog!", blogs=get_current_bloglist())


if __name__ == "__main__":
    app.run()