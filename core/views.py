from django.shortcuts import render, redirect
from core.models import Ativos,User
from core.forms import AtivosForm,ManutencaoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from core.models import Manutencoes



def index(request):
    return render(request, 'index.html')


def lista_ativos(request):
    ativos = Ativos.objects.order_by('-id')[:10]
    return render(request, 'lista_ativos.html', {'ativos': ativos})

def adicionar_ativo(request):
    if request.method == 'POST':
        imob = request.POST.get('imob')
        local = request.POST.get('local')
        setor = request.POST.get('setor')
        responsavel = request.POST.get('responsavel')
        tipo = request.POST.get('tipo')
        modelo = request.POST.get('modelo')
        win = request.POST.get('win')
        chave_win = request.POST.get('chave_win')
        mac = request.POST.get('mac')
        mac_wifi = request.POST.get('mac_wifi')
        office = request.POST.get('office')
        chave_office = request.POST.get('chave_office')
        obs = request.POST.get('obs')

        # Aqui você pode criar um objeto ou salvar os dados em algum lugar
        # por exemplo:
        novo_ativo = Ativos(
            imob=imob,
            local=local,
            setor=setor,
            responsavel=responsavel,
            tipo=tipo,
            modelo=modelo,
            win=win,
            chave_win=chave_win,
            mac=mac,
            mac_wifi=mac_wifi,
            office=office,
            chave_office=chave_office,
            obs=obs
        )
        novo_ativo.save()

        return redirect('lista-ativos')
    else:
        form = AtivosForm()
    return render(request, 'adicionar_ativo.html', {'form': form})


def editar_ativo(request, ativo_id):
    ativo = Ativos.objects.get(id=ativo_id)

    if request.method == 'POST':
        form = AtivosForm(request.POST, instance=ativo)
        if form.is_valid():
            form.save()
            return redirect('lista-ativos')
    else:
        form = AtivosForm(instance=ativo)

    return render(request, 'editar_ativo.html', {'form': form, 'ativo': ativo})


def excluir_ativo(request, id):
    ativo = Ativos.objects.get(id=id)
    if request.method == 'POST':
        ativo.delete()
        return redirect('lista-ativos')
    return render(request, 'excluir_ativo.html', {'ativo': ativo})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página desejada após o login
                return redirect('base')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def cadastros_view(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()

            # Redirecionar para outra página após o cadastro bem-sucedido
            return redirect('login')
    else:
        form = User()

    return render(request, 'cadastro.html', {'form_usuario': form})


def pesquisar_ativos(request):
    if request.method == 'GET':
        imob = request.GET.get('imob')

        # Realizar a pesquisa de ativos por 'imob'
        ativo = Ativos.objects.filter(imob__icontains=imob).first()

        # Renderizar o template com o resultado da pesquisa
        return render(request, 'busca.html', {'ativo': ativo, 'pesquisa': imob})

    return render(request, 'base.html')


def lista_manutencoes(request):
    manutencoes = Manutencoes.objects.all()
    return render(request, 'manutencoes_list.html', {'manutencoes': manutencoes})



def adicionar_manutencao(request):
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            manutencoes = form.save()  # Salva a manutenção no banco
            return redirect('lista-manutencoes')  # Redireciona para a lista de manutenções ou outra página desejada
    else:
        form = ManutencaoForm()

    return render(request, 'adicionar_manutencao.html', {'form': form})


