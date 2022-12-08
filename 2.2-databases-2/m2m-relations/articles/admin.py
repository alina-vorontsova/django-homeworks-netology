from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    
    def clean(self):
        main_tag = 0 
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tag += 1 
        if main_tag == 0:
            raise ValidationError('Укажите основной раздел.')
        elif main_tag > 1:
            raise ValidationError('Основным может быть только один раздел.')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_dasplay = ['title']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
