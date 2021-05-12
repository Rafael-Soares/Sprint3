from os import set_inheritable
from django.shortcuts import redirect, render
#importação para cadastrar os usuários
from django.contrib.auth.models import User
#importação para autenticacao dos usuarios
from django.contrib import auth

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        #recuperando os valores do formulário
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confSenha = request.POST['confiSenha']
        if not nome.strip():
            print('o campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('o campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha!=confSenha:
            print('as senhas não podem ser iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists(): #verificando se o usuário já existe
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha) #cadastrando usuário na base de dados
        user.save()

        print('usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
       
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() #trazando o username associado ao email
            user = auth.authenticate(request, username=nome, password=senha) 
            if user is not None: #autenticacao de fato
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('index')
