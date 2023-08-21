from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.utils import timezone
from .models import Location , FencedField
from shapely.geometry import Point, Polygon
from .forms import FencedFieldForm

def index(request):
    latest_location = Location.objects.latest('timestamp')
    context = {
        'latitude': latest_location.latitude,
        'longitude': latest_location.longitude,
        'timestamp':latest_location.timestamp
    }
    return render(request, "index.html",context)



    
    # return render(request, 'map.html')


# @csrf_exempt
# def handle_post_request(request):
#     if request.method == 'POST':

#         key1_value = request.POST.get('key1')
#         key2_value = request.POST.get('key2')

#         # my_variable = "Hello, World!"
#         # my_list = [1, 2, 3, 4, 5]
        
#         context = {
#         'variable': key1_value,
#         'list': key2_value,
#         }
        
#         data = {
#             'lat':key1_value,
#             'lon' :key2_value,
#         }
#         cordinates = json.dumps(data)
        
#         # print(cordinates.lat)
#         # print(cordinates.lon)
        
#         # return render(request, 'map.html', context)
#     # return HttpResponse("success")
#     return JsonResponse(cordinates, safe=False)

@csrf_exempt
def handle_post_request(request):
    if request.method == 'POST':
        latitude = request.POST.get('key1')
        longitude = request.POST.get('key2')
        timestamp = timezone.now()

        location = Location(latitude=latitude, longitude=longitude, timestamp=timestamp)
        location.save()
        
        latest_location = Location.objects.latest('timestamp')
        data = {
            'latitude': latest_location.latitude,
            'longitude': latest_location.longitude,
            'timestamp': latest_location.timestamp
        }

        # Return JSON response for AJAX requests
        return JsonResponse(data)
    
    else:
        return render(request, 'map.html')
        
        
    # elif request.method == 'GET':
    #    return HttpResponse("Success!")
        # return render(request, 'map.html', context)
    # return render(request, 'map.html')

        
def map_view(request):
    
    if request.method == 'POST':
        form = FencedFieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/map")  
    else:
        form = FencedFieldForm()
    

    latest_location = Location.objects.latest('timestamp')
    fencedpoints = FencedField.objects.latest('timestamp')
    
    polygon_vertices = [
    (fencedpoints.point1lat, fencedpoints.point1lon), 
    (fencedpoints.point2lat, fencedpoints.point2lon), 
    (fencedpoints.point3lat, fencedpoints.point3lon), 
    (fencedpoints.point4lat, fencedpoints.point4lon), 
    ]
    
    polygon = Polygon(polygon_vertices)
    point_to_check = Point(latest_location.latitude, latest_location.longitude)
    
    if polygon.contains(point_to_check):
        inside = 1    
    else:
        inside = 2 
    context = {
        'latitude': latest_location.latitude,
        'longitude': latest_location.longitude,
        'timestamp':latest_location.timestamp,
        'form':form,
        'inside': inside,
    }
    return render(request, "map.html",context )

def updatedata(request):
    if request.method == 'GET':
        
            latest_location = Location.objects.latest('timestamp')
            fencedpoints = FencedField.objects.latest('timestamp')
    
            polygon_vertices = [
            (fencedpoints.point1lat, fencedpoints.point1lon), 
            (fencedpoints.point2lat, fencedpoints.point2lon), 
            (fencedpoints.point3lat, fencedpoints.point3lon), 
            (fencedpoints.point4lat, fencedpoints.point4lon), 
            ]
    
            polygon = Polygon(polygon_vertices)
            point_to_check = Point(latest_location.latitude, latest_location.longitude)
    
            if polygon.contains(point_to_check):
                inside = 1    
            else:
                inside = 2 

            
            lat = request.GET['lat']
            if latest_location.latitude != lat:
                data = {
                    'latitude': latest_location.latitude,
                    'longitude': latest_location.longitude,
                    'timestamp': latest_location.timestamp,
                    'inside':inside,
                }
                return JsonResponse(data) # Sending an success response
            else:
                return JsonResponse({'message': 'No updates or invalid request'})
    
        
