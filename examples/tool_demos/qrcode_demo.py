# The agent "tool use" is simply this script
import qrcode

print("Generating QR Code for 'https://github.com/aygp-dr/throwaway-agent-lab'...")

# Create the QR object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/aygp-dr/throwaway-agent-lab')
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it to the virtual filesystem
output_path = "/output/repo_qr.png"
img.save(output_path)

print(f"Success! QR code saved to {output_path}")
