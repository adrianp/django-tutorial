import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from .models import Question


def create_question(text='', days=1, hours=0):
    """
    Creates a question with the given text and published date offset as
    specified by the days and hours aguments.
    """
    date = timezone.now() + datetime.timedelta(days=days, hours=hours)
    return Question.objects.create(question_text=text, pub_date=date)


class QuestionViewIndex(TestCase):
    def test_detail_view_with_a_future_question(self):
        qid = create_question().id
        response = self.client.get(reverse('polls:detail', args=(qid,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        qid = create_question('baz?', 0, -12).id
        response = self.client.get(reverse('polls:detail', args=(qid,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'baz?')


class QuestionsViewTest(TestCase):
    def test_index_view_with_no_arguments(self):
        """
        An appropiate message should be displayed when no questions are
        available
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_index_view_with_a_future_question(self):
        """
        Should not display future questions
        """
        create_question()
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Should display past question but not the future one
        """
        create_question('future?', 365)
        create_question('foo?', -1)
        response = self.client.get(reverse('polls:index'))
        questions = response.context['question_list']
        self.assertEquals(len(questions), 1)
        self.assertEquals(questions[0].question_text, 'foo?')

    def test_index_view_with_two_past_questions(self):
        """
        Should display past questions but no future ones
        """
        create_question('future?', 0, 1)
        create_question('foo?', -1, 23)
        create_question('bar?', 0, -1)
        response = self.client.get(reverse('polls:index'))
        questions = response.context['question_list']
        self.assertEquals(len(questions), 2)
        self.assertEquals(questions[0].question_text, 'bar?')
        pass


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
