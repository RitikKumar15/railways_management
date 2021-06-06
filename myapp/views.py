from django.shortcuts import render, redirect
from .models import Train, BookTicket
from django.db.models import Q
from .forms import TrainSearchForm, RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def Home(request):
  return render(request, 'myapp/home.html')

def Train_Spot(request):
  if request.method == 'POST':
    form = TrainSearchForm(request.POST)
    if form.is_valid():
      train_from = form.cleaned_data.get('train_from')
      train_to = form.cleaned_data.get('train_to')
      print(train_from, train_to)
      tn_search = Train.objects.filter(Q(train_from__icontains=train_from) & Q(train_to__icontains=train_to))
      print(tn_search)
      context = {
        'form':form,
        'tn_search':tn_search
        }
      return render(request, 'myapp/trainspot.html', context)
  else:
    form = TrainSearchForm()
    return render(request, 'myapp/trainspot.html', {'form':form})

def Schedule(request):
  all_train = Train.objects.all()
  return render(request, 'myapp/schedule.html', {'all_train':all_train})
  
def Book_Train(request):
  if not request.user.is_authenticated:
    return redirect('/login')
  else:
    if request.method == 'POST':
      user = request.user
      tid = request.POST.get('tid')
      tn = Train.objects.get(id=tid)
      seat_no = tn.available_seats
      bt = BookTicket(train=tn, user=user)
      bt.save()
      tn.available_seats = tn.total_seats - 1
      tn.save()
      messages.success(request, 'Congratulation, Your Train Hs Been Booked Successful!')
      return render(request, 'myapp/booktrain.html', {'tn':tn, 'seat_no':seat_no})
    else:
      return redirect ('/trainspot')

def Cancel(request):
  if not request.user.is_authenticated:
    return redirect('/login')
  else:
    if request.method == 'POST':
      user = request.user
      uno = request.POST.get('train_no')
      uname = request.POST.get('train_name')
      if BookTicket.objects.filter(Q(train__train_no=uno) & Q(train__train_name=uname) & Q(user=user)).exists():
        bt = BookTicket.objects.filter(Q(train__train_no=uno) & Q(train__train_name=uname) & Q(user=user))
        tn = Train.objects.get(train_no=uno)
        tn.available_seats +=1
        bt.delete()
        messages.success(request, 'Your Ticket Has Been Cancelled!')
      else:
        messages.warning(request, 'No Such Data Available.Please Enter Correct Details!')
    return render(request, 'myapp/cancel.html')

def Reschedule(request):
  return render(request, 'myapp/reschedule.html')

def user_Login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      form = LoginForm(request=request, data=request.POST)
      if form.is_valid():
        print('valid')
        uname = form.cleaned_data.get('username')
        upass = form.cleaned_data.get('password')
        validUser = authenticate(username=uname, password=upass)
        print(validUser)
        if validUser is not None:
          login(request, validUser)
          return redirect('/trainspot')
    else:
      form = LoginForm()
      print ('get')
      return render(request, 'myapp/login.html', {'form':form})
  else:
    return redirect ('/trainspot')
    

def Status(request):
  if not request.user.is_authenticated:
    return redirect ('/login')
  else:
    user = request.user
    tickets = BookTicket.objects.filter(user=user)
    if tickets:
      for tk in tickets:
        if tk.train.available_seats != 0:
          seat_no = tk.train.available_seats+1
      return render(request, 'myapp/status.html', {'tickets': tickets, 'seat_no': seat_no})
    else:
      messages.info(request, 'No Such Data Available, Book Tickets To See Your Train Status Here!')
      return render(request, 'myapp/status.html', {'tickets': tickets})

def user_Regi(request):
  if request.user.is_authenticated:
    return redirect ('/trainspot')
  else:
    if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/login')
    else:
      form = RegistrationForm()
    return render(request, 'myapp/signup.html', {'form':form})
  
def user_Logout(request):
  logout(request)
  return redirect('/login')
  
def BuyTicket(request):
  if not request.user.is_authenticated:
    return redirect ('/login')
  else:
    if request.method == 'POST':
      user = request.user
      tid = request.POST.get('tid')
      tn = Train.objects.get(id=tid)
      seat_no =tn.available_seats
      return render(request,'myapp/ticket.html',{'tn':tn, 'seat_no':seat_no})
    else:
      return redirect ('/trainspot')