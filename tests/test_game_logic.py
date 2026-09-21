from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_new_game_resets_state():
    app = AppTest.from_file("app.py").run(timeout=10)

    app.text_input(key="guess_input_Normal").input("25")
    app.button[0].click().run(timeout=10)
    assert app.session_state.attempts == 1

    app.button[1].click().run(timeout=10)

    assert app.session_state.attempts == 0
    assert app.session_state.score == 0
    assert app.session_state.status == "playing"
    assert app.session_state.history == []
