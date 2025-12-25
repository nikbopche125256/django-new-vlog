from django.contrib import admin
from .models import About , Sociallink
# Register your models here.

# To disable adding more than one About instance i Used the following code:
# Remaimber if there is no about instance then it will show the add button otherwise it will hide the add button.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0: # if limit exids more than 0 then it will return false and disable the add button
            return True
        else:
            return False

admin.site.register(About, AboutAdmin)
admin.site.register(Sociallink)