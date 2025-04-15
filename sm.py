import streamlit as st
import re

def check_strength(password):
    score = 0
    criteria = {
        "Length >= 8": len(password) >= 8,
        "Has Uppercase": bool(re.search(r'[A-Z]', password)),
        "Has Lowercase": bool(re.search(r'[a-z]', password)),
        "Has Digit": bool(re.search(r'\d', password)),
        "Has Special Character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    for passed in criteria.values():
        if passed:
            score += 1

    return score, criteria

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, results = check_strength(password)

    st.subheader("Strength Criteria:")
    for key, passed in results.items():
        st.write(f"{'✅' if passed else '❌'} {key}")

    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }

    st.subheader(f"Strength: {strength_levels[score]}")
    st.progress(score / 5)
