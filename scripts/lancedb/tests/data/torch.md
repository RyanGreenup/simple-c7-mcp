# PyTorch

PyTorch is a Python package providing tensor computation with strong GPU acceleration and deep neural networks built on a tape-based autograd system. It offers a NumPy-like tensor library with seamless GPU support, automatic differentiation for building and training neural networks, and a dynamic computational graph that allows for flexible model architectures. PyTorch is designed to be deeply integrated into Python, making it intuitive to use alongside popular scientific computing libraries like NumPy, SciPy, and scikit-learn.

The framework is organized around several core modules: `torch` for tensor operations, `torch.nn` for neural network layers and modules, `torch.autograd` for automatic differentiation, `torch.optim` for optimization algorithms, and `torch.utils.data` for data loading utilities. PyTorch supports multiple backends including CUDA for NVIDIA GPUs, ROCm for AMD GPUs, and Intel XPU, enabling efficient computation across various hardware platforms. The library emphasizes an imperative programming style with eager execution, making debugging straightforward while also providing tools like TorchScript for production deployment.

## Tensor Creation and Basic Operations

PyTorch tensors are multi-dimensional arrays that can live on CPU or GPU. They support a wide variety of mathematical operations and are the fundamental data structure for all PyTorch computations.

```python
import torch

# Create tensors
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
zeros = torch.zeros(3, 4)
ones = torch.ones(2, 3)
rand = torch.rand(5, 5)  # Uniform distribution [0, 1)
randn = torch.randn(5, 5)  # Normal distribution (mean=0, std=1)

# Create tensor on GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
gpu_tensor = torch.randn(3, 3, device=device)

# Tensor attributes
print(f"Shape: {x.shape}")  # torch.Size([2, 3])
print(f"Dtype: {x.dtype}")  # torch.float32
print(f"Device: {x.device}")  # cpu

# Basic operations
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
print(a + b)  # tensor([5., 7., 9.])
print(a * b)  # tensor([4., 10., 18.])
print(torch.dot(a, b))  # tensor(32.)
print(torch.matmul(torch.randn(2, 3), torch.randn(3, 4)))  # Matrix multiplication

# Indexing and slicing
t = torch.arange(12).reshape(3, 4)
print(t[0])  # First row
print(t[:, 1])  # Second column
print(t[1:, 2:])  # Submatrix

# Move tensor between devices
cpu_tensor = gpu_tensor.cpu()
gpu_tensor = cpu_tensor.to(device)
```

## torch.nn.Module - Building Neural Networks

The `nn.Module` class is the base class for all neural network modules. Custom models should subclass this class and implement the `forward` method.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Create model
model = SimpleNet(input_size=784, hidden_size=128, num_classes=10)

# Forward pass
x = torch.randn(32, 784)  # Batch of 32 samples
output = model(x)
print(f"Output shape: {output.shape}")  # torch.Size([32, 10])

# Access parameters
for name, param in model.named_parameters():
    print(f"{name}: {param.shape}")

# Move model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Set training/evaluation mode
model.train()  # Enable dropout, batch norm in training mode
model.eval()   # Disable dropout, use running stats for batch norm
```

## Convolutional Neural Networks

PyTorch provides comprehensive support for convolutional layers commonly used in image processing tasks.

```python
import torch
import torch.nn as nn

class ConvNet(nn.Module):
    def __init__(self, num_classes=10):
        super(ConvNet, self).__init__()
        # Convolutional layers
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        # Pooling and normalization
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(64)
        self.bn3 = nn.BatchNorm2d(128)

        # Fully connected layers
        self.fc1 = nn.Linear(128 * 4 * 4, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        # Input: (batch, 3, 32, 32)
        x = self.pool(F.relu(self.bn1(self.conv1(x))))  # (batch, 32, 16, 16)
        x = self.pool(F.relu(self.bn2(self.conv2(x))))  # (batch, 64, 8, 8)
        x = self.pool(F.relu(self.bn3(self.conv3(x))))  # (batch, 128, 4, 4)

        x = x.view(x.size(0), -1)  # Flatten: (batch, 128*4*4)
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

# Create and test model
model = ConvNet(num_classes=10)
x = torch.randn(16, 3, 32, 32)  # Batch of 16 RGB images (32x32)
output = model(x)
print(f"Output shape: {output.shape}")  # torch.Size([16, 10])
```

## Recurrent Neural Networks (RNN, LSTM, GRU)

PyTorch supports various recurrent architectures for sequence modeling tasks.

```python
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        # LSTM layer
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2,
            bidirectional=False
        )

        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # x shape: (batch, seq_len, input_size)
        # Initialize hidden state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        # Forward propagate LSTM
        out, (hn, cn) = self.lstm(x, (h0, c0))
        # out shape: (batch, seq_len, hidden_size)

        # Use last time step output
        out = self.fc(out[:, -1, :])
        return out

