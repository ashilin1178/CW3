from flask import Flask, render_template, request, jsonify
from functions.func.utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, \
    get_posts_by_user, get_log

app = Flask(__name__)


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


@app.errorhandler(404)
def page_not_found(error):
    """
    вывод ошибки 404
    :param error:
    :return:
    """
    return f"Страница не найдена ошибка {error}", 404


@app.errorhandler(500)
def int_server_error(error):
    """
    вывод ошибки 500
    :param error:
    :return:
    """
    return f"Ошибка на стороне сервера: {error}", 500


@app.route('/api/posts')
def get_all_posts_json():
    """
    возвращает список постов в формате json
    :return:
    """

    posts = get_posts_all(path_posts)
    get_log()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def get_post_by_pk_json(post_id):
    """
    возвращает оди пост в формате json
    :param post_id:
    :return:
    """
    post = get_post_by_pk(path_posts, post_id)
    get_log()
    return jsonify(post)


if __name__ == '__main__':
    app.run()
