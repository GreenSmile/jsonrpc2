# This file is part of Json-RPC2.
#
# Copyright (C) 2012 Marcin Lyko
# All rights reserved.
#
# Json-RPC2 is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Json-RPC2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Json-RPC2; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''
Defintion of a logger for Json-RPC classes and functions.
'''

import logging

LOG_FORMAT = '%(asctime)s [%(name)s] %(filename)s:%(lineno)d - %(message)s'

LOG_FUNCS = ['debug', 'info', 'warning', 'error', 'exception', 'critical']

_logger = None

def _log(*args, **kwargs):
    '''
    The fake logging function.
    '''
    pass

def setup(level=None):
    '''
    Sets up a logger instance with the given logging level.
    '''
    global _logger

    if _logger:
        return

    if level is None:
        level = logging.INFO

    formatter = logging.Formatter(LOG_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    _logger = logging.getLogger('Json-RPC2')
    _logger.addHandler(handler)
    _logger.setLevel(level)

    for name in LOG_FUNCS:
        globals()[name] = getattr(_logger, name)


if _logger is None:
    for name in LOG_FUNCS:
        globals()[name] = _log

