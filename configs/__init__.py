# -*- coding: utf8 -*-
import os
import sys
import default


def get(env=None):

    # inserting the current directory into the the path
    sys.path.insert(
        0,
        os.path.join(os.path.abspath(os.path.dirname(__file__))))

    conf = default.Config()

    return conf
