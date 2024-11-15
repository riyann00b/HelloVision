# HelloVision
---

**HelloVision** is a Python-based facial detection and greeting system powered by OpenCV and pyttsx3. It detects faces in real-time using a webcam, displays a glowing bounding box around detected faces, and greets each person with an audible "Hello!" message. 

---

## 🎯 Features

- **Cross-Platform Compatibility**: Works seamlessly on Linux, Windows, and macOS.
- **Real-Time Detection**: Uses OpenCV for fast and efficient facial detection.
- **Interactive Greeting**: Greets each face audibly using a TTS engine (pyttsx3).
- **Customizable Visuals**: Glowing bounding boxes and greeting text for a modern interface.
- **Lightweight**: Requires minimal resources to run.

---

## 🚀 Getting Started

### Prerequisites

1. Python 3.7+ installed on your system.
2. Install required libraries:
   ```bash
   pip install opencv-python pyttsx3 numpy
   ```

3. Ensure your webcam is accessible, and permissions are set correctly.

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HelloVision.git
   cd HelloVision
   ```

2. Run the script:
   ```bash
   python main.py
   ```

---

## ⚙️ Configuration

Customize the behavior by modifying the variables in the script:

- `GREETING_COOLDOWN`: Set the delay (in seconds) between repeated greetings.
- `BOX_COLOR`: Change the bounding box color (default is green).
- `TEXT_COLOR`: Change the greeting text color (default is white).

---

## 🖼️ Preview

<img src="https://via.placeholder.com/800x400?text=Demo+Image" alt="Demo Image" style="width: 100%; border: 1px solid #ccc;"/>

---

## 🌟 How It Works

1. **Facial Detection**: The system uses OpenCV’s Haar cascade classifier to detect faces in real-time.
2. **Greeting Logic**: Greets each face only once while it’s visible.
3. **TTS Integration**: Provides an audible greeting using pyttsx3.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🧑‍💻 Author

**Your Name**  
- GitHub: [@riyan00b](https://github.com/yourusername)
- Email: riyannazeer786@gmail.com
- LinkedIn: [MD Riyan Nazeer](https://linkedin.com/in/yourprofile)
