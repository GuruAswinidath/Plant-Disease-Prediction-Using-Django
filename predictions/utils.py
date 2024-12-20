import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

CLASS_INDICES = {
    0: "Apple___Apple_scab",
    1: "Apple___Black_rot",
    2: "Apple___Cedar_apple_rust",
    3: "Apple___healthy",
    4: "Cherry_(including_sour)___Powdery_mildew",
    5: "Cherry_(including_sour)___healthy",
    6: "Chili__leaf curl",
    7: "Chili__leaf spot",
    8: "Chili__whitefly",
    9: "Chili__yellowish",
    10: "Chili__healthy",
    11: "Coffee__healthy",
    12: "Coffee__Rust",
    13: "Coffee__red spider mite",
    14: "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    15: "Corn_(maize)___Common_rust_",
    16: "Corn_(maize)___Northern_Leaf_Blight",
    17: "Corn_(maize)___healthy",
    18: "Grape___Black_rot",
    19: "Grape___Esca_(Black_Measles)",
    20: "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    21: "Grape___healthy",
    22: "Peach___Bacterial_spot",
    23: "Peach___healthy",
    24: "Potato___Early_blight",
    25: "Potato___Late_blight",
    26: "Potato___healthy",
    27: "Strawberry___Leaf_scorch",
    28: "Strawberry___healthy",
    29: "Tomato___Bacterial_spot",
    30: "Tomato___Early_blight",
    31: "Tomato___Late_blight",
    32: "Tomato___Leaf_Mold",
    33: "Tomato___Septoria_leaf_spot",
    34: "Tomato___Spider_mites Two-spotted_spider_mite",
    35: "Tomato___Target_Spot",
    36: "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    37: "Tomato___Tomato_mosaic_virus",
    38: "Tomato___healthy",
    39: "Pepper,_bell___Bacterial_spot",
    40: "Pepper,_bell___healthy"
}

# Load the model
MODEL_PATH = "plant_disease_model_inception.h5"
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image_path):
    # Load and preprocess image
    image = load_img(image_path, target_size=(299, 299))  # Resize to model input size
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = tf.keras.applications.inception_v3.preprocess_input(image)  # Preprocessing specific to InceptionV3
    return image

def predict(image_path):
    # Preprocess image
    image = preprocess_image(image_path)
    # Predict
    predictions = model.predict(image)
    class_idx = np.argmax(predictions[0])  # Get class index
    return CLASS_INDICES[class_idx]
