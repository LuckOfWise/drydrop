# -*- mode: python; coding: utf-8 -*-
import logging
import google.appengine.ext.db as db
from drydrop.app.core.model import Model
from drydrop.lib.properties import JSONProperty, NiceDateTimeProperty

class Event(db.Expando, Model):
    author = db.StringProperty()
    date = NiceDateTimeProperty()
    code = db.IntegerProperty()
    action = db.StringProperty()
