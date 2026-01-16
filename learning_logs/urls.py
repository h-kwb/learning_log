"""learning_logsのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # HomePage
    path('', views.index, name='index'),
    # 全てのTopicを表示するpage
    path('topics/', views.topics, name='topics'),
    # 全てのTopicを表示するpage
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # 新規Topicの追加page
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新規記事の追加page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 記事の編集page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]