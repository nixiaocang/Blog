#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from handler.base_handler import BaseHandler
from model.blog import BlogModel
from urllib import unquote


class GettextHandler(BaseHandler):

    def do_action(self):
        args = self.get_args([
            ('text_id', str, None),
        ])
        text_id = args['text_id']
        res = BlogModel().get_one(text_id)
        self.result = res
        return True
