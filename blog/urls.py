from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailViews.as_view(),name='post_detail'),
    path('post/create/',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post_update'),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/draft/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('post/<int:pk>/approve/',views.comment_approval,name='comment_approval'),
    path('comment/<int:pk>/remove/',views.comment_removal,name='comment_removal'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),

]
