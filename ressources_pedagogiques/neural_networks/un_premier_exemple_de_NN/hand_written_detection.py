from tensorflow.keras.datasets import mnist
from nn import NeuralNetwork, InputLayer, Layer
import numpy as np

# Load and normalize data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0  # Normalize pixel values between 0 and 1
x_test = x_test / 255.0

# Flatten images and one-hot encode labels
x = [np.ravel(img) for img in x_train]
y = []
for label in y_train:
    tmp = np.zeros(10)
    tmp[label] = 1
    y.append(tmp)

x = np.array(x)
y = np.array(y)

# Combine into training pairs
training_data = [(x[i], y[i]) for i in range(len(x))]

# Initialize Neural Network
myNeuralNetwork = NeuralNetwork(np.array([
    InputLayer(784),          # Input layer for 28x28 images flattened
    Layer(784, 16),            # Hidden layer 1
    Layer(16, 16),             # Hidden layer 2
    Layer(16, 10)               # Output layer (10 digits)
]), eta=0.01)

# Training Loop
batch_size = 32
epochs = 10

for epoch in range(epochs):
    print(f"Epoch {epoch+1}/{epochs}")
    
    # Shuffle training data each epoch
    np.random.shuffle(training_data)
    
    # Train on mini-batches
    for batch_start in range(0, len(training_data), batch_size):
        batch = training_data[batch_start:batch_start + batch_size]
        myNeuralNetwork.backPropagation(batch)

    # Check output for first image (just for debugging)
    myNeuralNetwork.output(x[0])

print("Training complete!")
