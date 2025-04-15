import unittest
from src.cv.video_processing import process_video

class TestVideoProcessing(unittest.TestCase):

    def test_process_video_valid(self):
        video_path = 'src/data/sample_videos/sample_video.mp4'
        processed_frames = process_video(video_path)
        self.assertIsInstance(processed_frames, list)
        self.assertGreater(len(processed_frames), 0)

    def test_process_video_invalid(self):
        video_path = 'invalid/path/to/video.mp4'
        with self.assertRaises(FileNotFoundError):
            process_video(video_path)

if __name__ == '__main__':
    unittest.main()