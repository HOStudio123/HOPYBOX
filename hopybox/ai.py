import cohere

from .prompt import getpass
from .prompt import color_input
from .prompt import error_cross_simple

class CoralAI:      
    @property
    def _chat(self):
        self.api_key = getpass('Please enter the secret key (See <u>https://dashboard.cohere.com/api-keys</u> for more details)\n','#00ABFF',html=True)
        self.co = cohere.Client(api_key=self.api_key)
        self.chat_history = list()
        while True:
            try:
                message = color_input('(Coral) ','#FFD142')
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
        for event in stream:
            if event.event_type == "text-generation":
                print(event.text,end='')
                res_message.append(event.text)
        data_bot['message'] = ''.join(res_message)
        self.chat_history.append(data_user)
        self.chat_history.append(data_bot)
        print()

coral = CoralAI()