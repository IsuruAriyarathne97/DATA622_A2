import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(url, delimiter=";")

# Define input (X) and output (y)
X = data.iloc[:, :-1].values  # Features (all except last column)
y = data.iloc[:, -1].values   # Target (wine quality score)

# Convert target to classification (quality 3-9 -> categories)

# One-hot encode target variable


# Split into train and test sets

# Standardize features

# Define network architecture
input_size =  # Number of features
hidden_size = 16  # Hidden layer neurons
output_size =  # Number of classes

# Initialize weights and biases
np.random.seed(42)
W1 =
b1 =
W2 =
b2 =

# Activation functions
def relu(Z):
    """ Implement the ReLU activation function.

    """
    pass  # TODO: Implement ReLU function

def softmax(Z):
    """ Implement the softmax activation function.

    """
    pass  # TODO: Implement Softmax function

# Forward propagation
def forward_propagation(X):
    """ Compute the forward pass of the network.
    """
    pass  # TODO: Implement forward propagation

# Compute loss (categorical cross-entropy)
def compute_loss(y_true, y_pred):
    """ Compute the categorical cross-entropy loss.
    """
    pass  # TODO: Implement cross-entropy loss calculation

# Backpropagation
def backward_propagation(X, y, Z1, A1, A2):
    """ Compute the backward pass of the network.
    """
    pass  # TODO: Implement backpropagation

# Training loop
epochs = 1000
for epoch in range(epochs):
    # Perform forward propagation


    # Compute loss


    # Perform backward propagation


    # Print loss every 100 epochs
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Evaluate on test set
_, _, _, A2_test = forward_propagation(X_test)
y_pred = np.argmax(A2_test, axis=1)
y_true = np.argmax(y_test, axis=1)

accuracy = accuracy_score(y_true, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")
