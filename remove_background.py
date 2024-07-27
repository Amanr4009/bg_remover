import cv2
import numpy as np
from rembg import remove

# Load the image
image_path = 'nameLogo.png'
image = cv2.imread(image_path)

# Convert the image from BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Remove the background
result = remove(rgb_image)

# Convert the result back to BGR for saving with OpenCV
result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)

# Save the result
output_path = "output_image.png"
cv2.imwrite(output_path, result_bgr)

# Display the result
cv2.imshow('Segmented Image', result_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Background removed image saved as {output_path}")
