import cv2

def create_video_from_image(image_path, output_video_path, frame_count=30, frame_duration=1):
    # Resmi oku
    image = cv2.imread(image_path)

    # Resim boyutlarını al
    height, width, _ = image.shape

    # VideoWriter objesi oluştur
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, frame_count/frame_duration, (width, height))

    # Resmi frame_count kere videoya ekle
    for _ in range(frame_count):
        out.write(image)

    # VideoWriter objesini serbest bırak
    out.release()

    print(f"Video oluşturuldu: {output_video_path}")

# Örnek kullanım
image_path = r"C:\Users\uygar\Desktop\Codding\dataset_preprocessing\assets\uygarr.jpg"
output_video_path = r"C:\Users\uygar\Desktop\Codding\dataset_preprocessing\assets\uygarr.mp4"
create_video_from_image(image_path, output_video_path)

# import cv2

# def merge_images(image1_path, image2_path, output_path):
#     # İlk resmi oku
#     image1 = cv2.imread(image1_path)
#     height1, width1, _ = image1.shape

#     # İkinci resmi oku
#     image2 = cv2.imread(image2_path)
#     height2, width2, _ = image2.shape

#     # İki resmi yan yana birleştir
#     merged_image = cv2.hconcat([image1, image2])

#     # Birleştirilmiş resmi kaydet
#     cv2.imwrite(output_path, merged_image)
#     print(f"İki resim birleştirilerek kaydedildi: {output_path}")

# # Örnek kullanım
# image1_path = r"C:\Users\uygar\Desktop\Codding\dataset_preprocessing\assets\uygar.jpg"
# image2_path = r"C:\Users\uygar\Desktop\Codding\dataset_preprocessing\assets\uygar.jpg"
# output_path = r"C:\Users\uygar\Desktop\Codding\dataset_preprocessing\assets\uygarr.jpg"
# merge_images(image1_path, image2_path, output_path)

