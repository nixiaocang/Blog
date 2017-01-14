#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handler.base_handler import BaseHandler
from model.blog import BlogModel


class SaveHandler(BaseHandler):

    def do_action(self):
        args = self.get_args([
            ('title', str, None),
            ('description', str, None),
            ('content', str, None),
        ])
        print args
        self.result = args
        return True
