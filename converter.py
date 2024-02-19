from PIL import Image

def image_to_byte_array(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to grayscale
    img = img.convert('L')

    # Convert the image to a byte array
    byte_array = img.tobytes()

    return byte_array, img.width, img.height

def byte_array_to_image(byte_array, width, height, output_path):
    # Create a new image with the given width and height
    img = Image.frombytes('L', (width, height), byte_array)

    # Save the image in PNG format
    img.save(output_path)

    # Display the image (optional)
    img.show()

def save_byte_array_to_txt(byte_array, output_path):
    # Save the byte array to a text file
    with open(output_path, 'wb') as file:
        file.write(byte_array)

def read_byte_array_from_txt(input_path, width, height):
    # Read the byte array from a text file
    with open(input_path, 'rb') as file:
        byte_array = file.read()

    return byte_array

# User Input
input_type = input("Enter 'image' for image path or 'byte' for byte array file: ").lower()

if input_type == 'image':
    # User inputs image path
    image_path = input("Enter the path to the image file: ")

    # Convert image to byte array
    byte_array, width, height = image_to_byte_array(image_path)

    # Save byte array to a text file
    save_byte_array_to_txt(byte_array, 'output_byte_array.txt')

elif input_type == 'byte':
    # User inputs byte array file path
    byte_array_path = input("Enter the path to the byte array file (.txt): ")

    # Read byte array from text file
    byte_array = read_byte_array_from_txt(byte_array_path, width, height)

    # Convert byte array back to image and save it as PNG
    byte_array_to_image(byte_array, width, height, 'output_image.png')

else:
    print("Invalid input type. Please enter 'image' or 'byte'.")
