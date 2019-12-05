from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import re


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:test@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(200))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/newpost', methods=['POST', 'GET'])
def new_blog():

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_body = request.form['body']
        new_blog = Blog(blog_title, blog_body)

        title_error = ''
        body_error = ''

        if blog_title == '':
            title_error = 'Please enter a title for your blog.'

        if blog_body == '':
            body_error = 'Please enter text for your blog post'

        if not title_error and not body_error:
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/blog')
        else:
            return render_template('newpost.html', title_error = title_error, body_error = body_error)   

    return render_template('newpost.html')


@app.route('/blog/', methods = ['GET'])
def get_blog():
    blogs = Blog.query.all()
    blog_id = request.args.get('blog_id')
    blog = Blog.query.get(blog_id)

    return render_template ('blog.html', blogs=blogs, blog=blog, id=blog_id)



if __name__ == '__main__':
    app.run()