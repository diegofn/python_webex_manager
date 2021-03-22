#!/usr/bin/env python
# coding: utf-8

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:flask_webex_manager.sock'
umask = 0o007
reload = True

#logging
accesslog = '-'
errorlog = '-'
