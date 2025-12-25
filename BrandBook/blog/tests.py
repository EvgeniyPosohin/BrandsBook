from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import UserProfile, SocialLink, Section


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpassword123'
        )
        self.profile = UserProfile.objects.create(
            user = self.user,
            first_name = 'Ivan',
            last_name = 'Ivanov',
            slug = 'IvanovIvan'
        )

    def test_profile_creation(self):
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(self.profile.last_name, 'Ivanov')
        self.assertEqual(self.user.profile, self.profile)

class SocialLinkTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpassword123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            first_name='Ivan',
            last_name='Ivanov',
            slug='IvanovIvan'
        )
        self.social_link = SocialLink.objects.create(
            profile = self.profile,
            network = 'github',
            url='https://github.com/testuser'
        )

    def test_social_link_creation(self):
        self.assertEqual(SocialLink.objects.count(), 1)
        self.assertEqual(self.social_link.profile, self.profile)
        self.assertEqual(self.social_link.network, 'github')

    def test_social_link_delete(self):
        self.profile.delete()
        self.assertEqual(SocialLink.objects.count(), 0)

    def test_network_choise(self):
        links = self.profile.social_links.all()
        self.assertIn(self.social_link, links)

class SectionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='testpassword123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            first_name='Ivan',
            last_name='Ivanov',
            slug='IvanovIvan'
        )
        self.section = Section.objects.create(
            profile=self.profile,
            type='resume',
            title='Резюме'
        )

    def test_section_creation(self):
        self.assertEqual(Section.objects.count(), 1)
        self.assertEqual(self.section.profile, self.profile)
        self.assertEqual(self.section.type, 'resume')

    def test_section_choise(self):
        links = self.profile.sections.all()
        self.assertIn(self.section, links)

