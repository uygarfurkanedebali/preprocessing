import cv2
import face_recognition
from webcam_cap import frame_capture 
import shutil,tempfile,os

cap = cv2.VideoCapture(r'assets\ev.mp4')
folder = r'C:\Users\uygar\Desktop\Codding\dataset_preprocessing\assets'
i = 0
count = 0
name = 'uygar'
# Sonsuz bir döngü içinde webcam görüntüsünü al ve ekranda göster
while True:
    # Webcam'den bir kare al
    
    ret, frame = cap.read()
    if count % 15 ==0:
        
        temp_dir = tempfile.mkdtemp()
        temp_path = os.path.join(temp_dir, "frame.jpg")
        cv2.imwrite(temp_path, frame)
        image = face_recognition.load_image_file(temp_path)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 1:
            shutil.copy(temp_path,f'{folder}\\{name}_{i}.jpg')
            print('yüz bulundu ve dosya kaydedildi')
            i +=1
        elif len(face_locations) > 1:
            print('birden fazla yüz bulundu tekrar deneyiniz')
            print(len(face_locations))
        else:
            pass
        
        # print('yüz bulunamadı')
    # Kare alınamadıysa döngüyü kır
    if not ret:
        break

    # Alınan kareyi göster
    cv2.imshow('Webcam', frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    count +=1

# Döngüden çıktıktan sonra VideoCapture objesini serbest bırak
cap.release()
cv2.destroyAllWindows()

