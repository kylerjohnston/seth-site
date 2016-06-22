from . import blog
from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from .forms import PostForm, DeleteForm
from ..models import Post
from .. import db
import datetime
from .blog_class import Blog
from bs4 import BeautifulSoup
import requests
import random

def generate_description(post):
    if len(post) > 160:
        description = post[0:159].strip()
    else:
        description = post.strip()
    description += ' ...'
    return description

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

def parse_link(url):
    """ Returns a tuple of three strings:
        Link url, link title, and link description
    """
    try:
        r = requests.get(url)
    except:
        flash('Error: URL could not be requested.')
        return url, None, None
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html5lib')
        title = soup.title.string
        description = parse_description(soup)
        return url, title, description
    else:
        flash('Error: request exited with status code {}'.format(str(r.status_code)))
        return url, None, None

def parse_description(soup):
    """ Parses meta description tags from BeautifulSoup object """
    desc = ''
    for meta in soup.findAll('meta'):
        if 'description' == meta.get('name', '').lower():
            desc = meta['content']
    return desc

@blog.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        if form.link.data != '' and form.link.data is not None:
            url, link_title, link_description = parse_link(form.link.data)
        else:
            url, link_title, link_description = None, None, None
        new_post = Post(
            title = form.title.data,
            date = datetime.datetime.today(),
            content = form.content.data,
            user = current_user,
            link_url = url,
            link_description = link_description,
            link_title = link_title)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.root'))
    return render_template('blog/new.html', form = form)

def make_blog():
    blog = Blog()
    try:
        pages = blog.pages[0]
    except:
        pages = []
    return blog, pages

@blog.route('/')
def root():
    blog, pages = make_blog()
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
    # Find the requested post
    post = Post.query.filter_by(slug = post_name).first()
    description = generate_description(post.content)

    # Randomly select two "related" posts to show in footer
    blog, pages = make_blog()
    pages = [page for page in pages if page.slug != post_name]
    pages = random.sample(pages, 2)
    if len(pages) == 2:
        related = [
            {
                'title': page.title,
                'description': generate_description(page.content),
                'slug': page.slug
            }
            for page in pages
        ]
    else:
        pages = None

    if post is not None:
        return render_template('blog/post.html',
                               post = post,
                               description = description,
                               related = related)
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
    form.link.data = post.link_url
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
