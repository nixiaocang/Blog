#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from handler.base_handler import BaseHandler
from model.blog import BlogModel
from urllib import unquote


class SaveHandler(BaseHandler):

    def do_action(self):
        args = self.get_args([
            ('title', str, None),
            ('description', str, None),
            ('content', str, None),
        ])
        text_id = self.get_argument('text_id', None)
        content = args['content']
        content=unquote(content)
        args['content'] = content
        if text_id is None:
            BlogModel().insert(args)
        else:
            BlogModel().update(text_id, args)
        self.result = args
        return True
