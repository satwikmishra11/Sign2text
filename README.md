# HackKRMU3 Hackathon Project: Sign2Text - Sign Language Translation Application

![Screenshot Of Sign2Text](https://ather.om-mishra.com/downloads/Sign2Text.jpeg)

## Notice: Accuracy Fluctuation

**Important Notice:** Please be aware that the accuracy of Sign2Text may fluctuate significantly under varying camera and lighting conditions. Factors such as poor lighting, camera angle, and background clutter can affect the performance of the hand gesture detection and translation model. While Sign2Text strives to provide accurate translations, it is essential to consider environmental conditions when using the application.

## Instructions to Run Sign2Text

Sign2Text is a web-based application that utilizes computer vision and machine learning to translate sign language gestures into text. The application is designed to be user-friendly and accessible to a wide audience. To run Sign2Text on your local system, follow the instructions below:

**Step 1: View on browser** [https://sign2text.om-mishra.com/home](https://sign2text.om-mishra.com/home)
    

**Step 1: Clone the Repository**
```bash
git clone <repository_url>
cd Sign2Text
```

**Step 2: Install Dependencies**
Ensure you have Python installed on your system. Then, install the required Python libraries using pip:
```bash
pip install opencv-python mediapipe tensorflow Flask
```

**Step 3: Run the Application**
```bash
cd Application
python app.py
```

**Step 4: Access the Web Interface**
Open a web browser and navigate to `http://localhost:5000` to access the Sign2Text application.

**Step 5: Upload an Image**
Upload an image containing sign language gestures using the provided interface.

**Step 6: View Translated Text**
Once the image is uploaded, Sign2Text will process it, detect the sign language gestures, and display the translated text on the web page.

**Step 7: Consider Environmental Factors**
Please keep in mind that Sign2Text's accuracy may vary based on environmental factors such as lighting conditions and camera quality. Ensure adequate lighting and minimize background clutter for optimal performance.

**Step 8: Provide Feedback**
We value your feedback! If you encounter any issues or have suggestions for improvement, please don't hesitate to reach out to us.

## Team Information
Sign2Text was developed by the following team members during the HackKRMU Hackathon:
- Om Mishra
- Laxman Singh
- Bharat Bhushan
- Satwik Mishra

## Conclusion
Thank you for the amazing opportunity to participate in the HackKRMU3 Hackathon. We are excited to present Sign2Text and look forward to your feedback and suggestions. We hope that Sign2Text will help bridge the communication gap between the hearing-impaired and the general population, making the world a more inclusive and accessible place for everyone utilizing the untapped potential of AI and computer vision.
