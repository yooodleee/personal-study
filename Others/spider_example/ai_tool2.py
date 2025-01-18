import torch
import torch.nn as nn
import numpy as np
from bindsnet.network import Network
from bindsnet.network.nodes import Input, LIFNodes
from bindsnet.network.topology import Connection
from bindsnet.network.monitors import Monitor
from bindsnet.encoding import PoissonEncoder
from bindsnet.learning import PostPre
from bindsnet.pipeline import EnvironmentPipeline
from bindsnet.datasets import MNIST
from bindsnet.evaluation import all_activity, proportion_weighting

# Parameters
time = 100  # Number of time steps to simulate.
n_neurons = 100  # Number of neurons in the layer.

# Build the SNN.
network = Network(dt=1.0)

# Input layer.
input_layer = Input(n=784, shape=(1, 28, 28))

# LIF layer (Leaky Integrate-and-Fire).
lif_layer = LIFNodes(n=n_neurons)

# Connect the input layer to the LIF layer.
input_connection = Connection(source=input_layer, target=lif_layer, w=0.05 * torch.randn(input_layer.n, lif_layer.n))

# Add layers and connections to the network.
network.add_layer(input_layer, name='Input')
network.add_layer(lif_layer, name='LIF')
network.add_connection(input_connection, source='Input', target='LIF')

# Monitor spikes and voltages.
lif_monitor = Monitor(lif_layer, state_vars=['s', 'v'], time=time)
network.add_monitor(lif_monitor, name='LIF_Monitor')

# Load MNIST dataset.
mnist = MNIST(
    PoissonEncoder(time=time), None, root='.', download=True
)

# Train the network.
for step, batch in enumerate(mnist):
    inputs = {'Input': batch['encoded_image']}
    network.run(inputs=inputs, time=time)

    # Get the spike trains.
    spikes = lif_monitor.get('s')

    # Reset the network at the end of each batch.
    network.reset_state_variables()

    if step == 10:
        break

print("SNN training completed.")
