from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForm

# Create your views here.


def home(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for joining')
        return HttpResponseRedirect('/thankyou/')

    return render_to_response("signup.html",
                              locals(),
                              context_instance = RequestContext(request)
                              )


def thankyou(request):
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance = RequestContext(request)
    )