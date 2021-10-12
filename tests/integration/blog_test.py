from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test post', 'Test content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test post')
        self.assertEqual(b.posts[0].content, 'Test content')

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(len(b.posts), 0)

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test post', 'Test content')
        expected = {'title': 'Test', 'author': 'Test Author',
                    'posts': [{'title': 'Test post', 'content': 'Test content'}]}

        self.assertDictEqual(expected, b.json())
