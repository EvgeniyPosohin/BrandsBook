from django.contrib import admin
from blog.models import UserProfile, SocialLink, Section


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['profile', 'network', 'url']
    list_filter = ['network',]

admin.site.register(UserProfile)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['type', 'title', 'is_visible']
    list_filter = ['is_visible', ]

