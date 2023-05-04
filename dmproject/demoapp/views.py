from django.shortcuts import render
from django.http import HttpResponse
from  . models import place
from  . models import team
# Create your views here

def demo(request):
    obj = place.objects.all()
    teams=team.objects.all()
    return render(request, "index.html", {'result': obj,'results': teams})



#   name="calculation"
#def calculation(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # addition=x+y
 #   subtraction = x - y
  #  multiplication = x * y
  #  division = x / y

   # return render(request, 'result.html',
    #              {'addition': addition, 'subtraction': subtraction, 'multiplication': multiplication,
     #              'division': division})



