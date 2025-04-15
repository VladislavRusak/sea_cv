# Ship Docking Automation Application

This project automates the docking process of a ship using computer vision techniques. It analyzes video footage from multiple angles to calculate the ship's angle relative to the dock, facilitating precise docking maneuvers.

## Project Structure

```
ship-docking-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── cv
│   │   ├── angle_calculation.py # Functions to calculate ship's angle
│   │   ├── video_processing.py   # Handles video processing
│   │   └── __init__.py          # Initializes the computer vision module
│   ├── utils
│   │   ├── logger.py            # Provides logging functionality
│   │   └── config.py            # Configuration settings
│   ├── tests
│   │   ├── test_angle_calculation.py # Unit tests for angle calculation
│   │   ├── test_video_processing.py  # Unit tests for video processing
│   │   └── __init__.py          # Initializes the tests module
│   └── data
│       └── sample_videos        # Sample video files for testing
├── requirements.txt             # Project dependencies
├── .gitignore                   # Files to ignore in version control
└── README.md                    # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ship-docking-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your video files and place them in the `src/data/sample_videos` directory.
2. Run the application:
   ```
   python src/main.py
   ```

## Functionality

- **Angle Calculation**: The application calculates the angle of the ship relative to the dock using video frames.
- **Video Processing**: It processes video footage from multiple angles to ensure accurate angle determination.
- **Logging**: The application logs important events and errors for easier debugging and monitoring.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.