# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

import quopri

def home(request):

  data = {}

  data["hanuri_project"] = _("Hanuri Project")
  data["hanuri_title_ko"] = u"한우리 모임"  # unicode(quopri.decodestring("한우리 모임"), encoding="iso_8859-2")
  data["hanuri_title_en"] = u"One Together Gathering"

  return render_to_response("main/home.html", data, RequestContext(request))

def save_korean(request):

  data = {}

  return render_to_response("main/home.html", data, RequestContext(request))

def save_english(request):

  data = {}
  
  return render_to_response("main/home.html", data, RequestContext(request))