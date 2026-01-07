from django.urls import path
from .views import itemlistcreateview, itemDetailView

urlpatterns = [
    path("items/", itemlistcreateview.as_view()),
    path("items/<int:pk>/", itemDetailView.as_view()),
]
