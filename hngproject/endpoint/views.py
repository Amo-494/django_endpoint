from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
import pytz

# Create your views here.
def get_info(request):

    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if not slack_name or not track:
        return JsonResponse({"error": "slack_name and track parameters are required."}, status=400)
    
    utc_now = datetime.now(pytz.utc)
    utc_time_str = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    current_day = utc_now.strftime("%A")

    github_repo_url = "https://github.com/Amo-494/django_endpoint"
    github_file_url = f"{github_repo_url}/blob/main/file_name.ext"