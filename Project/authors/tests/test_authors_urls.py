from django.test import TestCase
from django.urls import reverse, resolve
from authors import views


class AuthorsTest(TestCase):
    def test_authors_register_url_is_correct(self):
        url = reverse('authors:register')
        self.assertEqual(url, '/authors/register/')

    def test_authors_register_view_function_is_correct(self):
        url = reverse('authors:register')
        view = resolve(url)
        self.assertIs(view.func, views.register_view)

    def test_authors_register_view_returns_status_code_200_OK(self):
        url = reverse('authors:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_authors_register_view_loads_correct_template(self):
        url = reverse('authors:register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'authors/pages/register_view.html')
