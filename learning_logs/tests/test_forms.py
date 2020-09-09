from django.test import SimpleTestCase

from learning_logs.forms import TopicForm, EntryForm


class TestForms(SimpleTestCase):

    def test_topic_form_valid_data(self):
        form = TopicForm(data={'text': 'topic1'})

        self.assertTrue(form.is_valid())

    def test_topic_form_no_data(self):
        form = TopicForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)        

