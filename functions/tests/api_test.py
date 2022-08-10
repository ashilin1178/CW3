from run import app

# Задаем, какие ключи ожидаем получать у поста
keys_post_should_be = {"poster_name", "poster_avatar", "pic", "content", "pk", "views_count", "likes_count", "pk"}


# @pytest.fixture()
# def client():
#     return app.test_client()

def test_get_post_by_pk_json():
    """
    проверяем что возвращает словарь с правильным набором ключей
    :return:
    """
    post = app.test_client().get('/api/posts/1').get_json()
    assert type(post) == dict, "не правильный тип данных"
    assert post.keys() == keys_post_should_be, "Не верный набор ключей"


def test_get_all_posts_json():
    """
    проверяем, что возвращает список словарей с правильным набором ключей
    :return:
    """
    posts = app.test_client().get('/api/posts').get_json()
    assert type(posts) == list, "не правильный тип данных"
    assert posts[0].keys() == keys_post_should_be, "Не верный набор ключей"
