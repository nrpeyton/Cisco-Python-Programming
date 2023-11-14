import base64

def convert_image_to_base64(filepath):
    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

# Replace 'path_to_your_file' with the path to your favicon file
base64_data = convert_image_to_base64('/home/nick/Documents/ytfavicon.ico')
print(base64_data)



