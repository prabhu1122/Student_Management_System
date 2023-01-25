from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from myApp.EmailBackEnd import EmailBackEnd

def BASE(request):
  return render(request, 'base.html')
  #return HttpResponse("hey prabhu!!")
  
  
  
def LOGIN(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
  return render(request, 'login.html')
  #return HttpResponse("hii prabhu")
  
  
def REGISTER(request):
  return render(request, 'register.html')
  
  
  
def doLogin(request):
  if request.method == "POST":
    user = EmailBackEnd.authenticate(
      request, 
      username = request.POST.get('email'),
      password = request.POST.get('password'),
    )
    if user != None:
      login(request, user)
      user_type = user.user_type
      if user_type == '1':
        return HttpResponse('hello')
        
      elif user_type == '2':
        return HttpResponse('hello')

      elif user_type == '3':
        return HttpResponse('hello')

      else:
        #message
        return redirect('login')
        
    else:
      #message
      return redirect('login')
  
  
  
  