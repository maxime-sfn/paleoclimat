from tensorflow.keras.datasets import mnist
from nn import NeuralNetwork, InputLayer, Layer
import numpy as np
from PIL import Image

class HandWritingDetection:
    
    def __init__(self, previous_data=False, eta=0.1):
        # Load and normalize data
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train = x_train / 255.0   # Normalize pixel values between 0 and 1
        x_test = x_test / 255.0

        # Flatten images and one-hot encode labels
        x = [np.ravel(img) for img in x_train]
        x_test = [np.ravel(img) for img in x_test]

        y = []
        for label in y_train:
            tmp = np.zeros(10)
            tmp[label] = 1
            y.append(tmp)

        x = np.array(x)
        x_test = np.array(x_test)
        y = np.array(y)

        self.x_train = x
        self.y_train = y
        self.x_test = x_test
        self.y_test = y_test

        # Combine into training pairs
        self.training_data = [(x[i], y[i]) for i in range(len(x))]

        # Initialize Neural Network
        self.myNeuralNetwork = NeuralNetwork(np.array([
            InputLayer(784), 
            Layer(784, 100, "hidden_layer1.txt", previous_data), 
            Layer(100, 100, "hidden_layer2.txt", previous_data), 
            Layer(100, 10, "output_layer.txt", previous_data)
        ]), eta)
    
    
    def training(self, batch_size=100, epochs=10):
        for epoch in range(epochs):
            print(f"Epoch {epoch+1}/{epochs}")
            
            # Shuffle training data each epoch
            np.random.shuffle(self.training_data)
            
            # Train on mini-batches
            for batch_start in range(0, len(self.training_data), batch_size):
                batch = self.training_data[batch_start:batch_start + batch_size]
                self.myNeuralNetwork.backPropagation(batch)

            # Check output for first image (just for debugging)
            #myNeuralNetwork.output(x[10])
            #print(f"The number should be : {y_train[10]}")

        print("Training complete!")
        
    def output_test(self, index):
        self.myNeuralNetwork.output(self.x_test[index])
        print(f"The number is : {self.y_test[index]}")
        print("-------------")
        
    def my_output(self, image_name, y):
        image = Image.open(image_name)
        # Force conversion to grayscale (mode 'L')
        grayscale_image = image.convert('L')
        pixel_array = np.array(grayscale_image)
        print(pixel_array.size)
        x = np.ravel(pixel_array) / 255
        self.myNeuralNetwork.output(x)
        print(f"The number is : {y}")
        print("-------------")


predidctor = HandWritingDetection(True, 0.1)

#predidctor.training(2000, 10)

#predidctor.output(100)

predidctor.my_output("2.png",2)