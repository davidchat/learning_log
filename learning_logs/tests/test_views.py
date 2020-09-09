from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from learning_logs.models import Topic, Entry


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        # Create dummy user
        self.user1 = User.objects.create_user(
            username='user1',
            password='1234',
        )
        self.user1.save()
        self.user1_login = self.client.login(username='user1', password='1234')
        # Create dummy topic
        self.topic1 = Topic.objects.create(
            text = 'topic1',
            owner = self.user1,
        )
        # Create dummy entry
        self.entry1 = Entry.objects.create(
            text = 'entry1',
            topic = self.topic1,
        )
        self.index_url = reverse('learning_logs:index')
        self.topics_url = reverse('learning_logs:topics')
        self.topic_url = reverse('learning_logs:topic', args=['1'])
        self.new_topic_url = reverse('learning_logs:new_topic')
        self.new_entry_url = reverse('learning_logs:new_entry', args=['1'])
        self.edit_entry_url = reverse('learning_logs:edit_entry', args=['1'])

    def tearDown(self):
        self.client.logout()

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/index.html')
    
    def test_topics_if_logged_in_GET(self):
        login = self.user1_login        
        response = self.client.get(self.topics_url)

        # Test that user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/topics.html')

    def test_topic_if_logged_in_GET(self):
        login = self.user1_login
        response = self.client.get(self.topic_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/topic.html')

    def test_new_topic_if_logged_in_GET(self):
        login = self.user1_login
        response = self.client.get(self.new_topic_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/new_topic.html')
    
    def test_new_topic_if_logged_in_POST(self):
        login = self.user1_login
        response = self.client.post(self.new_topic_url, {
            'text': 'topic2'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user1.topic_set.last().text, 'topic2')

    def test_new_entry_if_logged_in_GET(self):
        login = self.user1_login
        response = self.client.get(self.new_entry_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/new_entry.html')
    
    def test_new_entry_if_logged_in_POST(self):
        login = self.user1_login
        response = self.client.post(self.new_entry_url, {
            'text': 'entry2'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user1.topic_set.first().entry_set.last().text, 'entry2')

    def test_edit_entry_if_logged_in_GET(self):
        login = self.user1_login
        response = self.client.get(self.edit_entry_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/edit_entry.html')

    def test_edit_entry_if_logged_in_POST(self):
        login = self.user1_login
        response = self.client.post(self.edit_entry_url, {
            'text': 'entryA'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user1.topic_set.first().entry_set.first().text, 'entryA')



