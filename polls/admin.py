from django.contrib import admin

from .models import  Choice, Question
from django.contrib.auth.models import Group
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html


admin.site.site_header = 'Admin Tutorial DashBoard'
admin.site.site_title = 'Title reviewed'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # exclude = ('title',)
    # fields = (liste des champs voulus)
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'font_size_html_display')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
         'classes': ['collapse']})
    ]
    # inlines = [ChoiceInline]
    # fields = ['pub_date', 'question_text']
    change_list_template = 'admin/question/question_change_list.html'


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]
        return custom_urls + urls


    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size set successfully!')
        return HttpResponseRedirect("../")


    def font_size_html_display(self, obj):
        return format_html(
            f'<span style="font-size: {obj.font_size}px;">{obj.font_size}</span>'
        )

        
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question','votes']

admin.site.register(Choice, ChoiceAdmin)
# admin.site.unregister(Group)