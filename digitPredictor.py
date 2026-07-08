import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
import matplotlib.pyplot as plt

# Load the MNIST handwritten digits dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Scale pixel values between 0 and 1
train_images = train_images.astype("float32") / 255.0
test_images = test_images.astype("float32") / 255.0

# Create the neural network
digit_model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(64, activation="relu"),
    Dense(32, activation="relu"),
    Dense(10, activation="softmax")
])

# Configure the model
digit_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train the model
digit_model.fit(train_images, train_labels, epochs=5, verbose=1)

# Test the model
loss, accuracy = digit_model.evaluate(test_images, test_labels)

print(f"\nModel Accuracy: {accuracy:.4f}")

# Predict the first test image
result = digit_model.predict(test_images)

predicted_digit = result[0].argmax()
actual_digit = test_labels[0]

# Display the image
plt.imshow(test_images[0], cmap="gray")
plt.title(f"Prediction: {predicted_digit} | Actual: {actual_digit}")
plt.axis("off")
plt.show()