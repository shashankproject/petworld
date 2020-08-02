from django.contrib import admin
from testapp.models import feedback
# Register your models here.
class feedbackAdmin(admin.ModelAdmin):
    list_display=['name','feedback']


admin.site.register(feedback,feedbackAdmin)
