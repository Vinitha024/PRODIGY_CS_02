
from PIL import Image   # pip install Pillow
import os


def encrypt_decrypt_image(input_path: str, output_path: str, key: int) -> None:
      # Check if file exists
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    # Try opening the image
    try:
        img = Image.open(input_path).convert("RGB")  # make sure it's RGB
    except Exception as e:
        print("❌ Could not open image. Error:", e)
        return

    width, height = img.size
    pixels = img.load()  # access all pixels

    print(f"📏 Image size: {width} x {height}")
    print("🔄 Processing pixels... (may take a moment for large images)")

    # Go through each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  # original values

            # XOR each channel with the key
            r_new = r ^ key
            g_new = g ^ key
            b_new = b ^ key

            pixels[x, y] = (r_new, g_new, b_new)

    # Save the result
    try:
        img.save(output_path)
        print(f"✅ Done! Saved result as: {output_path}")
    except Exception as e:
        print("❌ Could not save image. Error:", e)


def ask_for_key() -> int:
       while True:
        key_text = input("Enter a numeric key (1–255): ").strip()

        if not key_text.isdigit():
            print("⚠ Please enter only digits (0–9).")
            continue

        key = int(key_text)
        if 1 <= key <= 255:
            return key
        else:
            print("⚠ Key must be between 1 and 255. Try again.")


def main():
    print("=== Image Encryption Tool (Pixel XOR) - Task 02 ===")
    print("1) Encrypt image")
    print("2) Decrypt image (use the same key used for encryption)")
    choice = input("Choose an option (1/2): ").strip()

    if choice not in ("1", "2"):
        print("❌ Invalid choice. Please run again and choose 1 or 2.")
        return

    input_path = input("Enter input image file name (e.g. input.png): ").strip()
    output_path = input("Enter output image file name (e.g. encrypted.png): ").strip()

    key = ask_for_key()

    # XOR is reversible, so same function works for both encrypt and decrypt
    encrypt_decrypt_image(input_path, output_path, key)


if __name__ == "__main__":
    main()
