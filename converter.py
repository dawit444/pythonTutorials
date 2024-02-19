from PIL import Image

def image_to_bits(image_path):
  image = Image.open(image_path)
  pixels = image.load()
  bit_string = ""

  for y in range(image.height):
    for x in range(image.width):
      r, g, b = pixels[x, y]
      r_bits = format(r, '08b')
      g_bits = format(g, '08b')
      b_bits = format(b, '08b')
      pixel_bits = r_bits + g_bits + b_bits
      bit_string += pixel_bits

  return bit_string

# Example usage
image_path = r"C:\Users\GAEDC\Downloads\silence.jpg"
bit_string = image_to_bits(image_path)

# Further processing or saving the bit_string as needed
print(bit_string)  # Print the first 100 bits for example
