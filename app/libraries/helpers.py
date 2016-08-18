# -*- coding: utf8 -*-
from flask import request, jsonify, abort, Response
import functools


def jsonize_request():
    if request.method != 'GET':
        datatype = request.headers.get("Content-Type", None)
        if not datatype:
            abort(404)
        elif "application/x-www-form-urlencoded" in datatype:
            data = dict(request.form)
            for each in data.keys():
                data[each] = data[each][0]
        elif "application/json" in datatype:
            data = dict(request.json)
        else:
            abort(400)
        return data
    else:
        data = dict(request.args.items())
        return data


def jsonizeRequest(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        data = jsonize_request()
        kwds['data'] = data
        return f(*args, **kwds)

    return wrapper

