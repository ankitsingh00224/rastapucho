from django.contrib import admin
from .models import Card,TopCard,RecentCard,BlogSlug,Blog,Review
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.
admin.site.register(Card)
admin.site.register(TopCard)
admin.site.register(RecentCard)


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [("title", {"fields": ["title"]}),
                 ("content", {"fields": ["content"]}),
                 ("slugs", {"fields": ["slug_title"]}),
                 ("href", {"fields": ["slug"]})
                 ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(BlogSlug)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Review)
