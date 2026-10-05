import streamlit as st


st.title("chai maker app")
if st.button("make chai"):
    st.success("chai is being made")
 
add_masala = st.checkbox("Add masala")
if add_masala:
    st.write("Masala added to your chai!")
tea_type= st.radio("Select tea type:", ("Green Tea", "Black Tea", "Herbal Tea"))
st.write(f"You selected: {tea_type}.")
flavor=st.selectbox("Select flavor:", ["Mint", "Lemon", "Ginger"])
st.write(f"You selected: {flavor} flavor.")
sugar=st.slider("Select sugar level:", 0, 10, 5)
st.write(f"You selected: {sugar} sugar level.")
cups =st.number_input("how many cups of tea?", min_value=1, max_value=10, step=1)
st.write(f"You selected: {cups} cups of tea.")                    
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Your chai is being prepared.")
dob=st.date_input("Enter your date of birth:")
st.write(f"Your date of birth is: {dob}.")