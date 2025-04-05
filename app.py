import streamlit as st
import random

def number_guessing_game():
    st.title("🎯 Number Guessing Game+")
    
    # Initialize session state
    if "target" not in st.session_state:
        reset_game()

    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Game Settings")
        
        # Custom range selector
        min_val, max_val = st.slider(
            "Select number range:",
            min_value=1,
            max_value=1000,
            value=(1, 100),
            key="range"
        )
        
        # Difficulty level
        difficulty = st.radio(
            "Difficulty levels:",
            ["😊 Easy (Unlimited)", "😐 Medium (15 attempts)", "😰 Hard (5 attempts)"],
            index=0
        )
        
        if st.button("🔄 New Game"):
            reset_game()
            st.rerun()

    # Main game area
    st.subheader(f"Guess between {st.session_state.range[0]} and {st.session_state.range[1]}")
    
    # Display remaining attempts if not easy mode
    if difficulty != "😊 Easy (Unlimited)":
        max_attempts = 15 if "Medium" in difficulty else 5
        remaining = max_attempts - st.session_state.guesses
        st.caption(f"Attempts remaining: {remaining}")
        
        if remaining <= 0:
            st.error(f"❌ Game Over! The number was {st.session_state.target}")
            st.session_state.game_over = True

    # Game logic
    if not st.session_state.game_over:
        guess = st.number_input(
            "Your guess:",
            min_value=st.session_state.range[0],
            max_value=st.session_state.range[1],
            step=1
        )
        
        if st.button("🎯 Submit Guess"):
            st.session_state.guesses += 1
            
            if guess < st.session_state.target:
                st.error(f"Too low! 📉 (Guess #{st.session_state.guesses})")
            elif guess > st.session_state.target:
                st.error(f"Too high! 📈 (Guess #{st.session_state.guesses})")
            else:
                st.success(f"🎉 You won in {st.session_state.guesses} guesses!")
                st.balloons()
                st.session_state.game_over = True
                
                # Save high score
                if st.session_state.guesses < st.session_state.get("best_score", 999):
                    st.session_state.best_score = st.session_state.guesses
                    st.balloons()

    # Display best score if available
    if "best_score" in st.session_state:
        st.markdown(f"🏆 **Best score:** {st.session_state.best_score} guesses")

def reset_game():
    """Reset all game variables"""
    st.session_state.target = random.randint(
        st.session_state.range[0] if "range" in st.session_state else 1,
        st.session_state.range[1] if "range" in st.session_state else 100
    )
    st.session_state.guesses = 0
    st.session_state.game_over = False

if __name__ == "__main__":
    number_guessing_game()