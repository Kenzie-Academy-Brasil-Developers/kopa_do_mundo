from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
import ipdb


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        teams_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)
        return Response(teams_list)

    def post(self, request):
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)
