from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="KINGDOMS: Seven Sins", layout="wide")

# Let the presentation scale its stage to the space above the game link.
st.markdown(
    """
    <style>
    [data-testid="stMainBlockContainer"] {
        max-width: none;
        padding: 0.5rem 1rem 1rem;
    }
    [data-testid="stHeader"] { display: none; }
    iframe[title="st.iframe"] { height: 85vh; height: 85dvh; }
    </style>
    """,
    unsafe_allow_html=True,
)

presentation = Path(__file__).with_name("presentation.html").read_text(encoding="utf-8")
components.html(presentation, height=720, scrolling=False)
st.link_button(
    "Play Weather Islands on Roblox",
    "https://www.roblox.com/games/80518464244305/Weather-Islands",
)