# Create model
model = LSTMModel(input_size=28, hidden_size=128, num_layers=2, num_classes=10)

# Example: Process sequence data
x = torch.randn(32, 100, 28)  # (batch=32, seq_len=100, features=28)
output = model(x)
print(f"Output shape: {output.shape}")  # torch.Size([32, 10])

# GRU alternative (simpler than LSTM)
gru = nn.GRU(input_size=28, hidden_size=128, num_layers=2, batch_first=True)
out, hn = gru(x)
```

## Transformer Architecture

PyTorch provides native support for Transformer models used in modern NLP and vision tasks.

```python
import torch
import torch.nn as nn

class TransformerModel(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers, dim_feedforward, num_classes):
        super(TransformerModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = nn.Parameter(torch.randn(1, 512, d_model))

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=0.1,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(d_model, num_classes)

    def forward(self, x, mask=None):
        # x shape: (batch, seq_len)
        x = self.embedding(x)  # (batch, seq_len, d_model)
        x = x + self.pos_encoding[:, :x.size(1), :]
        x = self.transformer_encoder(x, src_key_padding_mask=mask)
        x = x.mean(dim=1)  # Global average pooling
        return self.fc(x)

# Create model
model = TransformerModel(
    vocab_size=10000,
    d_model=256,
    nhead=8,
    num_layers=6,
    dim_feedforward=1024,
    num_classes=10
)

# Example usage
tokens = torch.randint(0, 10000, (32, 128))  # (batch=32, seq_len=128)
output = model(tokens)
print(f"Output shape: {output.shape}")  # torch.Size([32, 10])

# MultiheadAttention for custom architectures
mha = nn.MultiheadAttention(embed_dim=256, num_heads=8, batch_first=True)
query = key = value = torch.randn(32, 100, 256)
attn_output, attn_weights = mha(query, key, value)
```

## torch.autograd - Automatic Differentiation

PyTorch's autograd provides automatic differentiation for all operations on tensors. Set `requires_grad=True` to track computations for gradient computation.

```python
import torch

# Create tensors with gradient tracking
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = torch.tensor([4.0, 5.0], requires_grad=True)

# Perform operations
z = x * y + x ** 2
loss = z.sum()

# Compute gradients
loss.backward()

print(f"x.grad: {x.grad}")  # dL/dx = y + 2*x = [8., 11.]
print(f"y.grad: {y.grad}")  # dL/dy = x = [2., 3.]

# Gradient computation with neural network
model = torch.nn.Linear(10, 5)
x = torch.randn(32, 10)
target = torch.randn(32, 5)

output = model(x)
loss = torch.nn.functional.mse_loss(output, target)
loss.backward()

# Access gradients
for name, param in model.named_parameters():
    print(f"{name} grad shape: {param.grad.shape}")

# Disable gradient computation (for inference)
with torch.no_grad():
    output = model(x)  # No gradients computed

# Using inference_mode (more efficient than no_grad)
with torch.inference_mode():
    output = model(x)

# Gradient clipping (prevent exploding gradients)
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=0.5)
```

## torch.optim - Optimization Algorithms

PyTorch provides various optimization algorithms for training neural networks.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Create a simple model
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

# Common optimizers
optimizer_sgd = optim.SGD(model.parameters(), lr=0.01, momentum=0.9, weight_decay=1e-4)
optimizer_adam = optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999), weight_decay=1e-4)
optimizer_adamw = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
optimizer_rmsprop = optim.RMSprop(model.parameters(), lr=0.01, alpha=0.99)

# Training loop example
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(10):
    # Simulate batch data
    inputs = torch.randn(32, 784)
    targets = torch.randint(0, 10, (32,))

    optimizer.zero_grad()  # Clear gradients
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()  # Compute gradients
    optimizer.step()  # Update weights

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Learning rate schedulers
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
scheduler_cosine = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)
scheduler_plateau = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=5)

# Use scheduler in training loop
for epoch in range(100):
    # ... training code ...
    scheduler.step()  # Update learning rate

# Parameter groups with different learning rates
optimizer = optim.Adam([
    {'params': model[0].parameters(), 'lr': 0.001},
    {'params': model[2].parameters(), 'lr': 0.0001}
])
```

## Loss Functions

PyTorch provides various loss functions for different tasks.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# Classification losses
criterion_ce = nn.CrossEntropyLoss()  # For multi-class classification
criterion_bce = nn.BCEWithLogitsLoss()  # For binary/multi-label classification
criterion_nll = nn.NLLLoss()  # For log-softmax outputs

