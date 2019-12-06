from flask import request, redirect, render_template
import re
from app import app, db
from models import Blog, User
from hashutils import check_pw_hash


@app.route('/login', methods=['GET', 'POST'])
def login():
    # when a GET request return an empty form to collect login information
    if request.method == 'GET'
        return render_template('login.html')
        
    # when a PUSH with form information request infomation input through form
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        pw_verify = request.form['pw_verify']

        # check the user db for the first instance of the supplied email (???)
        user = User.query.filter_by(email=email).first()
        
    # if the user is valid and the password provided matches the hashed password in the db, flash the message to the / route
        if user and check_pw_hash(password, user.pw_hash)
            session['email'] = email
            flash('Logged in')
            return redirect('/')
    # otherwise flash the error and redirect to the login page
        else:
            flash("User password incorrect, or user does not exist", 'error')
            return redirect('/login')


    

# create a new post
@app.route('/newpost', methods=['POST', 'GET'])
def new_blog():

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_body = request.form['body']
        new_blog = Blog(blog_title, blog_body)
 
        title_error = ''
        body_error = ''

# prevents empty blog title from being entered into db
        if blog_title == '':
            title_error = 'Please enter a title for your blog.'

# prevents empty blog body from being entered into db
        if blog_body == '':
            body_error = 'Please enter text for your blog post'

# when the info colleted from the form passes without any errors from above, commit to db
        if not title_error and not body_error:
            db.session.add(new_blog)
            db.session.commit()

            # New id is auto generated by DB insert
            return redirect("/blog?blog_id=" + str(new_blog.id))

 # if any info from the form psses an error, return the error    
        else:
            return render_template('newpost.html', title_error = title_error, body_error = body_error)   

    return render_template('newpost.html')


@app.route('/blog/')
def get_blog():
# use GET to request id from the blog 
    blog_id = request.args.get('blog_id')

# if there is a blog id then provide the information on single blog to template
    if blog_id:
        blog = Blog.query.get(blog_id)
        blogs = None

# if there is no blog id provide all blog information to template
    else:
        blog = None
        blogs = Blog.query.all() 

    return render_template ('blog.html', blogs=blogs, blog=blog, id=blog_id)


if __name__ == '__main__':
    app.run()