from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
  # レコードにidとusername表示
  list_display = ('id', 'username')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'username')

# Django管理サイトにCustomerUser、CustomUserAdminを登録する
admin.site.register(CustomUser, CustomUserAdmin)
