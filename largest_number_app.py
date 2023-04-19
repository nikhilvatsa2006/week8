import streamlit as st

st.title("Find the largest among 3 numbers")

# Input numbers
num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)
num3 = st.number_input("Enter the third number", value=0, step=1)

# Calculate the largest number
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Button to find the largest number
if st.button("Find the largest number"):
    largest_number = find_largest(num1, num2, num3)
    st.write(f"The largest number is {largest_number}.")