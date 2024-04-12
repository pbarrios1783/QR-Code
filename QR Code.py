import streamlit as st
import qrcode
import io
import base64


def generate_qr_code(content):
    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)

    # Create in-memory buffer to save QR code image
    qr_code_buffer = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_buffer, format='PNG')

    return qr_code_buffer.getvalue()

def main():
    st.title('QR Code Generator')

    # Get content for QR code from user input
    content = st.text_area('Enter the content for your QR code:')
    if st.button('Generate QR Code'):
        # Generate QR code
        qr_code_image = generate_qr_code(content)

        # Display QR code
        st.image(qr_code_image, caption='QR Code')

        # Download QR code image
        st.markdown(get_binary_file_downloader_html(qr_code_image, file_name='qr_code.png'), unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_name='QRCode'):
    # Convert image to base64 and create download link
    bin_str = base64.b64encode(bin_file).decode()
    href = f'<a href="data:image/png;base64,{bin_str}" download="{file_name}">Download QR Code</a>'
    return href

if __name__ == '__main__':
    main()
