import streamlit as st

class UnitConverter:
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        length_conversions = {
            "meter": 1,
            "kilometer": 0.001,
            "centimeter": 100,
            "millimeter": 1000,
            "inch": 39.3701,
            "foot": 3.28084,
            "yard": 1.09361,
            "mile": 0.000621371,
        }
        return value * (length_conversions[to_unit] / length_conversions[from_unit])

    @staticmethod
    def convert_weight(value, from_unit, to_unit):
        weight_conversions = {
            "kilogram": 1,
            "gram": 1000,
            "milligram": 1e6,
            "pound": 2.20462,
            "ounce": 35.274,
        }
        return value * (weight_conversions[to_unit] / weight_conversions[from_unit])

    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "kelvin":
                return value + 273.15
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                return (value - 32) * 5/9
            elif to_unit == "kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                return value - 273.15
            elif to_unit == "fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value  # Default if units are the same

def main():
    st.title("Professional Unit Converter")
    st.write("Convert between different units easily!")

    # Select conversion type
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature"],
        help="Choose the type of unit conversion you want to perform."
    )

    # Input value
    value = st.number_input(
        "Enter value to convert",
        value=1.0,
        min_value=0.0 if conversion_type in ["Length", "Weight"] else -273.15,
        help="Enter the numerical value you want to convert."
    )

    # Unit selection based on conversion type
    if conversion_type == "Length":
        units = ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile"]
    elif conversion_type == "Weight":
        units = ["kilogram", "gram", "milligram", "pound", "ounce"]
    elif conversion_type == "Temperature":
        units = ["celsius", "fahrenheit", "kelvin"]

    # Dynamic unit selection
    from_unit = st.selectbox("From unit", units, help="Select the unit to convert from.")
    to_unit = st.selectbox(
        "To unit",
        [unit for unit in units if unit != from_unit],
        help="Select the unit to convert to."
    )

    # Perform conversion
    try:
        if conversion_type == "Length":
            result = UnitConverter.convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = UnitConverter.convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = UnitConverter.convert_temperature(value, from_unit, to_unit)

        # Display result
        st.success(f"Converted value: {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    main()