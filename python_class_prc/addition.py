import streamlit as st
st.set_page_config(page_title="Number Addition",page_icon="➕",layout="centered")
st.title("Addition of Two Number")
st.caption("Enter Two number and it will return addition of them")
form=st.form("add_from")
num1=form.number_input("First Number")
num2=form. number_input("Second Number")
submitted=form.form_submit_button("Calculate sum")

if submitted:
  result=num1+num2
  st.divider()
  st.metric(label="Result",value=result)

for i in range (1,11):
  st.write(f"2 X {i} =",{2*i})

