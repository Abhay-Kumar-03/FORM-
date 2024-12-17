from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  
def submit_form(request):
    if request.method == 'POST': 
        try:
           
            data = json.loads(request.body)
            print("Received Data:", data)  
           
            return JsonResponse({'message': 'Form submitted successfully!'}, status=200)
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'message': 'Error processing form data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
