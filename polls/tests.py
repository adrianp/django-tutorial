import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        Question.was_published_recently should return False for future
        questions
        """
        time = timezone.now() + datetime.timedelta(days=365)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """
        Question.was_published_recently should return False for old questions
        """
        time = timezone.now() - datetime.timedelta(days=1)
        past_question = Question(pub_date=time)
        self.assertFalse(past_question.was_published_recently())

    def test_was_published_recently_with_new_question(self):
        """
        Question.was_published_recently should return True for new questions
        """
        time = timezone.now() - datetime.timedelta(hours=23)
        new_question = Question(pub_date=time)
        self.assertTrue(new_question.was_published_recently())
