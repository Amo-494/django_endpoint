from datetime import datetime
from django.http import JsonResponse
import pytz

def get_info(request):
    # Retrieve query parameters from the request
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Check if required parameters are provided
    if not slack_name or not track:
        return JsonResponse({"error": "slack_name and track parameters are required."}, status=400)
    
    # Get the current UTC time
    utc_now = datetime.now(pytz.utc)
    utc_time_str = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Get the current day of the week
    current_day = utc_now.strftime("%A")

    # Replace these hardcoded values with your actual GitHub repository URLs
    github_repo_url = "https://github.com/Amo-494/django_endpoint"
    github_file_url = f"{github_repo_url}/blob/main/hngproject"

    # Construct the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    # Return the JSON response with a 200 status code
    return JsonResponse(response, status=200)
