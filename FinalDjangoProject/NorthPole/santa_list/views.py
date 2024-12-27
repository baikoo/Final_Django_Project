from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Kid, SantasList

# Create Santa's List
def create_santas_list(request):
    if request.method == 'POST':
        santas_list = SantasList.objects.create()
        santas_list.generate_lists()
        return JsonResponse({"message": "Santa's List created successfully!"})
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=400)

# View Santa's List
def view_santas_list(request):
    santas_list = SantasList.objects.last()  # Get the most recent Santa's List
    context = {
        'nice_list': santas_list.nice_list.all(),
        'naughty_list': santas_list.naughty_list.all(),
    }
    return render(request, 'view_santas_list.html', context)

# Remove a Child
def remove_child(request, kid_id):
    santas_list = SantasList.objects.last()
    kid = get_object_or_404(Kid, id=kid_id)
    santas_list.nice_list.remove(kid)
    santas_list.naughty_list.remove(kid)
    return JsonResponse({"message": f"{kid.name} removed from Santa's List."})

# Create a Kid
def create_kid(request):
    if request.method == 'GET':
        name = request.POST['name']
        niceness_coefficient = float(request.POST['niceness_coefficient'])
        gift = request.POST.get('gift', None)
        Kid.objects.create(name=name, niceness_coefficient=niceness_coefficient, gift=gift)
        return JsonResponse({"message": "Kid created successfully!"})

# View All Kids
def view_all_kids(request):
    kids = Kid.objects.all()
    return render(request, 'view_all_kids.html', {'kids': kids})

# View Specific Kid
def view_kid(request, kid_id):
    kid = get_object_or_404(Kid, id=kid_id)
    return render(request, 'view_kid.html', {'kid': kid})
