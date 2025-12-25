from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    """Расширенный профиль пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField('Name', max_length=50,)
    last_name = models.CharField('Last Name', max_length=50)
    avatar = models.ImageField('Avatar', upload_to='avatars/', blank=True)
    slug = models.SlugField('slug',max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('Published', default=False)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

class SocialLink(models.Model):
    """Социальные сети и контакты"""
    NETWORK_CHOICES = (
        ('vk', 'ВКонтакте'),
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('github', 'GitHub'),
        ('website', 'Веб-сайт'),
        ('mail', 'mail')
        # Добавьте другие по необходимости
    )

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_links')
    network = models.CharField(max_length=50, choices=NETWORK_CHOICES)
    url = models.TextField(max_length=300)

    class Meta:
        indexes = [
            models.Index(fields=('url',))
        ]


    def __str__(self):
        return f'{self.network}: {self.url}'

class Section(models.Model):
    """Раздел для портофлио(Резюме, Проекты и т.д.)"""
    SECTION_TYPES = (
            ('about', 'О себе'),
            ('resume', 'Резюме'),
            ('projects', 'Проекты'),
            ('certificates', 'Сертификаты'),
            ('skills', 'Навыки'),
            ('custom', 'Пользовательский'),
    )

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sections')
    type = models.CharField('Тип раздела', max_length=20, choices=SECTION_TYPES)
    title = models.CharField('Заголовок раздела', max_length=200)
    is_visible = models.BooleanField('Видимый', default=True)

