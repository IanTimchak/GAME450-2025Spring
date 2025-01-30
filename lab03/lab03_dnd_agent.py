from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Ian Timchak'
model = 'deepseek-r1:1.5b'
options = {'temperature': 0.5, 'max_tokens': 300}
messages = [
  {'role': 'system', 'content': 'You are a D&D agent. You should be able to interact with players as Dungeon Master. \
                                Your responses should be in the context of a SpellJammer campaign session. \
                                Start from the beginning of the campaign at the start of the message history. \
                                Compared to a table top game, this should operate more as a text-based adventure game. \
                                '},
  {'role': 'assistant', 'content': 'You are a player in a SpellJammer campaign. You are in the city of Waterdeep.'}
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
roundCounter = 0
while True:
  # Add your code below
  roundCounter+=1
  print(roundCounter)
  response = chat(model=model, messages=messages, stream=False, options=options)

  print(f'DM: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

