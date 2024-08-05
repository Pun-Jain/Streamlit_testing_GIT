import streamlit as st
st.title('My To-do list creater')

if 'mylist' not in st.session_state:
    st.session_state.mylist=["Milk", "bread","onions"]
st.write('My current to-do list is:',st.session_state.mylist)
new_list=st.text_input("What do you need to do?")
if st.button('Add the new item'):
    st.write('Adding a new item to the list')
    st.session_state.mylist.append(new_list)
st.write('My new To-do list is:',st.session_state.mylist)