from django.urls import path
from drafts import views


urlpatterns = [
    path('drafts/', views.DraftList.as_view()),
    path('drafts/<int:pk>/', views.DraftDetail.as_view())
]