import streamlit as st
import streamlit.components.v1 as components
st.title("🏛️ منصة الدرعية الذكية - واجهة Framer")
# ضع رابط Framer الخاص بك هنا
framer_url = "https://your-project-link.framer.app/"
# عرض موقع Framer داخل الداشبورد
components.iframe(framer_url, width=1200, height=800, scrolling=True)
