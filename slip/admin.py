from django.contrib import admin
from .models import Slip, AccountsItem, Overview

class SlipAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'slip_date', 'amount',)
    list_display_links = ('id', 'slip_date', 'amount',)
  

class AccountsItemAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


class OverviewAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'detail',)
    list_display_links = ('id', 'detail',)


# django管理サイトに登録
admin.site.register(Slip, SlipAdmin)
admin.site.register(AccountsItem, AccountsItemAdmin)
admin.site.register(Overview, OverviewAdmin)

