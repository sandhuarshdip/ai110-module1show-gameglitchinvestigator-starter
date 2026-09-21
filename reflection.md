# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game looked like a game where I was supposed to guess a secret number in a range of numbers within a preset amount of guesses depending on the diffuclty of my or any players choice.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - I notice that I was able to guess outside the range i was given and that the range on the actual game screen did not change no matter what difficulty i selected
    - I also noticed that the hints were not always accurate to what numbers i was inputting in relation to the secret number.
      often telling me to go higher or lower at random.
    - Also the "New Game" button does not do anything 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|     Input    |          Expected Behavior          | Actual Behavior |        Console Output / Error        |
|--------------|-------------------------------------|-----------------|--------------------------------------|
| guess of -1  |          "out of bound msg"         | "Go lower" hint |      should notify out of bounds     |
|press new game| guesses reset, secret number resets | nothing happens | "game over start a new game to reset |
|   guess 50   |     guess higher (secret is 60)     | "Go lower" hint |  |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  I asked the AI to check where i had tagged #FIXME for a problem with the higher lower function and the AI correctly suggested to remove the string conversion function that would convert every even attemt to a string.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  the first time i asked teh AI to suggest a fix to the higher lower function the AI suggested fixes to the entire code, which was out of scope for the problem i had asked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I read each line the AI was adding and removing and checked myself to see if the logic made sense and then via tests i asked the AI to set tests that tried higher lower guesses for the code.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    one test I ran was to see if the code would output higher correctly was to input a guess of 50 and lower for a secret value of 60 and make sure it always output "go higher" It showed me after my bug fixes that my code was running closer to my intended desire.
- Did AI help you design or understand any tests? How?
  yes ai redeisigned my tests, via me asking it to make tests based of the two bugs i targeted. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  streamlit was good, it seemed to run the game properly without any issues outside of the written code

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      I think one habit i would like to reuse is my tendancy to read the code altogether first to try and understand it as is before ever prompting the AI. And also using the "ASK" functionality of the chat to ask for questions before allowing it to make any changes or suggestions.
- What is one thing you would do differently next time you work with AI on a coding task?
    My initial suggestion was vague and allowed the AI to try and make changes throughout the code instead of telling it to look for the FIXME tags, in the future i would just start with more specific prompts.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  It made me realise AI generated code needs the help of a programmer for sure, especially once you start to get into more and more complicated tasks needing to be done. But with proper technique and skill it can be a helpfull tool to streamline work.
