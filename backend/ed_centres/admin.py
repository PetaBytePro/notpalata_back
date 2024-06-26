from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from django_summernote.admin import SummernoteModelAdmin

from content.mixins import AdminFieldMixin

from .models import CenterInfo, CenterTask, Discipline, EducationalMaterial, ManagerProfile, StudyPlan, TeachingStaff,\
    EducationalContact


@admin.register(EducationalContact)
class EducationalContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contact',]
    list_display_links = ['title']


@admin.register(CenterInfo)
class CenterInfoAdmin(AdminFieldMixin, TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ['id', 'title', 'get_little_image',]
    list_display_links = ['title']
    
    readonly_fields = ['get_little_image',]
    fields = ['title', 'description', 'thesis', ('image', 'get_little_image',),]
    search_fields = ['title',]
    summernote_fields = ('thesis',)


@admin.register(CenterTask)
class CenterTaskAdmin(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('id', 'get_small_text',)
    list_display_links = ('get_small_text',)
    summernote_fields = ('text',)

    def get_small_text(self, object):
        return f'{object.text[:67]}...' if len(object.text) > 70 else object.text

    get_small_text.short_description = ""


@admin.register(ManagerProfile)
class ManagerProfileAdmin(AdminFieldMixin, TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('id', 'full_name', 'get_little_image',)
    list_display_links = ('full_name',)
    summernote_fields = ('text',)

    readonly_fields = ['get_little_image',]
    fields = ['full_name', 'text', ('image', 'get_little_image',),]


class DisciplineInline(TranslationStackedInline):
    extra = 0
    model = Discipline


@admin.register(StudyPlan)
class StudyPlanAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    inlines = (DisciplineInline,)


@admin.register(TeachingStaff)
class TeachingStaffAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'position',)
    list_display_links = ('full_name',)
    
    fields = ['full_name', 'position',]


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'url',)
    list_display_links = ('title',)
