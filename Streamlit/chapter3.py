import streamlit as st

st.title ("Chai Taste Poll")

col1, col2 =st.columns(2)

with col1:
     st.header("Masala Chai")
     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_TfbUH3nQ4fs59rK35FgBB3ipYX-gZ-qTDJlKSID-aA&s=10" ,width=200)
     vote1=st.button("Vote Masala Chai")
with col2:
     st.header("Adrak Chai")
     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8pTt_8QuUyUXAdRuIy95Oa3dtg3EZv1VJkga9V4Yc8A&s=10", width =200)
     vote2=st.button("Vote Adrak Chai")

if vote1:
      st.success("Thankyou for choosing Masala Chai")
elif vote2:
     st.success("Thankyou for choosing Adrak Chai")


name=st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai:", ["Masala", "Kesar", "Adrak"])
st.write(f"Welcome {name} ad our {tea} chai is getting ready")

with st.expander("Show Chai Making Instructions"):
     st.write("""
     1.Boil Water with tea leaves.
     2.Add Milk & Spices.
     """)

st.markdown('### Welcome to Chai App')
st.markdown('>blockquote')