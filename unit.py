# new code 
# unit converter GIAIC Project
import streamlit as st

st.markdown("""
 <style>
  body {
        background-color:rgb(58, 66, 70);
        color:white;
 }
 .stApp {
        background: linear-gradient(135deg,rgb(100, 97, 97),rgb(233, 227, 227));
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.5);
 }
 .sidebar{
    background-color:rgb(16, 35, 56);
 }
 h1 {
        text-align: center;
        font-size: 36px;
        color:white;
        margin-bottom: 30px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
 }
 .stButton> button {
        background-color:rgb(77, 110, 146);
        color:white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        cursor:pointer;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
 }
 .stButton> button:hover {
        transform: scale(1.05);
        background-color: #0056b3;
 }
 .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color:rgb(146, 166, 187);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 2px 5px rgba(151, 76, 76, 0.2);
 }
 .result-box:hover {
        transform: scale(1.05);
        background-color:rgb(54, 98, 146);
 }
 .footer{
    text-align: center;
    font-size: 14px;
    color:rgb(22, 23, 24);
    margin-top: 20px;
 }
 </style>
 """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1> ✨Unit Converter</h1>", unsafe_allow_html=True)
st.write("Convert between different units of length, weight, and temperature")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Conversion options
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches", "Yards", "Miles"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches", "Yards", "Miles"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Yards": 1.09361,
        "Miles": 0.000621371
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Button for conversion
result = None  # Initialize result to avoid errors

if st.button("🤖Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

# Display result only if it's calculated
if result is not None:
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
else:
    st.warning("Please enter a valid value and click Convert.")

# Footer
st.markdown(f"<div class='footer'>Developed by Bushra Turk</div>", unsafe_allow_html=True)



