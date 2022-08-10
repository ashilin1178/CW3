import string
import logging

from flask import json


def load_data(path):
    """
    загружает все посты из файла data.json
    :return:
    """
    with open(path, "r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts


def get_posts_all(path_posts):
    """
    возвращает все посты
    :param path_posts:
    :return:
    """
    return load_data(path_posts)


def get_posts_by_user(path_posts, poster_name):
    """
    возвращает все посты пользователя
    :param path_posts:
    :param poster_name:
    :return:
    """
    posts = load_data(path_posts)
    posts_user = []

    try:
        for post in posts:
            if poster_name == post['poster_name']:
                posts_user.append(post)

        return posts_user
    except ValueError:
        "Такого пользователя не существует"


def get_comments_by_post_id(path_comments, post_id):
    """
    возвращает все комментарии выбранного поста
    :param path_comments:
    :param post_id:
    :return:
    """
    comments = load_data(path_comments)
    comments_post = []

    try:
        for comment in comments:
            if post_id == comment["post_id"]:
                comments_post.append(comment)

        return comments_post
    except ValueError:
        "К этому посту еще нет комментариев"


def search_for_posts(path_posts, query):
    """осуществляет поиск постов по ключевому слову
    :param path_posts:
    :param query:
    :return:
    """
    posts = load_data(path_posts)
    query_posts = []
    query_lower = query.lower()

    for post in posts:
        # переводим в нижний регистр, удаляем знаки препинания из поста и преобразуем строку в список (разделитель
        # пробел)
        words_post = post["content"].lower().translate(str.maketrans('', '', string.punctuation)).split(" ")
        if query_lower in words_post:
            query_posts.append(post)

    return query_posts


def get_post_by_pk(path_posts, pk):
    """
    возвращает один пост по его номеру
    :param path_posts:
    :param pk:
    :return:
    """
    posts = load_data(path_posts)
    for post in posts:
        if post["pk"] == pk:
            return post


def get_log():
    logger_api = logging.getLogger()
    file_handler = logging.FileHandler(filename="log/api.log", mode='a', encoding='utf-8')
    formatter_api = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
    file_handler.setFormatter(formatter_api)
    logger_api.addHandler(file_handler)
    pass
