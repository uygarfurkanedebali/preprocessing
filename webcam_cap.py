import cv2
import tempfile
import os

def frame_capture(frame):
    # Video dosyasını okumak için VideoCapture objesi oluşturuyoruz


    # Eğer kare alındıysa

        # Geçici bir dosya oluştur 

        temp_dir = tempfile.mkdtemp()
        save_path = os.path.join(temp_dir, "frame.jpg")
        
        # Kareyi geçici dosyaya kaydet
        cv2.imwrite(save_path, frame)
        # print(f"Frame kaydedildi: {save_path}")

    # VideoCapture objesini serbest bırak


        return save_path

# Örnek kullanım

