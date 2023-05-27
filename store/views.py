from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request, 'store/home.html')




def store(request):
    return render(request, 'store/store.html')
   
 
def search(request):
 
            
    return render(request, 'store/store.html' )
