from django.conf.urls import url
from .views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view()),
]
