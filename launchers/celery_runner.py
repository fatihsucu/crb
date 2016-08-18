# -*- coding: utf8 -*-
import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/../'))

import configs
conf = configs.get()
print sys.path

from app.app import createCeleryApp

application = createCeleryApp(conf)
