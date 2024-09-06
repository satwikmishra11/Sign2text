import os
import cv2
import mediapipe
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify, redirect, render_template, url_for, session

# Import the model class
sign_language_detector_model = load_model("models/alpha/keras_model.h5", compile=False)
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'space']

mediapipe_hands = mediapipe.solutions.hands
hands = mediapipe_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)

mediapipe_drawing = mediapipe.solutions.drawing_utils

# Function to preprocess the input image
def preprocess_image(image_path):
    # Load the input image
    input_image = cv2.imread(image_path)

    if input_image is None:
        print("Error: Unable to load the input image")
        return None

    # Convert the image to RGB
    input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    # Process the image using the MediaPipe Hands model
    results = hands.process(input_image_rgb)

    # If hands are detected, draw the hand landmarks on the image
    if results.multi_hand_landmarks:
        print("Hand landmarks detected in the input image")
        for hand_landmarks in results.multi_hand_landmarks:
            mediapipe_drawing.draw_landmarks(input_image, hand_landmarks, mediapipe_hands.HAND_CONNECTIONS)
            landmarks_x = [landmark.x for landmark in hand_landmarks.landmark]
            landmarks_y = [landmark.y for landmark in hand_landmarks.landmark]
            x_min = min(landmarks_x)
            x_max = max(landmarks_x)
            y_min = min(landmarks_y)
            y_max = max(landmarks_y)

        padding = .1 # 10% padding around the hand

        x_min = max(0, int((x_min - padding) * input_image_rgb.shape[1]))
        x_max = min(input_image_rgb.shape[1], int((x_max + padding) * input_image_rgb.shape[1]))
        y_min = max(0, int((y_min - padding) * input_image_rgb.shape[0]))
        y_max = min(input_image_rgb.shape[0], int((y_max + padding) * input_image_rgb.shape[0]))

        input_image = input_image[y_min:y_max, x_min:x_max] # Crop the image to the bounding box


        # Check if the cropped image size is valid
        if input_image.size == 0:
            print("Error: Cropped image size is invalid")
            return None

        # Resize the image to the required input size for the model
        resized_image = cv2.resize(input_image, (224, 224))

        resized_image = resized_image[:,:,:3]

        # Convert the image to a NumPy array
        image_array = np.array(resized_image)

        # Normalize the image array
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Expand the dimensions of the image array to match the input shape of the model
        input_data = np.expand_dims(normalized_image_array, axis=0)

        return input_data
    
    else:
        print("No hand landmarks detected in the input image")
        return None


app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

# API route for sign language translation using the model
@app.route('/api/v2/detect-sign-language', methods=['POST'])
def translate():
    # Initialize session sentences if not already initialized
    if 'sentence' not in session:
        session['sentence'] = []

    # Get the input image from the request
    input_image = request.files.get('inputImage')

    if input_image:
        # Save the input image to a file
        input_image_path = 'input_image_original.jpg'
        input_image.save(input_image_path)

        # Preprocess the input image
        input_data = preprocess_image(input_image_path)

        if input_data is not None:
            # Call the model to classify the hand gesture
            model_output = sign_language_detector_model.predict(input_data)

            # Assuming model_output is a tuple containing gesture and confidence
            gesture, confidence = labels[np.argmax(model_output)], np.max(model_output)

            # Append the detected gesture to the session sentences
            if gesture == 'space':
                session['sentence'].append(' ')
            elif gesture == 'del':
                session['sentence'].pop()
            else:
                session['sentence'].append(gesture)

            print("The hand gesture has been detected and the letter is: ", gesture, " with a confidence of ", confidence)

            # Return the output as a JSON response
            return jsonify({'status': 'success', 'message': 'The hand gesture has been detected and parsed successfully', 'gesture': gesture, 'confidence': float(confidence), 'sentence': session['sentence']}), 200
        else:
            return jsonify({'status': 'error', 'message': 'No hand landmarks detected in the input image'}), 400
    else:
        return jsonify({'status': 'error', 'message': 'No input image provided in the request'}), 400

