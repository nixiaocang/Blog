#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handler.base_handler import BaseHandler
from model.blog import BlogModel


class ListHandler(BaseHandler):

    def do_action(self):
        args = self.get_args([
            ('user_id', str, None),
        ])
        res = BlogModel().get(args['user_id'])
        self.result = res
        return True
