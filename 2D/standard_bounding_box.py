import cv2
import json

# Đọc ảnh từ đường dẫn
image_path = r"C:\Users\nguye\Downloads\NGU\9bb4438bc0026b5c3213.jpg"
image = cv2.imread(image_path)

# Tạo cửa sổ hiển thị ảnh
cv2.namedWindow("Select Object")

# Biến lưu trữ tọa độ của điểm đầu và điểm cuối của bounding box
rectangles = []
current_rectangle = []

# Hàm callback khi chuột được nhấn
def on_mouse(event, x, y, flags, param):
    global current_rectangle

    # Nếu chuột được nhấn
    if event == cv2.EVENT_LBUTTONDOWN:
        current_rectangle = [(x, y)]

    # Nếu chuột được giữ và di chuyển
    elif event == cv2.EVENT_LBUTTONUP:
        current_rectangle.append((x, y))
        rectangles.append(tuple(current_rectangle))
        current_rectangle = []

# Đăng ký hàm callback cho sự kiện chuột
cv2.setMouseCallback("Select Object", on_mouse)

# Đợi người dùng kết thúc vẽ bounding box bằng cách nhấn phím bất kỳ
while True:
    # Hiển thị ảnh và bounding boxes
    img_with_rectangles = image.copy()
    for rectangle in rectangles:
        if len(rectangle) == 2:  # Make sure we have a valid rectangle
            cv2.rectangle(img_with_rectangles, rectangle[0], rectangle[1], (0, 255, 0), 2)

    cv2.imshow("Select Object", img_with_rectangles)

    # Chờ phím bấm
    key = cv2.waitKey(1) & 0xFF

    # Nếu phím "r" được bấm, làm mới bounding boxes
    if key == ord("r"):
        rectangles = []

    # Nếu phím "esc" hoặc "q" được bấm, thoát khỏi vòng lặp
    elif key == 27 or key == ord("q"):
        break

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()


# # In tọa độ của các bounding boxes
# for i, rectangle in enumerate(rectangles):
#     print(f"Bounding Box {i + 1}: {rectangle}")

# Lưu thông tin bounding boxes vào một tệp JSON
output_file_path = r"C:\Users\nguye\Downloads\bounding_boxes.json"

with open(output_file_path, 'w') as json_file:
    data = {'bounding_boxes': []}
    for i, rectangle in enumerate(rectangles):
        if len(rectangle) == 2:  # Make sure we have a valid rectangle
            x1, y1 = rectangle[0]
            x2, y2 = rectangle[1]
            data['bounding_boxes'].append({
                'id': i + 1,
                'x_min': min(x1, x2),
                'y_min': min(y1, y2),
                'x_max': max(x1, x2),
                'y_max': max(y1, y2),
            })

    json.dump(data, json_file, indent=4)

print(f"Bounding box information saved to {output_file_path}")