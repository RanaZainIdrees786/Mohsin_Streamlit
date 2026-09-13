import streamlit as st
import cv2
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.write("hello this is a new line")

st.text_input("Your name", key="name")

# You can access the value at any point with:
# st.session_state.name
st.write(f"The name you entered is {st.session_state.name}",)


import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (0.0, 75.0)
)


left_column, center_column, right_column = st.columns(3)
# You can use a column just like st.sidebar
btn = left_column.button('Press me!')

if(btn):
    st.write('button is clicked')

with center_column:
    st.text_input("Your email", key="email")
    img = cv2.imread('my.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img)
    
with right_column:
    right_col_sel = st.selectbox(
    'How would you want your order to be delivered?',
    ('TCS', 'M&P', 'Leopard Courier')
    )