from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Member
from django.shortcuts import get_object_or_404, redirect

def memberList(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
        'total_members': Member.objects.count(),
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    if request.method == 'POST':
        if 'delete' in request.POST:
            member = get_object_or_404(Member, id=id)
            member.delete()
            return HttpResponseRedirect(reverse('members'))
        else:
            member = get_object_or_404(Member, id=id)
            member.first_name = request.POST.get('first_name')
            member.last_name = request.POST.get('last_name')
            member.phone = request.POST.get('phone')
            member.email = request.POST.get('email')
            member.role = request.POST.get('role')
            member.save()
            return HttpResponseRedirect(reverse('members'))
    
    mymember = Member.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def add_member(request):
    if request.method == 'POST':
        member = Member(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            role=request.POST.get('role', 'Regular')
        )
        member.save()
        return HttpResponseRedirect(reverse('members'))
    
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def main(request):
    template = loader.get_template('main.html')
    context = {
        'total_members': Member.objects.count(),
    }
    return HttpResponse(template.render(context, request))