# Regression losses
criterion_mse = nn.MSELoss()  # Mean Squared Error
criterion_l1 = nn.L1Loss()  # Mean Absolute Error
criterion_smooth_l1 = nn.SmoothL1Loss()  # Huber loss

# Example usage
logits = torch.randn(32, 10)
targets = torch.randint(0, 10, (32,))
loss = criterion_ce(logits, targets)

# Binary classification
binary_logits = torch.randn(32, 1)
binary_targets = torch.randint(0, 2, (32, 1)).float()
loss = criterion_bce(binary_logits, binary_targets)

# Regression
predictions = torch.randn(32, 1)
regression_targets = torch.randn(32, 1)
loss = criterion_mse(predictions, regression_targets)

# Functional interface (for more control)
loss = F.cross_entropy(logits, targets, label_smoothing=0.1)
loss = F.mse_loss(predictions, regression_targets, reduction='mean')

# Custom weighted loss
weights = torch.tensor([1.0, 2.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
criterion_weighted = nn.CrossEntropyLoss(weight=weights)
```

## torch.utils.data - Data Loading

PyTorch provides utilities for efficient data loading and batching.

```python
import torch
from torch.utils.data import Dataset, DataLoader, TensorDataset, random_split

# Custom Dataset
class CustomDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        label = self.labels[idx]

        if self.transform:
            sample = self.transform(sample)

        return sample, label

# Create dataset
X = torch.randn(1000, 784)
y = torch.randint(0, 10, (1000,))
dataset = CustomDataset(X, y)

# Simple TensorDataset
dataset = TensorDataset(X, y)

# Split dataset
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# DataLoader with batching and shuffling
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    pin_memory=True,  # Faster transfer to GPU
    drop_last=True
)

val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)

# Iterate through data
for batch_idx, (data, targets) in enumerate(train_loader):
    # Move to GPU
    data = data.cuda()
    targets = targets.cuda()

    # Forward pass
    outputs = model(data)
    loss = criterion(outputs, targets)

    if batch_idx % 100 == 0:
        print(f"Batch {batch_idx}, Loss: {loss.item():.4f}")
```

## Saving and Loading Models

PyTorch provides utilities for serializing and deserializing models.

```python
import torch
import torch.nn as nn

# Create model
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Save entire model (not recommended for production)
torch.save(model, 'model.pth')

# Load entire model
model = torch.load('model.pth', weights_only=False)

# Save only state dict (recommended)
torch.save(model.state_dict(), 'model_state.pth')

# Load state dict
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)
model.load_state_dict(torch.load('model_state.pth', weights_only=True))

# Save checkpoint (for resuming training)
checkpoint = {
    'epoch': 10,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': 0.5,
}
torch.save(checkpoint, 'checkpoint.pth')

# Load checkpoint
checkpoint = torch.load('checkpoint.pth', weights_only=False)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
start_epoch = checkpoint['epoch']
loss = checkpoint['loss']

# Safe loading with weights_only=True (default in PyTorch 2.6+)
model.load_state_dict(torch.load('model_state.pth', weights_only=True))
```

## CUDA and GPU Operations

PyTorch provides seamless GPU acceleration through CUDA.

```python
import torch

# Check CUDA availability
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA device count: {torch.cuda.device_count()}")
print(f"Current device: {torch.cuda.current_device()}")
print(f"Device name: {torch.cuda.get_device_name(0)}")

# Move tensors to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(1000, 1000)
x_gpu = x.to(device)
x_gpu = x.cuda()  # Shorthand

# Move model to GPU
model = torch.nn.Linear(1000, 100)
model = model.to(device)

# Multi-GPU training with DataParallel
if torch.cuda.device_count() > 1:
    model = torch.nn.DataParallel(model)

# Memory management
torch.cuda.empty_cache()  # Free unused memory
print(f"Memory allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
print(f"Memory cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")

# Synchronize CUDA operations (for timing)
torch.cuda.synchronize()

# Mixed precision training
scaler = torch.cuda.amp.GradScaler()
with torch.cuda.amp.autocast():
    output = model(x_gpu)
    loss = output.sum()

scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()

# Set default device
torch.set_default_device('cuda')
x = torch.randn(100, 100)  # Created on GPU by default
```

## torch.compile - Model Compilation

PyTorch 2.0 introduced `torch.compile` for optimizing model execution.

```python
import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

# Basic compilation
compiled_model = torch.compile(model)

# Compilation with options
compiled_model = torch.compile(
    model,
    mode="reduce-overhead",  # Options: "default", "reduce-overhead", "max-autotune"
    fullgraph=True,  # Compile entire model as single graph
    dynamic=False,  # Static shapes for better optimization
)

# Use compiled model (same interface)
x = torch.randn(32, 784)
output = compiled_model(x)

# Compilation modes:
# "default" - Good balance of compile time and speedup
# "reduce-overhead" - Minimize overhead, good for small models
# "max-autotune" - Maximum optimization, longer compile time
```

## torch.export - Model Export

Export PyTorch models for deployment and interoperability.

```python
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 5)

    def forward(self, x):
        return torch.relu(self.linear(x))

