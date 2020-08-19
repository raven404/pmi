from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import get_template
from posts.models import Post, Author, PostView, Team, TeamView
from django.template import Context, Template, RequestContext
from subscribe.forms import EmailSignupForm
from subscribe.models import Signup
# from .forms import CommentForm, PostForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import datetime


now = datetime.datetime.now()
latest = Post.objects.order_by('-timestamp')[0:9]
# form = EmailSignupForm()

# Create your views here.


def about(request):
    return render(request, 'about.html', {'now': now, })


def financial_transparency(request):
    return render(request, 'financial_transparency.html', {'now': now, })


def family(request):
    return render(request, 'mission_Statement.html', {'now': now, })


def Nandlal_Community(request):
    return render(request, 'nandlal.html', {'now': now, })


def Bada_Bagh(request):
    return render(request, 'badabagh.html', {'now': now, })


def Campus_Engagement(request):
    return render(request, 'campus_engagement.html', {'now': now, })


def Awareness_Program(request):
    return render(request, 'awareness.html', {'now': now, 'latest': latest})


def Relief_Funds(request):
    return render(request, 'relief.html', {'now': now, 'latest': latest})


def Co_Curricular_Activities(request):
    return render(request, 'co_curricular.html', {'now': now, 'latest': latest})


def Child_Sponsorship_Program(request):
    return render(request, 'CSP.html', {'now': now, 'latest': latest})


def Field_Visit(request):
    return render(request, 'field_visit.html', {'now': now, 'latest': latest})


def Blanket_Drive(request):
    return render(request, 'blanket_drive.html', {'now': now, 'latest': latest})


def Medical_Camp(request):
    return render(request, 'medical_camp.html', {'now': now, 'latest': latest})


def media(request):
    return render(request, 'Media.html', {'now': now, 'latest': latest})


def chat_over_coffee(request):
    return render(request, 'COC.html', {'now': now, 'latest': latest})


def focal_point(request):
    return render(request, 'focalpoint.html', {'now': now, 'latest': latest})


def forums(request):
    return render(request, 'forums.html', {'now': now, 'latest': latest})


def music(request):
    return render(request, 'music.html', {'now': now, 'latest': latest})


def language(request):
    return render(request, 'language.html', {'now': now, 'latest': latest})


def Alumni(request):
    return render(request, 'Alumni.html', {'now': now, 'latest': latest})


def Internships(request):
    return render(request, 'Internship.html', {'now': now, 'latest': latest})


def Volunteer(request):
    return render(request, 'volunteers.html', {'now': now, 'latest': latest})


def donation(request):
    return render(request, 'Donation.html', {'now': now, 'latest': latest})


def Impact(request):
    return render(request, 'impact.html', {'now': now, 'latest': latest})


def Success_Stories(request):
    return render(request, 'Success_stories.html', {'now': now, 'latest': latest})


def contact(request):
    return render(request, 'contact.html', {'now': now, 'latest': latest})


def team(request):
    team = Team.objects.filter(
        categories__title__exact="team").order_by('-timestamp')
    context = {
        'team': team,
        'now': now,
        'latest': latest
    }

    return render(request, 'team.html', context)


def impact(request):
    impact = Team.objects.filter(
        categories__title__exact="impact").order_by('-timestamp')
    context = {
        'impact': impact,
        'now': now,
        'latest': latest
    }

    return render(request, 'impact.html', context)


def faqs(request):
    return render(request, 'FAQs.html', {'now': now, 'latest': latest})
