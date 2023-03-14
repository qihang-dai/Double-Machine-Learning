import numpy as np

# Define the data points and their labels
X = np.array([[2, 3, 'A'], [4, 6, 'B'], [5, 1, 'C'], [10, 12, 'D']])

# Define the number of clusters
k = 2

# Define the initial centers and their labels
initial_centers = np.array([[5, 1, 'C1'], [8, 4, 'C2']])

def k_means(X, k, initial_centers):
    # Extract the features and labels from the data points
    features = X[:, :-1]
    labels = X[:, -1]

    # Extract the coordinates and labels from the initial centers
    initial_coords = initial_centers[:, :-1]
    initial_labels = initial_centers[:, -1]

    # Initialize the centers with the initial coordinates
    centers = initial_coords

    while True:
        # Assign each data point to the closest center
        distances = np.sqrt(((features - centers[:, np.newaxis])**2).sum(axis=2))
        new_labels = initial_labels[distances.argmin(axis=0)]

        # Update the centers
        new_centers = np.array([features[new_labels == label].mean(axis=0) for label in initial_labels])

        # Check if the centers have converged
        if np.allclose(new_centers, centers):
            break

        centers = new_centers

    # Return the final labels and centers
    return new_labels, centers

labels, centers = k_means(X, k, initial_centers)
print("Final labels:", labels)
print("Final centers:", centers)
