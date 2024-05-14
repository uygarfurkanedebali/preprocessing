import cv2
import face_recognition
import shutil,tempfile,os

cap = cv2.VideoCapture(0)
# Görüntülerin toplanacağı klasörün pathini giriniz
folder = r''                    
os.makedirs(folder,exist_ok=True)
i = 0
count = 0
# Görüntülerin kaydedileceği ismi giriniz
name = ''    

while True:
    
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
        
    if not ret:
        break
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    count +=1

cap.release()
cv2.destroyAllWindows()

