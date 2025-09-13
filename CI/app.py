import streamlit as st

st.title("Calculator App")
st.write("This is a simple calculator app built with Streamlit.")

def add(a, b):
    return a + b        
def subtract(a, b): 
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

num1 = st.number_input("Enter first number:", value=0)
num2 = st.number_input("Enter second number:", value=0)
operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    st.write(f"The result is: {result}")