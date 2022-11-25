from django.urls import path
from .views import TeamView, TeamViewsTest

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<team_id>/", TeamViewsTest.as_view()),
]
