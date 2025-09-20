import streamlit as st
from classifier import classify
from responder import build_reply

st.title("Conversation Tailor Bot")
goal = st.selectbox("Business goal", ["schedule a call","collect email","confirm donation","book demo",""])
user_text = st.text_area("User message")
if st.button("Tailor Reply"):
    if user_text.strip():
        meta = classify(user_text)
        reply, cta = build_reply(user_text, goal, meta["style"])
        st.write(f"**Detected:** style={meta['style']} | sentiment={meta['sentiment']} | tone={meta['tone']}")
        st.markdown(f"**Reply:** {reply}")
        st.markdown(f"**CTA:** {cta}")
    else:
        st.info("Type a message to get a tailored reply.")
