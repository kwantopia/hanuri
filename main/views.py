# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib import messages

from main.models import BrokenRelationKorean, BrokenRelationEnglish
from main.forms import BrokenRelationKoreanForm, BrokenRelationEnglishForm

import hashlib


def home(request):

  data = {}

  data["hanuri_project"] = _("Hanuri Project")
  data["hanuri_title_ko"] = u"한우리 모임"  # unicode(quopri.decodestring("한우리 모임"), encoding="iso_8859-2")
  data["hanuri_title_en"] = u"One Together Gathering"

  ko_form = BrokenRelationKoreanForm(request.POST or None, prefix="ko")
  en_form = BrokenRelationEnglishForm(request.POST or None, prefix="en")

  print "Submitted form: %s" % request.POST.get('submit')

  if request.POST.get('submit', None) == 'Korean':
    if ko_form.is_valid():
      # save form
      entry = ko_form.save(commit=False)
      entry.remote_addr = request.META.get('REMOTE_ADDR', None)
      entry.user_agent = request.META.get('HTTP_USER_AGENT', None)
      # some hash of IP address and user-agent
      entry.remote_id = hashlib.sha224(request.META.get('REMOTE_ADDR', None)
                                      + request.META.get('HTTP_USER_AGENT', None)).hexdigest()
      entry.remote_host = request.META.get('REMOTE_HOST', None)
      entry.referrer = request.META.get('HTTP_REFERRER', None)
      entry.save()
      messages.success(request, "이야기를 나눠주셔서 감사합니다.")
      ko_form = BrokenRelationKoreanForm(None, prefix="ko")
  else:
    ko_form = BrokenRelationKoreanForm(None, prefix="ko")

  if request.POST.get('submit', None) == 'English':
    if en_form.is_valid():
      entry = en_form.save(commit=False)
      # some hash of IP address and user-agent
      entry.remote_id = hashlib.sha224(request.META.get('REMOTE_ADDR', None)
                                      + request.META.get('HTTP_USER_AGENT', None)).hexdigest()
      entry.remote_addr = request.META.get('REMOTE_ADDR', None)
      entry.remote_host = request.META.get('REMOTE_HOST', None)
      entry.user_agent = request.META.get('HTTP_USER_AGENT', None)
      entry.referrer = request.META.get('HTTP_REFERRER', None)
      entry.save()
      messages.success(request, "Thank you for sharing your story.")
      en_form = BrokenRelationEnglishForm(None, prefix="en")
  else:
    en_form = BrokenRelationEnglishForm(None, prefix="en")

  data['ko_form'] = ko_form
  en_form.initial = {'country': 234}
  data['en_form'] = en_form

  return render_to_response("main/home.html", data, RequestContext(request))


def recent(request):
  """
    Recent posts
  """
  data = {}

  data["ko_posts"] = BrokenRelationKorean.objects.all().order_by('-timestamp')
  data["en_posts"] = BrokenRelationEnglish.objects.all().order_by('-timestamp')

  return render_to_response("main/recent.html", data, RequestContext(request))


def contact(request):
  """
    Contact page
  """
  data = {}

  return render_to_response("main/contact.html", data, RequestContext(request))


def contribute(request):
  """
    Contribute page
  """
  data = {}

  return render_to_response("main/contribute.html", data, RequestContext(request))
