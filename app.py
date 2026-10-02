"""Streamlit web interface for the calculator."""
import streamlit as st
from calculator import calculate, OPERATIONS

st.set_page_config(page_title="Python Calculator", page_icon="🧮")
st.title("🧮 Python Calculator")
st.caption("Shows the execution time of every calculation.")

col1, col2, col3 = st.columns([2, 1, 2])
a = col1.number_input("First number", value=0.0, format="%f")
op = col2.selectbox("Operator", list(OPERATIONS.keys()))
b = col3.number_input("Second number", value=0.0, format="%f")

if st.button("Calculate", type="primary"):
    try:
        result, elapsed = calculate(a, op, b)
        st.success(f"{a} {op} {b} = {result}")
        st.info(f"Execution time: {elapsed * 1e6:.2f} microseconds")
    except ZeroDivisionError as e:
        st.error(str(e))
