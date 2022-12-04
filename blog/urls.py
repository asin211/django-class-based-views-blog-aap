from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

# rest api design
# posts/<int:pk>/
urlpatterns = [
    path("posts/new/", BlogCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("", BlogListView.as_view(), name="home"),
]
