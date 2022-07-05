from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('cat/<int:id>/', MainIndex.as_view(), name='cat'),
    path('uplaod/', UploadPost.as_view(), name='upload'),
    path('post/<str:action>/<int:post_id>/', PostLike.as_view(), name='like'),
    path('comments/<int:post_id>/', PostCommentView.as_view(), name='comments')
]
