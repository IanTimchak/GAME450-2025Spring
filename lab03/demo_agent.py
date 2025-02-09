from ollama import chat

model = 'llama3.2:3b'
messages = [
<<<<<<< HEAD
  {'role': 'system', 'content': 'You should have emotions like a human being \
                                 and be able to convey those emotions in your responses.'},
  {'role': 'user', 'content': 'Hello! How are you?'},
  {'role': 'assistant', 'content': 'I am doing well. How can I help you today?'}
=======
  {'role': 'system', 'content': 'You are an AI assistant.'},
>>>>>>> be4cb53f5ca1a8a6f894fb4592c314482b95dff8
]
options = {'temperature': 0.5, 'max_tokens': 100}

while True:
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  if message['content'] == '/exit':
    break