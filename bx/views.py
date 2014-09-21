from django.http import HttpResponse
from django.template import Context,RequestContext,Template
from django.shortcuts import render_to_response,redirect
from bx.models import blog

def blog_create(request):
          print request.POST
          if request.method == "POST":
                    t = request.POST['a']
                    s = request.POST['b']
                    blog(title=t,content=s).save()
          return redirect("/list")

def blog_list(request):
          blogs = blog.objects.filter().order_by('-id')
          d = {'blogs':blogs}
          return render_to_response('list.html', d, context_instance=RequestContext(request))

def blog_delete(request,id):
          blog.objects.get(id=int(id)).delete()
          return redirect("/list")

def blog_update(request,id):
          b = blog.objects.get(id=int(id))
          d = {'b':b}
          return render_to_response('update.html',d,context_instance=RequestContext(request))

def blog_update_save(request,id):
          b = blog.objects.get(id=int(id))
          b.title = request.POST['a']
          b.save()
          return redirect("/list")
          
          
