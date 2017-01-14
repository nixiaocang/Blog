#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from handler.base_handler import BaseHandler
from model.blog import BlogModel
from urllib import unquote


class DeleteHandler(BaseHandler):

    def do_action(self):
        args = self.get_args([
            ('text_id', str, None),
        ])
        text_id = args['text_id']
        BlogModel().delete(text_id)
        self.result = 'success'
        return True
