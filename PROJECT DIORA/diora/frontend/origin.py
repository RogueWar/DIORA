from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from diora import app, db, bcrypt
from diora.frontend.forms import RegistrationForm, LoginForm, PForm
from diora.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


front = Blueprint('front', __name__)

@front.route("/")
@front.route("/home")
def home():
    posts = Post.query.order_by(Post.date_posted.desc()) 
    return render_template('home.html', posts=posts)


@front.route("/about")
def about():
    return render_template('about.html', title='About')

@front.route("/user")
@login_required
def user():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('user.html', title='Account', posts=posts)


@front.route("/post/<int:post_id>")
def postid(post_id):
    post = Post.query.get(post_id)
    return render_template('postid.html', title=post.title, post=post)

@front.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('front.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('front.login'))
    return render_template('register.html', title='Register', form=form)


@front.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('front.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('front.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@front.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('front.home'))




@front.route("/post", methods=['GET', 'POST'])
@login_required
def post():
    form = PForm()
    if form.validate_on_submit():
        post= Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created.', 'success')
        return redirect(url_for('front.user'))
    return render_template('post.html', title='Post', form=form, legend="New Post")



@front.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_postid(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    form = PForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated.', 'success')
        return redirect(url_for('front.postid', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('post.html', title='Update Post', form=form, legend="Update Post")

@front.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_postid(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted!', 'success')
    return redirect(url_for('front.user'))
