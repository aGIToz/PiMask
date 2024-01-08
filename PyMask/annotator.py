import cv2
import numpy as np

# Global variables
drawing = False  # True if mouse is pressed
ix, iy = -1, -1

# Mouse callback function
def annotate(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            color = (0, 0, 0)  # Black color
            cv2.circle(img, (x, y), 3, color, -1)

    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        color = (0, 0, 0)  # Black color
        cv2.circle(img, (x, y), 3, color, -1)


def create_mask(input_path, output_path):
    global img
    img = cv2.imread(input_path)
    img = np.where(img == 0, 1, img) # add noise
    cv2.namedWindow('image',cv2.WINDOW_GUI_NORMAL) # Qt backend assumption!
    cv2.setMouseCallback('image', annotate)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        
        # Press 's' to save the mask
        if k == ord('s'):
            img = (np.where(img == 0, 0, 255)).astype(np.uint8)
            cv2.imwrite('mask.png', img)
            print(f"Mask saved as '{output_path}'")
            break

        # Press 'esc' to exit
        elif k == 27:
            break

    cv2.destroyAllWindows()