model = MyModel()

# Export to TorchScript (for C++ deployment)
scripted_model = torch.jit.script(model)
scripted_model.save("model_scripted.pt")

# Trace-based export
example_input = torch.randn(1, 10)
traced_model = torch.jit.trace(model, example_input)
traced_model.save("model_traced.pt")

# Load TorchScript model
loaded_model = torch.jit.load("model_scripted.pt")
output = loaded_model(example_input)

# Export with torch.export (PyTorch 2.0+)
exported_program = torch.export.export(model, (example_input,))

# Export to ONNX
torch.onnx.export(
    model,
    example_input,
    "model.onnx",
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
)
```

## Complete Training Example

A comprehensive example showing a complete training pipeline.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split

# Define model
class MLP(nn.Module):
    def __init__(self, input_size, hidden_sizes, num_classes, dropout=0.5):
        super(MLP, self).__init__()
        layers = []
        in_size = input_size

        for hidden_size in hidden_sizes:
            layers.extend([
                nn.Linear(in_size, hidden_size),
                nn.BatchNorm1d(hidden_size),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            in_size = hidden_size

        layers.append(nn.Linear(in_size, num_classes))
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)

# Hyperparameters
BATCH_SIZE = 64
LEARNING_RATE = 0.001
NUM_EPOCHS = 20
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create synthetic dataset
X = torch.randn(10000, 784)
y = torch.randint(0, 10, (10000,))
dataset = TensorDataset(X, y)

# Split dataset
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# Initialize model, loss, optimizer
model = MLP(784, [512, 256, 128], 10).to(DEVICE)
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=LEARNING_RATE, weight_decay=0.01)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=NUM_EPOCHS)

# Training loop
best_val_acc = 0.0
for epoch in range(NUM_EPOCHS):
    # Training phase
    model.train()
    train_loss = 0.0
    train_correct = 0
    train_total = 0

    for inputs, targets in train_loader:
        inputs, targets = inputs.to(DEVICE), targets.to(DEVICE)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        train_loss += loss.item()
        _, predicted = outputs.max(1)
        train_total += targets.size(0)
        train_correct += predicted.eq(targets).sum().item()

    # Validation phase
    model.eval()
    val_loss = 0.0
    val_correct = 0
    val_total = 0

    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(DEVICE), targets.to(DEVICE)
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            val_loss += loss.item()
            _, predicted = outputs.max(1)
            val_total += targets.size(0)
            val_correct += predicted.eq(targets).sum().item()

    train_acc = 100. * train_correct / train_total
    val_acc = 100. * val_correct / val_total

    print(f"Epoch {epoch+1}/{NUM_EPOCHS}")
    print(f"  Train Loss: {train_loss/len(train_loader):.4f}, Acc: {train_acc:.2f}%")
    print(f"  Val Loss: {val_loss/len(val_loader):.4f}, Acc: {val_acc:.2f}%")

    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_model.pth')

    scheduler.step()

print(f"Best Validation Accuracy: {best_val_acc:.2f}%")
```

## Summary

PyTorch is the leading deep learning framework for research and production, offering an intuitive Pythonic interface with powerful GPU acceleration. Its core strengths include dynamic computational graphs that enable flexible model architectures, comprehensive neural network modules through `torch.nn`, automatic differentiation via `torch.autograd`, and efficient data loading utilities. The framework supports modern architectures including CNNs, RNNs, LSTMs, GRUs, and Transformers, making it suitable for computer vision, natural language processing, and other machine learning domains.

The ecosystem provides seamless integration patterns for various deployment scenarios: `torch.jit` for TorchScript-based C++ deployment, `torch.onnx` for cross-framework interoperability, and `torch.compile` for optimized execution. PyTorch's modular design allows researchers to experiment rapidly while providing production-ready tools for model training, evaluation, checkpointing, and deployment. The library's consistent API across CPU and GPU backends, combined with built-in support for distributed training and mixed-precision computation, makes it a versatile choice for projects ranging from academic research to enterprise-scale machine learning systems.
