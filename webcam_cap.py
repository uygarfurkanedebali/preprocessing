import cv2
import tempfile
import os

def frame_capture(frame):


        temp_dir = tempfile.mkdtemp()
        save_path = os.path.join(temp_dir, "frame.jpg")
        

        cv2.imwrite(save_path, frame)





        return save_path

# Örnek kullanım

