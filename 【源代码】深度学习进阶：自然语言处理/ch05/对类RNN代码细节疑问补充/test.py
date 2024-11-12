import numpy as np

class RNN:
    def __init__(self, Wx, Wh, b):
        self.params = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache = None

    def forward(self, x, h_prev):
        Wx, Wh, b = self.params
        t = np.dot(h_prev, Wh) + np.dot(x, Wx) + b
        h_next = np.tanh(t)

        self.cache = (x, h_prev, h_next)  # Cache the values for backward pass
        print(f"Forward pass - t: {t}, h_next: {h_next}")
        return h_next

    def backward(self, dh_next):
        Wx, Wh, b = self.params
        x, h_prev, h_next = self.cache

        # Calculate gradients
        dt = dh_next * (1 - h_next ** 2)
        db = np.sum(dt, axis=0)
        dWh = np.dot(h_prev.T, dt)
        dh_prev = np.dot(dt, Wh.T)
        dWx = np.dot(x.T, dt)
        dx = np.dot(dt, Wx.T)

        # Store gradients
        self.grads[0][...] = dWx
        self.grads[1][...] = dWh
        self.grads[2][...] = db

        print(f"Backward pass - dh_next: {dh_next}, dt: {dt}, db: {db}, dWh: {dWh}, dWx: {dWx}, dx: {dx}, dh_prev: {dh_prev}")
        return dx, dh_prev

# Define the parameters
Wx = np.array([[0.5, -0.3], [0.8, 0.1]])
Wh = np.array([[0.7, 0.2], [-0.5, 0.4]])
b = np.array([0.1, -0.2])

# Initialize the RNN
rnn = RNN(Wx, Wh, b)

# Define the inputs and initial hidden state
x_sequence = [
    np.array([[1.0, 0.5]]),  # x1
    np.array([[0.3, -0.3]]),  # x2
    np.array([[-0.7, 0.2]])   # x3
]
h_prev = np.array([[0.0, 0.0]])  # Initial hidden state

# Forward pass through the sequence
h_sequence = []
for i, x in enumerate(x_sequence):
    print(f"\nTime Step {i+1}:")
    h_next = rnn.forward(x, h_prev)
    h_sequence.append(h_next)
    h_prev = h_next  # Update h_prev for the next time step

# Example backward pass
# Assume some gradient from next layer or loss gradient (random for this example)
dh_next = np.array([[1.0, -1.5]])  # Sample gradient coming from the next layer

print('list(enumerate(h_sequence))===',list(enumerate(h_sequence)))
# Backward pass through the sequence (in reverse order)
for i, h in reversed(list(enumerate(h_sequence))):
    print(f"\nBackward Step {i+1}:")
    dx, dh_prev = rnn.backward(dh_next)
    dh_next = dh_prev  # Propagate gradient to the previous time step
