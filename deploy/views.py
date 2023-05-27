from django.shortcuts import render

# Create your views here.



def reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        choice = request.POST.get('choice')

        # Process the form data (perform desired actions)

        # Render a success message or redirect to another page
        return render(request, 'deploy/success.html', {'first_name': first_name, 'last_name':last_name, 'choice': choice})
    else:
        return render(request, 'deploy/deploy.html')
