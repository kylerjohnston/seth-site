from . import blog
from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from .forms import PostForm, DeleteForm
from ..models import Post
from .. import db
import datetime
from .blog_class import Blog

def page_test(page_num, pages):
    if len(pages) > page_num:
        newer_pages = True
    else:
        newer_pages = False
    if page_num > 1:
        older_pages = True
    else:
        older_pages = False

    return older_pages, newer_pages

@blog.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(
            title = form.title.data,
            date = datetime.datetime.today(),
            content = form.content.data,
            user = current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.root'))
    return render_template('blog/new.html', form = form)

@blog.route('/')
def root():
    blog = Blog()
    try:
        pages = blog.pages[0]
    except:
        pages = []
    older_pages, newer_pages = page_test(1, blog.pages)
    return render_template('blog/blog.html',
                           posts = pages,
                           newer_pages = newer_pages,
                           older_pages = older_pages,
                           page_num = 1)

@blog.route('/pages/<pagenumber>/')
def pages(pagenumber):
    pagenumber = int(pagenumber)
    blog = Blog()
    try:
        page = blog.pages[(pagenumber - 1)]
    except:
        return redirect(url_for('blog.root'))
    older_pages, newer_pages = page_test(pagenumber, blog.pages)
    return render_template('blog/blog.html',
                           posts = page,
                           newer_pages = newer_pages,
                           older_pages = older_pages,
                           page_num = pagenumber)

@blog.route('/posts/<post_name>')
def post(post_name):
    post = Post.query.filter_by(slug = post_name).first()
    if post is not None:
        return render_template('blog/post.html',
                               post = post)
    else:
        return abort(404)

@blog.route('/edit/<postid>/', methods=['GET', 'POST'])
@login_required
def edit(postid):
    post = Post.query.get_or_404(int(postid))
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.last_modified = datetime.datetime.today()
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_name = post.slug))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('blog/edit.html',
                           form = form,
                           postid = postid)

@blog.route('/rm/<postid>', methods = ['GET', 'POST'])
@login_required
def delete(postid):
    form = DeleteForm()
    post = Post.query.get_or_404(int(postid))
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('blog/delete.html',
                           form = form,
                           post = post)
