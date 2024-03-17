from PIL import Image

ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 30]
    return ascii_str

def main(image_path, output_width=100):
    try:
        image = Image.open(image_path)

        image = resize_image(image, output_width)

        image = grayscale_image(image)

        ascii_str = pixels_to_ascii(image)

        ascii_str_len = len(ascii_str)
        ascii_img = ''
        for i in range(0, ascii_str_len, output_width):
            ascii_img += ascii_str[i:i+output_width] + '\n'
            
        f = open("out.txt", "w")
        f.write(ascii_img)
        f.close()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    image_path = 'Images/testImage.png'
    output_width = 100
    main(image_path, output_width)
    print("check out.txt file")