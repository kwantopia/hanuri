from django.contrib import admin
from main.models import BrokenRelationKorean, BrokenRelationEnglish

class BrokenRelationKoreanAdmin(admin.ModelAdmin):
  list_display = ['broken', 'restore', 'remote_id', 'user_agent', 'timestamp']

class BrokenRelationEnglishAdmin(admin.ModelAdmin):
  list_display = ['broken', 'restore', 'country', 'remote_id', 'user_agent', 'timestamp']

admin.site.register(BrokenRelationKorean, BrokenRelationKoreanAdmin)
admin.site.register(BrokenRelationEnglish, BrokenRelationEnglishAdmin)