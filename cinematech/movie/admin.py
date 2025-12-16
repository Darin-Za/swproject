from django.contrib import admin
from movie.models import  Movie

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','release_year','description','rating','poster')
    ordering = ('id',)
    search_fields = ('title',)

admin.site.register(Movie, ArticleAdmin)

