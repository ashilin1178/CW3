import string

from functions.func.utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, get_posts_by_user, search_for_posts

# Задаем, какие ключи ожидаем получать у комментария
keys_comment_should_be = {"post_id", "commenter_name", "comment", "pk"}

# Задаем, какие ключи ожидаем получать у поста
keys_post_should_be = {"poster_name", "poster_avatar", "pic", "content", "pk", "views_count", "likes_count", "pk"}

path_comments = 'data/comments.json'
path_posts = 'data/data.json'


def test_get_posts_all():
    """
    проверяем вывод всех постов
    :return:
    """
    posts = get_posts_all(path_posts)
    assert type(posts) == list, "возвращается не список"
    assert len(posts) > 0, "возвращается пустой список"
    assert set(posts[0].keys()) == keys_post_should_be, "неверный список ключей"


def test_get_post_by_pk():
    """ Проверяем, верный ли пост возвращается при запросе одного """
    post = get_post_by_pk(path_posts, 1)
    assert (post["pk"] == 1), "возвращается неправильный пост"
    assert set(post.keys()) == keys_post_should_be, "неверный список ключей"


def test_get_comments_by_post_id():
    """
    проверяем вывод всех комментариев по заданному посту
    :return:
    """
    comments = get_comments_by_post_id(path_comments, 1)
    assert comments[0]["post_id"] == 1, "пост с неверным ID"
    assert (len(comments) > 0), "возвращается пустой список"
    assert set(comments[0].keys()) == keys_comment_should_be, "неверный список ключей"


def test_get_posts_by_user():
    """
    проверяем вывод всех постов пользователя
    :return:
    """
    post = get_post_by_pk(path_posts, 2)
    posts = get_posts_by_user(path_posts, post["poster_name"])
    assert (len(posts) > 0), "возвращается пустой список"
    assert set(post.keys()) == keys_post_should_be, "неверный список ключей"


def test_search_for_posts():
    """
    проверяем поиск по ключевому слову
    :return:
    """
    post = get_post_by_pk(path_posts, 2)
    query = post["content"].lower().translate(str.maketrans('', '', string.punctuation)).split(" ")[0]
    posts = search_for_posts(path_posts, query)
    assert (len(posts) > 0), "возвращается пустой список"
    assert set(post.keys()) == keys_post_should_be, "неверный список ключей"
