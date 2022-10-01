from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Slip

class IndexView(ListView):
  # index.htmlをレンダリングする
  template_name = 'index.html'
  # 伝票日付の降順で並べる
  queryset = Slip.objects.order_by('-slip_date')
  # 1ページに表示するレコード件数
  paginate_by = 10
