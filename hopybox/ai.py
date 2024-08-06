# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123 (hostudio.hopybox@foxmail.com).
'''

import cohere

from .prompt import getpass
from .prompt import color_input
from .prompt import color_print
from .prompt import error_cross_simple

class CoralAI:      
    @property
    def _chat(self):
        self.api_key = getpass('Please enter the secret key (See <u>https://dashboard.cohere.com/api-keys</u> for more details)\n','#00ABFF',html=True)
        self.co = cohere.Client(api_key=self.api_key)
        self.chat_history = list()
        color_print('Welcome to chat with Coral AI ! (Continue:^C) (Exit:^D)','#49D07D')
        while True:
            try:
                message = color_input('(You) ','#EB7A16')
                if not message.strip():
                    continue
                self._process(message)
            except EOFError:
                break
            except KeyboardInterrupt:
                continue
            except Exception as e:
                error_cross_simple(e)
        
    def _process(self,message):
        data_user = dict()
        data_bot = dict()
        stream = self.co.chat_stream(chat_history=self.chat_history,message=message)
        data_user['role'] = 'USER'
        data_user['message'] = message
        data_bot['role'] = 'CHATBOT'
        res_message = list()
        is_output = 0
        for event in stream:
            if event.event_type == "text-generation":
                if is_output == 0:
                    text = [
                    ('class:head','(Bot)'),
                    ('',' '),
                    ('class:text',event.text)
                    ]
                    style = {
                    'head':'#FFD142'
                    }
                    color_print(text,style,single=False,end='')
                    is_output = 1
                else:
                    print(event.text,end='')
                res_message.append(event.text)
        data_bot['message'] = ''.join(res_message)
        self.chat_history.append(data_user)
        self.chat_history.append(data_bot)
        print()

coral = CoralAI()