from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BlogPostModelForm,BlogCommentModelForm
from .models import BlogPostModel,BlogCommentModel

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request): 
    command_list = ['crea-post','lista-post']
    context = {
        'command_list': command_list,
    }
    return render(request, "blog/index.html", context)

class listaPostView(ListView):
    model = BlogPostModel #modello dei dati da utilizzare 
    template_name = "blog/lista_post.html"  #pagina per mostrare i dati
    
    #recupera di dati da passare alla pagina per il render
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context["posts"] = BlogPostModel.objects.all()
    #    return context

#class PostDetailView(DetailView):
    # model = BlogPostModel #modello dei dati da utilizzare 
    #template_name = "blog/post_detail.html" #pagina per mostrare i dati
def PostDetailView2(request, pk):
    post = get_object_or_404(BlogPostModel, id=pk)
    # Lista di commenti attivi per questo post
    comments = post.comments.filter(attivo=True)
    new_comment = None
    if request.method == 'POST':
        # il commento è stato inviato
        comment_form = BlogCommentModelForm(data=request.POST)
        if comment_form.is_valid():
            # creo l'oggetto commento ma non lo salvo ancora nel db
            new_comment = comment_form.save(commit=False)
            # metto in relazione il commento al post a cui si riferisce
            new_comment.post = post
            # metto in relazione il commento al suo autore
            new_comment.autore = request.user
            # Salvo il commento nel database
            new_comment.save()
    else:
        # preparo il form vuoto in cui scrivere il commento
        comment_form = BlogCommentModelForm()

    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form
               }
    return render(request, 'blog/post_detail.html', context)

#Modifica del post
def modificaPostView(request, pk=None):
    obj = get_object_or_404(BlogPostModel, pk=pk) #carico il post in base alla chiave primaria pk
    form = BlogPostModelForm(request.POST or None, instance=obj)  #passo l'oggetto post al form
    if request.method == 'POST': 
        if form.is_valid():
           form.save()
           return redirect('/blog/lista-post')
    context = {"form": form,"pk":pk} #creo i parametri
    return render(request, 'blog/modifica_post.html', context)

def eliminaPostView(request, pk=None):
    obj = get_object_or_404(BlogPostModel, pk=pk) #carico il post in base alla chiave primaria pk
    obj.delete()
    return HttpResponseRedirect("blog/lista-post")

@login_required(login_url='/accounts/login/')
#Creazione del post
def creaPostView(request):
    if request.method == "POST": 
        form = BlogPostModelForm(request.POST) #ottengo il form dalla richiesta
        if form.is_valid():     #validazione del form
            print("Il Form è Valido!")
            new_post = form.save(commit=False)  #creo il post ma non lo salva
            new_post.autore=request.user
            new_post.save()
            print("new_post: ", new_post)
            return HttpResponseRedirect("lista-post")
    else: #se la chiamata non è POST vuol dire che è la prima chiamata GET, quindi mostro il form vuoto
        form = BlogPostModelForm()
    context = {"form": form}   #contesto dei parametri da passare al render
    return render(request, "blog/crea_post.html", context)  #passo il form alla pagina per il render