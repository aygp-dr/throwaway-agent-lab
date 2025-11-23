import qrcode

# Complex generation that would require a complex API schema in MCP
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction
    box_size=20,
    border=2,
)
qr.add_data("https://github.com/aygp-dr/throwaway-agent-lab")
qr.make(fit=True)

img = qr.make_image(fill_color="darkblue", back_color="white")
img.save("/output/complex_qr.png")
