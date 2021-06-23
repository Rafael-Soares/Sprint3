from os import set_inheritable
from django.db import reset_queries
from django.shortcuts import redirect, render
#importação para cadastrar os usuários
from django.contrib.auth.models import User
#importação para autenticacao dos usuarios
from django.contrib import auth, messages  

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        #recuperando os valores do formulário
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confSenha = request.POST['confiSenha']
        if not campo_vazio(nome):
            messages.error(request, 'o campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not campo_vazio(email):
            messages.error(request,'o campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha_nao_sao_iguais(senha, confSenha):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists(): #verificando se o usuário já existe
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists(): #verificando se o nome já existe
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha) #cadastrando usuário na base de dados
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, 'Os campos email e senha não podem ficar em branco!')
            return redirect('login')
       
        if User.objects.filter(email=email).exists(): #verificando se o email existe
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() #trazendo o username associado ao email
            user = auth.authenticate(request, username=nome, password=senha) 
            if user is not None: #autenticacao de fato
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request,'Email ou senha inválidos')
                return redirect('login')
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

#organizando as funções que se repetem
def campo_vazio(campo):
    return campo.strip()
def senha_nao_sao_iguais(senha, senha2):
    return senha != senha2