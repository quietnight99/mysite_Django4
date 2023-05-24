from django.urls import path
from . import views

app_name = 'polls'

"""
include的背后是一种即插即用的思想。项目的根路由不关心具体app的路由策略，只管往指定的二级路由转发，实现了应用解耦。
app所属的二级路由可以根据自己的需要随意编写，不会和其它的app路由发生冲突。app目录可以放置在任何位置，而不用修改路由。这是软件设计里很常见的一种模式。
建议：除了admin路由外，尽量给每个app设计自己独立的二级路由
"""

# 一个路由配置模块就是一个urlpatterns列表，列表的每个元素都是一项path，每一项path都是以path()的形式存在。
# path()方法可以接收4个参数，其中前2个是必须的：route和view，以及2个可选的参数：kwargs和name。
# urlpatterns = [
#     path('index/', views.index, name = 'index'),
#     # path('<int:question_id>/', views.detail, name = 'detail'),
#     path('specifics/<int:question_id>/', views.detail, name = 'detail'),
#     path('<int:question_id>/results/', views.results, name = 'results'),
#     # path('<int:question_id>/vote/', views.vote, name = 'vote'),
#     path('<int:question_id>/vote/', views.vote, name = 'vote'),
# ]

# urlpattern = [
#     path('',views.IndexView.as_view(),name = 'index'),
#     path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
#     path('<int:pk>/results/',views.ResultsView.as_view(),name = 'results'),
#     path('<int:question_id>/vote/',views.vote,name = 'vote'),
# ]
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]