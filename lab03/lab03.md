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
I tried swapping to deepseak-r1:1.5b for faster response times. The result is a hilariously bad attempt at talking to the player, like really bad. It was magnitudes worse in terms of quality.