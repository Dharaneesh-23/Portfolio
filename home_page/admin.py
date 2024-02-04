from django.contrib import admin
from .models import welcome,experience,links,education,about,projects,skills,Contact_message
# Register your models here.

admin.site.register(links)
admin.site.register(education)
admin.site.register(about)
admin.site.register(projects)
admin.site.register(welcome)
admin.site.register(experience)
admin.site.register(skills)
admin.site.register(Contact_message)