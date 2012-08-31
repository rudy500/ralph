# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from django.http import HttpResponse

from ralph.ui.views.common import Base
from ralph.dnsedit.models import DHCPServer

class Index(Base):
    template_name = 'dnsedit/index.html'
    section = 'dns'

    def __init__(self, *args, **kwargs):
        super(Index, self).__init__(*args, **kwargs)


def dhcp_synch(request):
    address = request.META['REMOTE_ADDR']
    server = DHCPServer.get_or_create(ip=address)
    server.last_synchronized = datetime.datetime.now()
    return HttpResponse('OK', content_type='text/plain')
