from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import re


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:test@localhost:8889/build=a=blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String)

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/newpost', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name = request.form['title']
        new_blog = Blog(blog_name)
        db.session.add(new_task)
        db.session.commit()

    # blogs = Blog.query.all()
    return render_template('newpost.html')

# @app.route('/delete-task', methods=['POST'])
# def delete_task():

#     task_id = int(request.form['task-id'])
#     task = Task.query.get(task_id)
#     task.completed = True
#     db.session.add(task)
#     db.session.commit()
 
#     return redirect('/')


if __name__ == '__main__':
    app.run()