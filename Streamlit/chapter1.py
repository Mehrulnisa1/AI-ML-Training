import streamlit as st


st.title("Hello Mehr")
st.subheader("AI/ML Intern")
st.text("Welcome to your Ist interactive app")
st.write("Choose your fav food")

chai= st.selectbox("Your fav Chai:" , ["Masala Chai", "Adrak Chai", "Lemon tea"])
st.write(f'You choose {chai}. Excellent choice')
st.success("Your chai has been brewed")