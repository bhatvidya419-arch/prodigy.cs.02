from PIL import Image

def process_image(image_path, key, output_path):
    """
    Encrypts or decrypts an image by applying an XOR operation to each pixel.
    """
    try:
        # Load the image
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        # Iterate through every pixel
        for y in range(height):
            for x in range(width):
                # Get the RGB values of the current pixel
                r, g, b = pixels[x, y]

                # Apply mathematical operation (XOR with key)
                # This changes the data and makes it unreadable
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        # Save the result
        img.save(output_path)
        print(f"Success! Image saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# User Interaction
def main():
    print("--- Simple Image Encryption Tool ---")
    choice = input("Enter 'E' to Encrypt or 'D' to Decrypt: ").upper()
    path = input("Enter the image file path (e.g., input.jpg): ")
    key = int(input("Enter a numeric key (0-255): "))
    output = "encrypted_image.png" if choice == 'E' else "decrypted_image.png"

    process_image(path, key, output)

if __name__ == "__main__":
    main()
