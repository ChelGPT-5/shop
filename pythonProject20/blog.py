from flask import Flask, flash, redirect, \
    render_template, request, url_for
from facade import PostsFacade
from db import EngineDB

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
engine_db = EngineDB()
posts_facade = PostsFacade(engine_db=engine_db)


@app.route('/')
def index():
    posts_data = posts_facade.get_all_posts()
    return render_template('index.html', posts=posts_data)


@app.route('/posts/<int:post_id>')
def post(post_id):
    post_data = posts_facade.get_post(id_=post_id)
    return render_template('post.html', post=post_data)


@app.route('/<int:post_id>/edit', methods=['POST', 'GET'])
def edit(post_id):
    post_data = posts_facade.get_post(id_=post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are both required')
        else:
            posts_facade.update_post(id_=post_id,
                                     title=title,
                                     content=content)
            return redirect(url_for('index'))
    return render_template('edit.html', post=post_data)


@app.route('/<int:post_id>/delete', methods=['POST', ])
def delete(post_id):
    posts_facade.remove_post(id_=post_id)
    flash(f"Post {post_id} was deleted")
    return redirect(url_for('index'))


@app.route('/create-post', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are both required')
        else:
            posts_facade.create_post(title=title, content=content)
            return redirect(url_for('index'))
    return render_template('create.html')


app.run(debug=True)