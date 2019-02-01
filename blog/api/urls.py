
from django.conf.urls import url

from .views import PostListAPIview

urlpatterns = [
    url(r'^$', PostListAPIview.as_view()),
]
