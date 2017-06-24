"""votingbooth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from booth.views import *
from votepage.views import *
from votepage_new.views import showitem as new_item

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^session/(?P<session_id>\d+)/(?P<el_id>\d+)/(?P<item_id>\d+)$', open_session),
    url(r'^session/(?P<session_id>\d+)/(?P<el_id>\d+)/(?P<item_id>\d+)/next$', next_vote),
    url(r'^session/(?P<session_id>\d+)/(?P<el_id>\d+)/(?P<item_id>\d+)/prev$', prev_vote),
    
    url(r'^session/(?P<session_id>\d+)/general/(?P<el_id>\d+)$', general_vote),
    

    url(r'^session/(?P<session_id>\d+)/(?P<el_id>\d+)$', overview_el),
    url(r'^session/(?P<session_id>\d+)$', overview),
    url(r'^session/(?P<session_id>\d+)/$', redirect_open_session),

    url(r'^session/(?P<session_id>\d+)/(?P<el_id>\d+)/mgmt$', mgmt_el),
    url(r'^session/(?P<session_id>\d+)/mgmt$', mgmt),
    url(r'^session/(?P<session_id>\d+)/out\.csv$', get_file),

    url(r'^session/(?P<session_id>\d+)/criteria$', criteria),

    url(r'^session/(?P<session_id>\d+)/login', login),

    url(r'^session/(?P<session_id>\d+)/vote', vote),

    url(r'^s/(?P<section_id>\w+)/(?P<field>\d+)', showitem),
    url(r'^s/(?P<section_id>\w+)', showitem),
    
    url(r'^sn/(?P<section_id>\w+)/(?P<field>\d+)', new_item),
    url(r'^sn/(?P<section_id>\w+)', new_item),
]
