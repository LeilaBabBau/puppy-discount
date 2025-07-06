import streamlit as st
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP

TAX_RATE = Decimal('0.0825')
TAX_MULT = Decimal('1') + TAX_RATE

st.title("Puppy Price Discount Calculator 🐶")

subtotal_input = st.text_input("Enter original subtotal ($):", "5599")
target_total_input = st.text_input("Enter desired final price (with tax) ($):", "3800")

try:
    subtotal = Decimal(subtotal_input.replace(',', '').strip())
    target_total = Decimal(target_total_input.replace(',', '').strip())

    pre_tax = (target_total / TAX_MULT).quantize(Decimal('0.01'))
    discount = (subtotal - pre_tax).quantize(Decimal('0.01'))

    st.markdown(f"### 💸 Needed pre-tax price: **${pre_tax}**")
    st.markdown(f"### 🔻 Discount to apply: **${discount}** off your original subtotal")

except Exception:
    st.error("Please enter valid numbers for both fields.")
