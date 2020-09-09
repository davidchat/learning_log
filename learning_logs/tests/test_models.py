from django.test import TestCase
from django.contrib.auth.models import User

from learning_logs.models import Topic, Entry


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='1234',
        )
        self.user1.save()
        
        # Create dummy topic
        self.topic1 = Topic.objects.create(
            text='topic1',
            owner=self.user1,
        )
        # Create dummy entry
        self.entry1 = Entry.objects.create(
            text='entry1',
            topic=self.topic1,
        )

    def test_topic_string_representation(self):
        self.assertEqual(str(self.topic1), 'topic1')

    def test_entry_string_representation(self):
        self.assertEqual(str(self.entry1), 'entry1')

