import streamlit as st
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("image.png")

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("data:image/png;base64,{img}");
    background-size: contain;   /* Shows full image */
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: transparent;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)


    
st.markdown(
    """
    <style>
    .praween-font {
        font-family: 'Courier New', Courier, Montserrat;
        font-size: 24px;
        color: #D9380F
;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="praween-font">ORGANIC GROCERY MARKET</p>', unsafe_allow_html=True
)


import streamlit as st
import qrcode
from PIL import Image


import streamlit as st

# Custom CSS to set background color
page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #F2EEED
; /* Replace with your desired color code */
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
"""

st.markdown(page_bg_color, unsafe_allow_html=True)

# ... (Rest of your code goes here)
import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

# Initialize session state with unique, safe names
if 'cart_items' not in st.session_state:
    st.session_state.cart_items = []
    st.session_state.cart_prices = []
    st.session_state.cart_qtys = []
if 'temp_scanned_item' not in st.session_state:
    st.session_state.temp_scanned_item = ''

st.title("ORGANIC GROCERY MARKET")

# 1. Barcode Scanner - Placed outside the form
if st.button("Open Barcode Scanner"):
    scanned_data = qrcode_scanner(key='barcode_scanner')
    if scanned_data:
        st.session_state.temp_scanned_item = scanned_data
        st.rerun() 

# 2. Billing Form
with st.form("billing_form", clear_on_submit=True):
    # Using the scanned data to fill the input box
    item = st.text_input("Enter Item Name:", value=st.session_state.temp_scanned_item)
    price = st.number_input("Enter Price:", min_value=0.0, format="%.2f")
    qty = st.number_input("Enter Quantity:", min_value=1, step=1)
    submitted = st.form_submit_button("Add Item")

    if submitted and item:
        st.session_state.cart_items.append(item)
        st.session_state.cart_prices.append(price)
        st.session_state.cart_qtys.append(qty)
        st.session_state.temp_scanned_item = '' # Clear the scanner cache

# 3. Display the Bill
if st.session_state.cart_items:
    st.subheader("BILL")
    total = 0
    # Use the new safe names here
    for i in range(len(st.session_state.cart_items)):
        amount = st.session_state.cart_prices[i] * st.session_state.cart_qtys[i]
        total += amount
        st.write(f"{st.session_state.cart_items[i]} | Qty: {st.session_state.cart_qtys[i]} | Price: ₹{st.session_state.cart_prices[i]:.2f}")
    
    st.write("---")
    st.write(f"*Total Amount: ₹{total:.2f}*")
    import streamlit as st
import qrcode
from PIL import Image

# Define the data you want in the QR code
data = "https://www.google.com"

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")

# Display in Streamlit
st.title("QR Code Generator")
st.image("my_qr_code.png", caption="Scan me!")

st.image(r"D:\html\praveen 0305\image.png", caption="my image")