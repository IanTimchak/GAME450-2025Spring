from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
<<<<<<< HEAD
sign_your_name = 'Ian Timchak'
model = 'Llama3.2:3b'
options = {'temperature': 10, 'max_tokens': 300}
messages = [
  {'role': 'system', 'content': 'You are a D&D agent. You should be able to interact with players as Dungeon Master. \
                                Your responses should be in the context of a SpellJammer campaign session. \
                                Use the DND 5E character rulesets and campaign rules. \
                                Start from the beginning of the campaign at the start of the message history. \
                                Compared to a table top game, this should operate more as a text-based adventure game. \
                                \
                                The first prompt you make to the user should describe \'BACKGROUND\' and \'PLAYER CHARACTER\' and \'PLAYER QUEST\'. \
                                Decide on the player\'s starting inventory and stats. \
                                '},
  {'role': 'user', 'content': 'I am a human wizard named Zephyr.'},
]
=======
sign_your_name = 'Bryan Caskey'
model = 'llama3.2:3b'
options = {'temperature': 1.2,
           'top_p': 0.5}
messages = [{'role': 'system', 'content': 'You are a Dungeon Master of a D&D campaign. Your job \
is to provide the player with a detailed description of the current \
scenario they are in, and provide them with options for how they want \
to interact with the world. You should be able to generate a story, \
create NPC characters, manage the game world, make changes to player \
character sheets, and implement a turn-based combat system.'},
            {'role': 'assistant', 'content': 'You are a D&D player who is playing a character \
named "Thonk the Large" in the "Hoard of the Dragon Queen" campaign.'}]
>>>>>>> be4cb53f5ca1a8a6f894fb4592c314482b95dff8


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
roundCounter = 0
while True:
  # Add your code below
<<<<<<< HEAD
  roundCounter+=1
  print(roundCounter)
  response = chat(model=model, messages=messages, stream=False, options=options)

  print(f'DM: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
=======
  print(f'Dungeon Master: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})

>>>>>>> be4cb53f5ca1a8a6f894fb4592c314482b95dff8
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

