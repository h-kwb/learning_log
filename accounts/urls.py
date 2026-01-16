"""accounts用のURLパターンの定義"""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # デフォルトの認証URLを取り組む
    path('', include('django.contrib.auth.urls')),
    # User登録page
    path('register/', views.register, name='register'),
]