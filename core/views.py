from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from core.models import PayData, Post

# Create your views here.
def home(request):
    return render(request, 'core/main.html')

@login_required
def productone(request):
    one = PayData.objects.filter(user=request.user)
    if not one:
        return HttpResponse('Payment required')
    else:
        return render(request, 'core/one.html')

@login_required
def producttwo(request):
    one = PayData.objects.filter(user=request.user)
    if not one:
        return HttpResponse('Payment required')
    else:
        return render(request, 'core/one.html')
    

@login_required
def postdata(request):
    post = Post.objects.all()
    one = PayData.objects.filter(user=request.user, unit=1)#.order_by('-id')[:1]
    if not one:
        return HttpResponse('Payment required')
    else:
        return render(request, 'core/content.html', {'post':post})


