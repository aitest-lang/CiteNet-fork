from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required


@login_required() #redirect when user is not logged in
def search(request):
    return render(request,"core/search_suggestions.html")

@csrf_exempt
def save_search(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            search_id = data.get('id')
            if search_id is not None:
                print(f"Received search ID: {search_id}")
                return JsonResponse({'status': 'success', 'message': 'Search ID saved successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid search ID'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)