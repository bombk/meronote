from django.contrib import admin

from savefile.models import saveFile

# Register your models here.
class SaveFile(admin.ModelAdmin):
    list_display=('id','name','message','fname')

admin.site.register(saveFile,SaveFile)