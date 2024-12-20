import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import logout
from .utils import predict
import uuid  # For generating unique file names
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {}
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        # Ensure 'media/' directory exists
        media_path = settings.MEDIA_ROOT
        os.makedirs(media_path, exist_ok=True)

        # Save the file with a unique name
        unique_filename = f"{uuid.uuid4()}_{uploaded_image.name}"
        image_path = os.path.join(media_path, unique_filename)
        with open(image_path, 'wb+') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # Predict the class
        try:
            predicted_class = predict(image_path)
            context['predicted_class'] = predicted_class
        except Exception as e:
            context['error'] = f"An error occurred: {e}"

    return render(request, 'prediction.html', context)

def about(request):
    return render(request, 'about.html')

def architecture(request):
   return render(request,'architecture.html')

def landing(request):
   return render(request,'landing.html')

def contact(request):
    return render(request, 'contact.html')

def library(request):
    return render(request, 'library.html')

def services(request):
    return render(request,'services.html')

def login(request):
   return render(request,'login.html')

def form(request):
   return render(request,'form.html')

def logout_view(request):
    logout(request)
    return redirect('landing')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to a home page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("about")
 else:
  form = UserCreationForm()
 return render(request, "signup.html", {"form": form})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  
def newsletter_submit(request):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            gender = data.get('gender')
            place = data.get('place')

            return JsonResponse({'message': 'Thank you for subscribing to our newsletter!'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)
@csrf_exempt
def newsletter_submit(request):
    if request.method == 'POST':
        print(request.body) 
        return JsonResponse({'message': 'Data received successfully.'}, status=200)
    return JsonResponse({'message': 'Invalid request method.'}, status=405)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user  
    return render(request, 'profile.html', {'user': user})


###updated
from django.http import HttpResponse
from .models import PredictionHistory
from .forms import ImageUploadForm

def predict_plant_disease(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            predicted_class = "Sample Disease"  # Replace with actual prediction logic

            # Save to history
            history = PredictionHistory(image=image, predicted_class=predicted_class)
            history.save()

            return render(request, 'prediction.html', {
                'form': form,
                'predicted_class': predicted_class,
                'history': PredictionHistory.objects.all()
            })
    else:
        form = ImageUploadForm()

    return render(request, 'prediction.html', {
        'form': form,
        'history': PredictionHistory.objects.all()
    })

def delete_prediction(request, id):
    """
    Deletes a specific prediction entry and its associated image.
    """
    try:
        entry = PredictionHistory.objects.get(id=id)
        
        file_path = os.path.join(settings.MEDIA_ROOT, entry.image.name)
        if os.path.exists(file_path):
            os.remove(file_path)

        entry.delete()
    except PredictionHistory.DoesNotExist:
        pass  
    return redirect('index')
