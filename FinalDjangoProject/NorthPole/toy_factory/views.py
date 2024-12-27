from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Toy, Coal
from santa_list.models import Kid

# 1. Create a Toy
def create_toy(request, kid_id):
    if request.method == 'POST':
        kid = get_object_or_404(Kid, id=kid_id)
        toy_type = request.POST.get('toy_type')
        Toy.objects.create(kid=kid, toy_type=toy_type)
        return JsonResponse({"message": f"Toy for {kid.name} created successfully!"})

# 2. View All Toys
def view_all_toys(request):
    toys = Toy.objects.all()
    return render(request, 'view_all_toys.html', {'toys': toys})

# 3. View a Specific Toy
def view_toy(request, toy_id):
    toy = get_object_or_404(Toy, id=toy_id)
    return render(request, 'view_toy.html', {'toy': toy})

# 4. Generate a Gift for a Kid (Coal if on naughty list)
def generate_gift(request, kid_id):
    kid = get_object_or_404(Kid, id=kid_id)
    if kid in kid.naughty_list.all():  # Check if the kid is in the naughty list
        Coal.objects.create(kid=kid, reason="Naughty behavior")
        return JsonResponse({"message": f"{kid.name} has received coal!"})
    else:
        toy = Toy.objects.get(kid=kid)
        return JsonResponse({"message": f"{kid.name} receives the toy: {toy.toy_type}"})
