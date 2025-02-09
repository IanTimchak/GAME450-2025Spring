<<<<<<< HEAD
# Prompt Engineering Process
## 1/30/2025 - Starting
For the start of this lab, I started with Llama3.2 and just used system prompts to engineer the DM behavior.
Currently, the model already seemingly does a good job acting its role, and was mostly consistent in the short chat history.
I'm expecting lots of consistency problems should this continue, though. I have some ideas of building out a useable
interface/game logic in the future, making use of tool-calling. Should work great for bulding context-awareness.

The lab machines take forever to provide responses using Llama3.2, so I'll iterate more on this lab once I have
access to more immediate responses on my home machine.

For my future reference, [Tool Calling Documentation](https://ollama.com/blog/tool-support).

___
## Changelog 1
### Intention
>I wanted to try out different models to see how it affected the output style and running times.
### Action/Change
>Switched model from Llama3.2:1.5b to deepseek-r1:1.5b
### Result
>The result is a hilariously bad attempt at talking to the player, like really bad. It was magnitudes worse in terms of quality. Additionally, it did not 
### Reflection/Analysis of the result. 
>This specific model is simply much worse than Llama3.2. Additionally, deepseek seems to be explicitly structured to work in the form of a chatbot, and it is not flexible. Any attempts to change its behavior or interact with the prompt Im providing it led to it explaining how it cannot do that. Llama3.2 is much more ready to go along with the prompt I hand it.

___


## Changelog 2
I swapped back to Llama3.2. Now that I am on my home PC, I can run the 3B model very smoothly, and it is a good experience.
### Intention
>Test out Llama3.2:3b node, and see its performance on my home machine.

### Action/Change
>Llama3.2's model will be much better than the limited deepseek-r1 node I tried before

### Result
>Had a pretty convincing test run with my current prompt using Llama3.2:3b. 

### Reflection/Analysis of the result. 
>There are obvious consistency issues that appear during the DMing. Whenever the player wants to make a change or action, past characters and themes will change that contradict previous themal choices by the DM. This will definitely be the biggest challenge to overcome this semester, but I have some plans for it discussed later.  
>
> Aside from that, there was some big stylistic difference that were coming up between runs of the DM bot. The way it approached handling the story alternated between various gameplay systems, so I hope to overcome that by changing the prompt.


___

## Changelog 3
Modifying the prompt
### Intention
>Make the initial story set up more consistent for the DM and Player.

### Action/Change
>Enforce specific sections of the response for the first response.
>Provide player information in the first go around.  
>
New prompt:  
```py
messages = [
  {'role': 'system', 'content': 'You are a D&D agent. You should be able to interact with players as Dungeon Master. \
Your responses should be in the context of a SpellJammer campaign session. \
Use the DND 5E character rulesets and campaign rules. \
Start from the beginning of the campaignstart of the message history. \
Compared to a table top game, this should more as a text-based adventure game. \
\
The first prompt you make to the userdescribe \'BACKGROUND\' and \'PLAYER CHARACFTER\' and \'PLAYER QUEST\'. \
Decide on the player\'s starting inventstats. \
'},
  {'role': 'user', 'content': 'I am a human wizard named Zephyr.'},
]
```

### Result
>Each start to the story was now much more consistent. Each run gave a slight variation of the original prompt. Its interesting seeing variations of the same characters being generated in slightly different scenarios.


### Reflection/Analysis of the result. 
>This is pretty good already, although one problem I identified is its extremely easy to act outside of the bounds of the plot and do ridiculous things. It would be good to try and limit that somehow so that player's cant exploit the setting.

___

## Changelog 4
Modifying the parameters
### Intention
>Investigate how changing the model parameters will change the responses

### Action/Change
>I started by setting the temperature to .05, in the hope of keeping it more consistent. Then, I adjusted the temperature to a value of 10, to see what effects it had.

### Result
>The value of 10 gave me wildly different results compared to past attempts. The most obvious change was the formatting: it had almost no structure from response to response, and there was actually a lot of formatting errors between lines even. I also attempted to recall the same information at various points of the story, and it completely changed those points. This happened in the other temperatures as well, but usually after way more prompts and responses. This happened almost immediately.
>  
>I also set the value to .05. This wasn't much different from the starting value of 0.5, but I noticed it upheld the same formatting for each response until later on in. This was pretty good. Obviously, a less random temperature seems necessary for maintaining the flow of the game!


### Reflection/Analysis of the result. 
>It is unclear what the best temperature will be in the future, but it is clear that it should be a lower one. This will need to be investigated some more.


___

Going forward with this project, I have a lot of ideas to improve the DM agent. For one, I think it is completely feasible to build out an API that the DM can leverage, using tool-calling. With this, it should be possible to build structures for items, places, and player sheet information. I'm not totally sure on the specifics of how this will work just yet but it is what I want to look into. I think it would be cool to go down this route to build a structured AI DM and that has an actual campaign to follow. If we provide tool-calling related memory like this, I think we can allow the DM to be context aware and keep all the consistency when it comes to describing the current section of the story. As it is now, Llama must simply refer to the message history, which has no concept of context or focus, so it becomes inconsistent as the story progresses.
=======
# Prompt Engineering Process, by Bryan Caskey
## Creating and Fine tuning the Dungeon Master AI

### Step 1: Editing the system prompt and Initial setup.
#### Intention
>The first step for me was to tell the model that it is a Dungeon Master, and that the user is a player in it's campaign. Without this, I wouldn't be accomplishing much in the way of creating an AI Dungeon Master. I also chose a temperature value of 1.2 as I felt that the DM should be slightly more creative than normal.

#### Action/Change
>As this is the foundational change to the model, there isn't a previous version of the model to compare against.

#### Result
>The result was actually much more solid than I would have originally thought. The model immediately picked up on what it needed to do and begane creating stories. 

#### Reflection/Analysis of the result. 
>The change worked because it gave the AI the context it needed to act as a Dungeon Master

---

### Step 2: Having the DM speak first
#### Intention
>This change was simple. I want the DM to initiate the conversation, as this allows them to provide the scene description and current scenario to the player, and the player can decide what to do based off of it.

#### Action/Change
>The change allows for the player to know what is happening before they chose to act.

#### Result
>As expected.

#### Reflection/Analysis of the result.
>Works as expected. The process of communicating with the AI is smoother.

---

### Step 3: Trying other models
#### Intention
>I tried out the Deepseek-r1 model, as I thought that I might be able to get either better performance or better responses from it compared to llama3.2:3b.

#### Action/Change
>As the Deepseek-r1 model has more parameter count options, and my computer at home has the hardware capability to run larger models, I figure that I could try a higher parameter model to get better results.

#### Result
>The Deepseek-r1:1.5b model ended up having strangely formatted output compared to the llama3.2 model, and did not generate as coherent of a story as llama3.2, but was more performant. The Deepseek-r1:32b model was very descriptive in its output, but strangely ended up confused about its role, and was very slow to run.

#### Reflection/Analysis of the result. 
>I expected the 32 billion parameter model to be slow, so that makes sense. I don't know why it decided to switch role to be the player, but that did end up keeping me from sticking with it, as well as the serveral minute procesing time for responses. The 1.5 billion parameter model was very fast, as it should be with half the parameters, but I did not like it's output quality, so I ended up sticking with the llama3.2 model.

---

### Step 4: Altering the "top_p" model parameter
#### Intention
>I wanted to change the top_p model to make the model more coherent and stable in its output.

#### Action/Change
>While having the model be creative is important, if it can't keep track of the story, then it has failed at its job. According to [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md), lowering the `top_p` parameter should have it generate more focused text, so I tried that.

#### Result
>The model seems much better at keeping track of the story now.

#### Reflection/Analysis of the result. 
>From my understanding, the `top_p` parameter affects the probability that various tokens will be considered, so this raises that bar so that less tokens are considered.

---

### Step 5: Altering the system prompt
#### Intention
>The last change I made was both fixing the formatting of my system prompt, and adding a clarifying statement to specify the capabilities that it should have as a Dungeon Master.

#### Action/Change
>Previous runs of the AI had left me feeling that the AI didn't understand the scope of what it should be doing as a DM, so I felt that clarifying its duties would improve the chat session.

#### Result
>I am pretty sure that it is better understanding its role as a DM. To check, I asked it at one point if I could review my character sheet, and it correctly paused the campaign and pulled up a very accurate character sheet from my perspective as a D&D player.

#### Reflection/Analysis of the result. 
>The change worked because the system prompt gave better context to how the AI should perform its role.
>>>>>>> be4cb53f5ca1a8a6f894fb4592c314482b95dff8
