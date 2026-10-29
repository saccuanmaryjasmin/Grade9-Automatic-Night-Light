
import streamlit as st

st.set_page_config(
    page_title="Automatic Night Light",
    page_icon="💡",
    layout="centered"
)

st.title("💡 Automatic Night Light Monitoring System")
st.write(
    "Monitor the simulated light sensor reading "
    "and observe the LED status."
)

st.divider()

st.subheader("📊 Light Sensor Monitoring")

reading = st.slider(
    "Adjust Analog Sensor Reading",
    min_value=0,
    max_value=1023,
    value=300,
    step=1
)

st.metric("Analog Sensor Reading", reading)

if reading > 600:
    st.success("💡 LED STATUS: ON")
    st.warning("Dark condition detected. The LED is ON.")
    led_status = "ON"
    condition = "Dark condition"
else:
    st.info("☀️ LED STATUS: OFF")
    st.write("Bright condition detected. The LED is OFF.")
    led_status = "OFF"
    condition = "Bright condition"

st.divider()

st.subheader("🧪 Test Readings")

test_data = {
    "Analog Reading": [300, 600, 750],
    "Expected LED": ["OFF", "OFF", "ON"],
    "Condition": [
        "Bright condition",
        "Bright condition",
        "Dark condition"
    ]
}

st.table(test_data)

st.subheader("📈 Analog Reading Graph")
st.bar_chart(
    {"Analog Reading": [300, 600, 750]}
)

st.divider()

st.subheader("📝 Interpretation")
st.write(
    f"The current analog reading is {reading}. "
    f"The condition is {condition}, and the LED is {led_status}. "
    "The LED turns ON when the reading is greater than 600 "
    "and turns OFF when the reading is 600 or below."
)

st.subheader("Temperature Graph")

st.line_chart(
    data,
    y="Temperature"
)

st.subheader("Interpretation")

st.write(
    "The warning LED turns ON when the "
    "temperature reaches 40°C or higher. "
    "Below 40°C, the LED remains OFF."
)
