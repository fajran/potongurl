from django.contrib import admin

from potongurl.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('hash', 'active', 'url_excerpt', 'created')
    list_filter = ('active',)

admin.site.register(Link, LinkAdmin)

