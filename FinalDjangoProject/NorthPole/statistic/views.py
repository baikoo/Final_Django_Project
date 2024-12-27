from django.shortcuts import render
from django.http import JsonResponse
from santa_list.models import Kid, SantasList
from toy_factory.models import Toy
from django.db.models import Count

# 1. How many kids are on the nice_list and naughty_list
def nice_and_naughty_counts(request):
    santas_list = SantasList.objects.last()  # Get the most recent Santa's List
    nice_count = santas_list.nice_list.count()
    naughty_count = santas_list.naughty_list.count()
    return JsonResponse({"nice_list_count": nice_count, "naughty_list_count": naughty_count})

# 2. A list of toys and how many kids want each toy
def toys_and_kid_counts(request):
    toy_counts = Toy.objects.values('toy_type').annotate(kid_count=Count('kid'))
    return JsonResponse({"toy_counts": list(toy_counts)})

# 3. How long does it take to make all the toys (given time per toy)
def time_to_make_toys(request):
    time_per_toy = float(request.GET.get('time_per_toy', 0))  # Time in minutes to make one toy
    total_toys = Toy.objects.count()
    total_time = total_toys * time_per_toy
    return JsonResponse({"total_time_minutes": total_time})

# 4. How long does it take to deliver all the toys (given time per delivery)
def time_to_deliver_toys(request):
    time_per_delivery = float(request.GET.get('time_per_delivery', 0))  # Time in minutes to deliver one toy
    total_toys = Toy.objects.count()
    total_time = total_toys * time_per_delivery
    return JsonResponse({"total_delivery_time_minutes": total_time})
