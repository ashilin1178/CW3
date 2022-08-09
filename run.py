from flask import Flask, render_template, request
# import logging
# from loader.loader import loader_blueprint
# from main.main import main_blueprint

from functions.func.utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, \
    get_posts_by_user

app = Flask(__name__)
# # подключаем логирование в файл и конфигурируем уровень логирования
# logging.basicConfig(filename='log.txt', level=logging.INFO, encoding='utf-8')
# # регистрируем blueprint
# app.register_blueprint(main_blueprint)
# app.register_blueprint(loader_blueprint)

path_posts = "data/data.json"
path_comments = "data/comments.json"

@app.route('/')
def main_page():
    """
    главная страница
    :return:
    """
    posts = get_posts_all(path_posts)
    return render_template("index.html", posts=posts, len=len(posts))

@app.route('/post/<int:postid>')
def post_page(postid):
    """
    страница поста
    :param postid:
    :return:
    """
    post = get_post_by_pk(path_posts, postid)
    print(post)
    comments = get_comments_by_post_id(path_comments, postid)
    len_comm = len(comments)
    return render_template("post.html", postid=postid, post=post, comments=comments, len_comm=len_comm)

@app.route('/search')
def search_posts():
    """
    поиск постов по входящему слову
    :return: 
    """
    qwery = request.args.get('s', '')
    posts = search_for_posts(path_posts, qwery)
    return render_template('search.html', posts=posts, len=len(posts), qwery=qwery)

@app.route('/users/<username>')
def users_posts(username):
    """
    вывод всех постов пользователя
    :param username:
    :return:
    """
    posts = get_posts_by_user(path_posts, username)
    return render_template("user-feed.html", posts=posts)

if __name__ == '__main__':
    app.run()