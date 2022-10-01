from statistics import mode
from django.db import models
from accounts.models import CustomUser

# 何のアプリで入れたか
ENTRY_TYPE = (
    ('manual', '手動'), 
    ('bank_book', '銀行通帳'), 
    ('fixed_cost', '固定費'), 
    ('csv_upload', 'CSVアップロード'),
    ('other', 'その他'),
)

# CSVで入れた場合のタイプは何か
CSV_ENTRY_TYPE = (
    ('yodo', 'ヨドバシ'), 
    ('view', 'びゅー'), 
    ('tokyo_gas', '東京ガス'), 
)

class AccountsItem(models.Model):
    '''勘定科目を表すモデル
    '''
    name = models.CharField(verbose_name='勘定科目', max_length=64)
    auxiliary_accounts = models.CharField(verbose_name='補助科目', max_length=80, null=True, blank=True)
    is_item_debits = models.BooleanField(verbose_name='科目の借方貸方')

    def __str__(self) -> str:
        return self.name


class Overview(models.Model):
    '''摘要を表すモデル
    '''
    detail = models.CharField(verbose_name='摘要', max_length=128)

    def __str__(self) -> str:
        return self.detail


class Slip(models.Model):
    '''伝票1行を表すモデル
    '''
    # 伝票の日付
    slip_date = models.DateField(
        verbose_name='取引日時',
    )

    debit_accounts = models.ForeignKey(
        AccountsItem,
        verbose_name='借方勘定科目',
        related_name="debit_accounts_item",
        on_delete=models.PROTECT,  # 例外を発生させて削除させない
    )

    credit_accounts = models.ForeignKey(
        AccountsItem,
        verbose_name='貸方勘定科目',
        related_name="credit_accounts_item",
        on_delete=models.PROTECT,  # 例外を発生させて削除させない
    )
    #is_debits = models.BooleanField(verbose_name='借方or貸方(Trueで借方)')

    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザ',
        on_delete=models.CASCADE, # ユーザを削除する場合は投稿データも全て削除
    )
    amount = models.BigIntegerField(verbose_name='金額')
    overview = models.ForeignKey(
        Overview,
        verbose_name='摘要',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    entry_type = models.CharField(max_length=48, choices=ENTRY_TYPE)
    csv_entry_type = models.CharField(
        max_length=48, 
        choices=CSV_ENTRY_TYPE, 
        null=True, 
        blank=True
    )

    def __str__(self) -> str:
        return f'id: {self.id} 借方科目: {self.debit_accounts.name} 金額: {self.amount}'

    class Meta:
        verbose_name = '伝票'
