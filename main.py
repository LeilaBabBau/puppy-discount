from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP

TAX_RATE = Decimal('0.0825')
TAX_MULT = Decimal('1') + TAX_RATE

subtotal = Decimal(input("Enter original subtotal: ").replace(',', '').strip())
target_total = Decimal(input("Enter desired total (with tax): ").replace(',', '').strip())

pre_tax = (target_total / TAX_MULT).quantize(Decimal('0.01'))
discount = (subtotal - pre_tax).quantize(Decimal('0.01'))

print(f"\nNeeded pre-tax price: ${pre_tax}")
print(f"Discount to apply: ${discount} off your original subtotal")
