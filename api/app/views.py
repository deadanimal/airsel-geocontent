# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django import template
from .forms import UserCreateForm, RoleUpdateForm, GeotagCreateForm, GeotagUpdateForm
from .models import Role, Geotag

@login_required(login_url="/login/")
def index(request):
    geotags = Geotag.objects.all()
    context = {'geotags':geotags}
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def map(request):
    geotag_form = GeotagCreateForm()
    geotags = Geotag.objects.all()
    if request.method == 'POST':
        geotag_form = GeotagCreateForm(request.POST, request.FILES or None)
        if geotag_form.is_valid():
            geotag_form.save()
            return redirect('map')
    context = {'geotag_form':geotag_form, 'geotags':geotags}
    return render(request, "map.html", context)

@login_required(login_url="/login/")
def map_edit(request,id):
    geotag = Geotag.objects.get(id=id)
    geotag_form = GeotagUpdateForm(instance=geotag)
    if request.method == 'POST':
        if 'edit' in request.POST:
            geotag_form = GeotagUpdateForm(request.POST, request.FILES or None, instance=geotag)
            if geotag_form.is_valid():
                geotag_form.save()
                messages.success(request, 'Successfully Edited')
                return redirect('map')
            else:
                messages.warning(request, 'Unable to edit : ' + geotag_form.errors.as_text())
                return redirect('map')
        if 'delete' in request.POST:
            geotag.delete()
            messages.success(request, 'Successfully Deleted')
            return redirect('map')
    context = {'geotag_form':geotag_form, 'geotag':geotag}
    return render(request, "map-update.html", context)

@login_required(login_url="/login/")
def api(request):
    return render(request, "api.html")

@login_required(login_url="/login/")
def user(request):
    form_user = UserCreateForm()
    if request.method == 'POST':
        if 'delete' in request.POST:
            id = request.POST["id"]
            user = get_object_or_404(User, id=id)
            user.delete()
            messages.success(request, 'Successfully Deleted')
        if 'edit' in request.POST:
            id = request.POST["id"]
            user = get_object_or_404(User, id=id)
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.email = request.POST["email"]
            user.save()
            messages.success(request, 'Successfully Edited')
        if 'create' in request.POST:
            form_user = UserCreateForm(request.POST)
            if form_user.is_valid():
                form_user.save()
                messages.success(request, 'Successfully Created')
            else:
                messages.warning(request, 'Invalid Information: ' + form_user.errors.as_text())
                return redirect('user')

        return redirect('user')
    users = User.objects.all()
    context = {'users':users,'form_user':form_user}
    return render(request, "user.html", context)
    
@login_required(login_url="/login/")
def role(request):
    form_role = RoleUpdateForm()
    if request.method == 'POST':
        if 'update' in request.POST:
            role = get_object_or_404(Role, id=request.POST["id"])
            form_role = RoleUpdateForm(request.POST,instance=role)
            if form_role.is_valid():
                form_role.save()
                messages.success(request, 'Successfully Updated')
        return redirect('role')

    roles = Role.objects.all()
    context = {'roles':roles,'form_role':form_role}
    return render(request, "role.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
