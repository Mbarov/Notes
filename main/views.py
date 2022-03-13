from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NoteForm
from .models import Note

#создание нового аккаунта
def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
    else:
        form  = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})



#вход в ЛК
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
        else:
            form = AuthenticationForm()
            return render(request, 'main/login.html', {'form': form}) 
    else:
        form = AuthenticationForm()
        return render(request, 'main/login.html', {'form': form})


#выход из ЛК
def logoutView(request):
    logout(request)
    return redirect('login')


#Главная страница
def home(request):
    if request.user.is_authenticated:
        count = Note.objects.filter(user=request.user).count
    else:
        count=0   
    return render(request, 'main/home.html', {'count': count})

#Список заметок
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-date')
    return render(request, 'main/notes_list.html', {'notes': notes})

#Создание заметки
def create(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            full_text = request.POST['full_text']
            note = Note.objects.create(user=request.user,full_text=full_text)
            note.save()
            return redirect('notes_list')
        else:
            error = 'Форма была неверной'            
    form = NoteForm()
    context = {
        'form': form,
        'error': error}
    return render(request, 'main/create.html', context)


#Удаление заметки
def remove_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if note.user == request.user:
        note.delete()
    return redirect('notes_list')