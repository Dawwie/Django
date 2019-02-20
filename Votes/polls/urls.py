from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name = "index"),
    #127.0.0.1/polls/
    path('<question_id>/', views.detail, name="detail"),
    #127.0.0.1/polls/1-9
    path('<question_id>/results/', views.results, name="results"),
    #127.0.0.1/polls/1-9/results
    path('<question_id>/vote/', views.vote, name="vote"),
    #127.0.0.1/polls/1-9/vote
]