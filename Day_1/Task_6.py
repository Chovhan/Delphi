from PIL import Image
import numpy as np


def get_image_array(path):
    image = Image.open(path)
    return np.asanyarray(image)


def calculate_pixels(image_array):
    white, black, gray = 0, 0, 0
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            for z in range(len(image_array[i][j])):
                if image_array[i][j][z] == 0:
                    black += 1
                elif image_array[i][j][z] == 255:
                    white += 1
                else:
                    gray += 1
    return [white, black, gray]


func = calculate_pixels(get_image_array('image.jpg'))
print("White: " + str(func[0]) + "\nBlack: " + str(func[1]) + "\nGray: " + str(func[2]))
