from app import app, db
from flask import render_template, flash, redirect, url_for
from flask import session
from forms import PostsCreateForm
from models import Post

@app.route("/posts")
@app.route("/posts/index")
def posts():
    return render_template("posts.html", items=Post.query.limit(25).all())

@app.route("/posts/create", methods=["GET", "POST"])
def posts_create():
    if session.get("is_auth"):
        return redirect(url_for(posts.__name__))
    form = PostsCreateForm()
    if form.validate_on_submit():
        post = Post(header=form.header.data, body=form.body.data)
        db.session.add(post)
        try:
            db.session.commit()
            flash(f"Post created {form.header.data}")
            return redirect(url_for(posts.__name__))
        except Exception as e:
            db.session.rollback()
            flash(f"Пост не був створений через: {e}!")

    return render_template("posts_create.html", form=form)

