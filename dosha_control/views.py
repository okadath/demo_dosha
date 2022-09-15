from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_django,authenticate, login, logout
from django.contrib.auth.decorators import login_required
from extended_user.auth import IDPasswordlessAuth, EmailPasswordlessAuth, UsernamePasswordlessAuth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
# def login(request):
#     context_dict={}
#     print(request.user)
#     return render(request, 'index.html', context_dict)




def login_func(request):
    # print(request.POST)
    context_dict={}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('ventas'))

    if request.method == 'POST':
        try:
            user = IDPasswordlessAuth.authenticate(
                id_user=request.POST['id_user'] 
            )
        except Exception as e: 
            context_dict["error_messages"]="no se pudo loguear, contactar soporte tecnico y brinde id de usuario y demas datos"
            return HttpResponseRedirect(reverse('/'))

        if user:
            if user.is_active:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('ventas'))
            # elif user.profile.is_producer or user.profile.is_director:
            #     login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            #     return HttpResponseRedirect(reverse('eng_partner_home'))
            else:
                context_dict["error_messages"]="cuenta inactiva, contacte soporte tecnico"
                return render(request, 'index.html',  context_dict)
        else:
            context_dict["error_messages"]="los datos proporcionados son incorrectos"
            return render(request, 'index.html',  context_dict)
    else:
        if request.user.is_anonymous == True:
            return render(request, 'index.html', context_dict)
        else:
            # return render(request, 'index.html', context_dict)
            # return redirect('eng_home')
            return HttpResponseRedirect(reverse('ventas'))


@login_required(login_url="/")
def ventas(request):
    context_dict={}
    print(request.user)
    return render(request, 'ventas.html', context_dict)

@login_required(login_url="/")
def recompensas(request):
    context_dict={}
    print(request.user)
    return render(request, 'recompensas.html', context_dict)

@login_required(login_url="/")
def registra_venta(request):
    pass

def logout(request):
    print("deslogueado")
    logout_django(request)
    return redirect('login_func')