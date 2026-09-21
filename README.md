# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [The Games purpose is to have the user, depending on the difficulty, guess the randomly generated number within a certain range and number of attempts.] Describe the game's purpose.
- [I found that the game innacurately displayed the range in which the random number could be in, did not properly reset when new game was pressed, and did not show higher or lower hints as expected according to the guess values] Detail which bugs you found.
- [I removed the code that related to changing the guess number to a string every even guess attempt, fixed the UI code to ask for a high and low value instea of just usin 0 to 100, and added status and other reset code that was needed in order to reset the game properly ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enter a value of 25
2. Game Returns "Too High"
3. User enters a guess of 3 -> "Too Low"
4. Score updates correctly after each guess
5. Hint Displays correct message based on guess
6. UI dispays correct range and difficulties and range/attempts match up logically
7. Game ends after the correct guess
8. Game properly resets after "New Game" button is pressed


## 🧪 Test Results

```
============================================ test session starts ============================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Sandh\Documents\gameglitchinvestigator\ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
plugins: anyio-4.14.2
collected 4 items                                                                                            

tests\test_game_logic.py ....                                                                          [100%]

============================================= 4 passed in 4.51s =============================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
