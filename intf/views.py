from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def index(request):
	return render(request,'intf/index.html')