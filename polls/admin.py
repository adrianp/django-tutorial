from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    # you could skip the fieldsets, but this way you can customize them
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
