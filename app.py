import streamlit as st
import pandas as pd

st.title("Automatic Night Light Monitoring")

light = st.slider(
    "Analog Sensor Reading",
    0, 1023, 300
)

st.metric("Sensor Reading", light)

# TASK 2: Change the threshold to 500
if light > 600:
    st.warning("DARK: LED ON")
else:
    st.success("BRIGHT: LED OFF")

data = pd.DataFrame({
    "Reading": [300, 500, 550, 750]
})

st.dataframe(data)
st.line_chart(data.set_index(pd.Index(range(1, 5))))
