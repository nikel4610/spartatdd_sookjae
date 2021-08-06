from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        past_time = timezone.now() + datetime.timedelta(days=-30)
        question = Question(question_text="test", pub_date=past_time)
        question.save()
        response = self.client.get("/polls/")

        self.assertQuerysetEqual(
            response.context['question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        question = Question(question_text="test", pub_date=future_time)
        question.save()
        response = self.client.get("/polls/")
        self.assertContains(response, "등록된 설문조사가 없습니다.")
        self.assertQuerysetEqual(response.context['question_list'], [])


