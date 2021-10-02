from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый текст',
        )

    def test_post_models_have_correct_object_names(self):
        """Проверяем, что у моделей post корректно работает __str__."""
        post = PostModelTest.post
        expected_post_text = post.text
        self.assertEqual(expected_post_text, str(post))

    def test_post_models_have_correct_verbose_name(self):
        """Проверяем, что у всех полей модели Post верный verbose_name"""
        field_verbose_name = {
            'text': 'Текст',
            'pub_date': 'Дата публикации',
            'group': 'Группа',
            'author': 'Автор',
        }
        post = PostModelTest.post
        for field, expected_value in field_verbose_name.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_value)

    def test_post_models_have_correct_help_text(self):
        """Проверяем, что у всех полей модели Post верный help_text"""
        field_help_text = {
            'text': 'Введите текст',
            'pub_date': 'Введите дату публикации',
            'group': 'Введите название группы',
            'author': 'Введите автора'
        }
        post = PostModelTest.post
        for field, expected_value in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).help_text, expected_value)


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовый тайтл',
            slug='test-slug',
            description='Тестовое описание группы',
        )

    def test_group_models_have_correct_object_names(self):
        """Проверяем, что у моделей group корректно работает __str__."""
        group = GroupModelTest.group
        expected_group_title = group.title
        self.assertEqual(expected_group_title, str(group))

    def test_group_models_have_correct_verbose_name(self):
        """Проверяем, что у всех полей модели Group верный verbose_name"""
        field_verbose_name = {
            'title': 'Заголовок',
            'slug': 'Уникальная строка',
            'description': 'Описание',
        }
        group = GroupModelTest.group
        for field, expected_value in field_verbose_name.items():
            with self.subTest(field=field):
                self.assertEqual(
                    group._meta.get_field(field).verbose_name, expected_value)

    def test_group_models_have_correct_help_text(self):
        """Проверяем, что у всех полей модели Post верный help_text"""
        field_help_text = {
            'title': 'Введите заголовок',
            'slug': 'Введите уникальную строку',
            'description': 'Введите описание',
        }
        group = GroupModelTest.group
        for field, expected_value in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    group._meta.get_field(field).help_text, expected_value)
