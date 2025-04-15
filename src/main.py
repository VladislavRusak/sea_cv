import cv2
from cv.video_processing import process_video
from cv.angle_calculation import calculate_angle
from utils.logger import setup_logger
from utils.config import load_config

def main():
    setup_logger("main", "main.txt")
    config = load_config()
    
    video_path = config['video_path']
    frames = process_video(video_path)
    
    for i in range(len(frames) - 1):
        frame1 = frames[i]
        frame2 = frames[i + 1]
        angle, visualized_frame = calculate_angle(frame1, frame2, visualize=True)
        
        print(f"Calculated angle: {angle}")
        
        # Отображение кадра с визуализацией
        cv2.imshow("Docking Visualization", visualized_frame)
        
        # Закрытие окна при нажатии клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()