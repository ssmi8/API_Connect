from django.urls import path
from skills import views

urlpatterns = [
    path('skills/', views.SkillList.as_view()),
    path('skills/<int:pk>/', views.SkillsDetail.as_view()),
]
