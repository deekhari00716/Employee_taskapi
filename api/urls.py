from django.urls import path
from . import views

urlpatterns = [

    path('task/', views.TaskListCreate.as_view()),
    path('task/<int:pk>', views.TaskRetrieveUpdateDestroy.as_view()),
    path('task/<int:pk>/complete', views.TaskComplete.as_view()),
    path('task/completed', views.TaskCompletedList.as_view()),

    #AUTH
    path('signup/', views.signup),
    path('login/', views.login),
]
