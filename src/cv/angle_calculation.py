import cv2
import numpy as np

def calculate_angle(frame1, frame2, visualize=False):
    # Преобразование в HSV и выделение красных объектов
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Поиск контуров
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = []

    for contour in contours:
        # Фильтрация по размеру (например, площадь меньше 5000 пикселей)
        area = cv2.contourArea(contour)
        if 1 < area < 50:  # Условие для швартовых столбов
            filtered_contours.append(contour)
    
    # Определение центров швартовых столбов
    centers = []
    for contour in filtered_contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            centers.append((cx, cy))
            if visualize:
                cv2.circle(frame1, (cx, cy), 5, (255, 0, 0), -1)  # Отметка центра
    
    # Построение прямой причала
    if len(centers) >= 2:
        centers = sorted(centers, key=lambda x: x[0])  # Сортировка по X
        x_coords, y_coords = zip(*centers)
        line = np.polyfit(x_coords, y_coords, 1)  # Линейная регрессия
        slope, intercept = line
        
        # Визуализация прямой
        if visualize:
            height, width = frame1.shape[:2]
            x1, y1 = 0, int(intercept)
            x2, y2 = width, int(slope * width + intercept)
            cv2.line(frame1, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Пример вычисления угла между кораблем и причалом (заглушка)
        angle = 0  # Здесь должна быть логика вычисления угла
    else:
        angle = None  # Если недостаточно точек для построения прямой
    
    if visualize:
        # Наложение текста с углом
        angle_text = f"Angle: {angle:.2f}" if angle is not None else "Angle: N/A"
        cv2.putText(frame1, angle_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return angle, frame1
    
    return angle