import argparse
import logging
import os
import qrcode

# Set up logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(log_dir, "app.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def generate_qr_code(url: str, output_dir: str = "qr_codes") -> str:
    """Generate a QR code image for the given URL and save it to output_dir."""
    os.makedirs(output_dir, exist_ok=True)

    # Create a safe filename from the URL
    safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_").replace(".", "_")
    filename = f"{safe_name}.png"
    filepath = os.path.join(output_dir, filename)

    logger.info(f"Generating QR code for URL: {url}")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    logger.info(f"QR code saved to: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument(
        "--url",
        type=str,
        default="http://github.com/kaw393939",
        help="The URL to encode in the QR code"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="qr_codes",
        help="Directory to save generated QR codes"
    )
    args = parser.parse_args()

    logger.info("QR Code Generator started")
    filepath = generate_qr_code(args.url, args.output_dir)
    logger.info(f"Done! QR code generated at: {filepath}")


if __name__ == "__main__":
    main()
