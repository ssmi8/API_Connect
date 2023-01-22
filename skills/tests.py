from django.contrib.auth.models import User
from .models import Skills
from rest_framework import status
from rest_framework.test import APITestCase


class SkillListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='steve', password='pass')

    def test_can_list_posts(self):
        steve = User.objects.get(username='steve')
        Skills.objects.create(owner=steve, title='a title')
        response = self.client.get('/skills/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/skills/', {'title': 'a title'})
        count = Skills.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/skills/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SkillsDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Skills.objects.create(
            owner=adam, title='a title', content='adams content'
        )
        Skills.objects.create(
            owner=brian, title='another title', content='brians content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/skills/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/skills/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='steve', password='pass')
        response = self.client.put('/skills/1/', {'title': 'a new title'})
        skills = Skills.objects.filter(pk=1).first()
        self.assertEqual(skills.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/skills/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
