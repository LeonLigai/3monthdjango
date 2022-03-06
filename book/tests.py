from django.test import TestCase

# Create your tests here.
#hw8

from datetime import date
from . import models, forms
from django.test import Client
from django.contrib.auth.models import User

class TestBookModel(TestCase):
    def test_model_book_create_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        books = models.book.objects.create(**book)
        self.assertEqual(books.title, book["title"])
        self.assertEqual(books.description, book["description"])
        self.assertEqual(books.image, book["image"])
        self.assertEqual(books.created_date, book["created_date"])
        self.assertEqual(books.update_date, book["update_date"])
        self.assertEqual(books.author, book["author"])


    def test_model_book_create_fail(self):
        book = {
            "title": "Test Title",
            "description": 25,
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        with self.assertRaises(ValueError):
            books = models.book.objects.create(**book)


    def test_model_book_update_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        books = models.book.objects.create(**book)
        new_title = "New Title"
        books.title = new_title
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.title, new_title)


    def test_model_book_update_fail(self):
        book = {
            "title": "Test Title",
            "description": 25,
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        with self.assertRaises(ValueError):
            books = models.book.objects.create(**book)
            new_title = "New Title"
            books.title = new_title
            books.save()
            books.refresh_from_db()
            self.assertEqual(books.title, new_title)


    def test_model_book_delete_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        books = models.book.objects.create(**book)
        book_id = books.id
        books.delete()
        with self.assertRaises(models.book.DoesNotExist):
            models.book.objects.get(id=book_id)

    def test_model_book_delete_fail(self):
        book = {
            "title": 25,
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        with self.assertRaises(ValueError):
            books = models.book.objects.create(**book)
            book_id = books.id
            books.delete()
            with self.assertRaises(models.book.DoesNotExist):
                models.book.objects.get(id=book_id)



class TestBookFeedBackModel(TestCase):
    def test_model_BookFeedBack_create_success(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": "Comment Test",
        }
        books_comment = models.BookFeedBack.objects.create(**book_feedback)
        self.assertEqual(books_comment.title, book_feedback["text"])
        self.assertEqual(books_comment.created_date, book_feedback["created_date"])
        self.assertEqual(books_comment.author, book_feedback["comment"])


    def test_model_BookFeedBack_create_fail(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": 25,
        }
        with self.assertRaises(ValueError):
            books_comment = models.BookFeedBack.objects.create(**book_feedback)


    def test_model_BookFeedBack_update_success(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": "Comment Test",
        }
        books_comment = models.BookFeedBack.objects.create(**book_feedback)
        new_text = "New Text"
        books_comment.title = new_text
        books_comment.save()
        books_comment.refresh_from_db()
        self.assertEqual(books_comment.title, new_text)

    def test_model_BookFeedBack_update_fail(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": 25,
        }
        with self.assertRaises(ValueError):
            books_comment = models.BookFeedBack.objects.create(**book_feedback)
            new_text = "New Text"
            books_comment.title = new_text
            books_comment.save()
            books_comment.refresh_from_db()
            self.assertEqual(books_comment.title, new_text)


    def test_model_BookFeedBack_delete_success(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": "Comment Test",
        }
        books_comment = models.BookFeedBack.objects.create(**book_feedback)
        book_feedback_id = books_comment.id
        books_comment.delete()
        with self.assertRaises(models.BookFeedBack.DoesNotExist):
            models.BookFeedBack.objects.get(id=book_feedback_id)

    def test_model_book_delete_fail(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": 25,
        }
        with self.assertRaises(ValueError):
            books_comment = models.BookFeedBack.objects.create(**book_feedback)
            book_feedback_id = books_comment.id
            books_comment.delete()
            with self.assertRaises(models.BookFeedBack.DoesNotExist):
                models.BookFeedBack.objects.get(id=book_feedback_id)




class TestBookForm(TestCase):
    def test_form_book_create_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        books = models.book.objects.create(**book)
        form = forms.BookForm(initial={"books": books})
        is_valid_form = form.is_valid()
        self.assertTrue(is_valid_form)
        form.save()

    def test_form_book_create_fail(self):
        book = {
            "title": 25,
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
             "author": "Gvido Test",
            }
        with self.assertRaises(ValueError):
            books = models.book.objects.create(**book)
            form = forms.BookForm(initial={"books": books})
            is_valid_form = form.is_valid()
            self.assertTrue(is_valid_form)
            form.save()


class TestBookFeedBackForm(TestCase):
    def test_form_BookFeedBack_create_success(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": "Comment Test",
        }
        books_comment = models.BookFeedBack.objects.create(**book_feedback)
        form = forms.BookForm(initial={"books_comment": books_comment})
        is_valid_form = form.is_valid()
        self.assertTrue(is_valid_form)
        form.save()

    def test_form_BookFeedBack_create_fail(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": 25,
        }
        with self.assertRaises(ValueError):
            books_comment = models.BookFeedBack.objects.create(**book_feedback)
            form = forms.BookForm(initial={"books_comment": books_comment})
            is_valid_form = form.is_valid()
            self.assertTrue(is_valid_form)
            form.save()


class TestBookViews(TestCase):
    def test_view_book_success(self):
        book = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        books = models.book.objects.create(**book)
        client = Client()
        user = User.objects.create(username='Username')
        client.force_login(user)
        response = client.get(path=f"/book/{books.id}/")
        self.assertEqual(response.status_code, 200)

    def test_view_book_fail(self):
        book = {
            "title": 25,
            "description": "Test Description",
            "image": "image.png",
            "created_date": date.today(),
            "update_date": date.today(),
            "author": "Gvido Test",
        }
        with self.assertRaises(ValueError):
            books = models.book.objects.create(**book)
            client = Client()
            user = User.objects.create(username='Username')
            client.force_login(user)
            response = client.get(path=f"/book/{books.id}/")
            self.assertEqual(response.status_code, 200)



class TestBookFeedBackViews(TestCase):
    def test_view_BookFeedBack_success(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": "Comment Test",
        }
        books_comment = models.BookFeedBack.objects.create(**book_feedback)
        client = Client()
        user = User.objects.create(username='Username')
        client.force_login(user)
        response = client.get(path=f"/book/{books_comment.id}/")
        self.assertEqual(response.status_code, 200)

    def test_view_BookFeedBack_fail(self):
        book_feedback = {
            "text": "Test Text",
            "created_date": date.today(),
            "comment": 25,
        }
        with self.assertRaises(ValueError):
            books_comment = models.BookFeedBack.objects.create(**book_feedback)
            client = Client()
            user = User.objects.create(username='Username')
            client.force_login(user)
            response = client.get(path=f"/book/{books_comment.id}/")
            self.assertEqual(response.status_code, 200)