### Install ONNX Runtime NuGet Packages with .NET CLI

Source: https://onnxruntime.ai/docs/get-started/with-csharp

Installs the necessary Microsoft.ML.OnnxRuntime and System.Numerics.Tensors NuGet packages using the .NET CLI. Ensure you have the .NET SDK installed.

```bash
dotnet add package Microsoft.ML.OnnxRuntime --version 1.16.0
dotnet add package System.Numerics.Tensors --version 0.1.0
```

--------------------------------

### Install ONNX Runtime Web using npm

Source: https://onnxruntime.ai/docs/get-started/with-javascript/web

Installs the latest release version or a nightly build of ONNX Runtime Web using npm. This is the initial step for integrating the library into a project.

```shell
# install latest release version
npm install onnxruntime-web

# install nightly build dev version
npm install onnxruntime-web@dev

```

--------------------------------

### Install ONNX Runtime Node.js Binding using npm

Source: https://onnxruntime.ai/docs/get-started/with-javascript/node

Installs the latest release version of the ONNX Runtime Node.js binding using npm. This is the first step to using ONNX Runtime in your Node.js projects.

```bash
# install latest release version
npm install onnxruntime-node
```

--------------------------------

### Install ONNX Runtime CPU

Source: https://onnxruntime.ai/docs/get-started/with-python

Installs the ONNX Runtime CPU package using pip. This is recommended for Arm-based CPUs and macOS. No external dependencies are required beyond pip.

```shell
pip install onnxruntime
```

--------------------------------

### Import ONNX Runtime Web with WebGPU Support

Source: https://onnxruntime.ai/docs/get-started/with-javascript/web

Imports ONNX Runtime Web with experimental WebGPU support. This allows for leveraging GPU acceleration for inference tasks. It includes both ES6 and CommonJS import examples.

```javascript
// use ES6 style import syntax (recommended)
import * as ort from 'onnxruntime-web/webgpu';

```

```javascript
// or use CommonJS style import syntax
const ort = require('onnxruntime-web/webgpu');

```

--------------------------------

### Install ONNX Runtime Training Packages

Source: https://onnxruntime.ai/docs/get-started/training-pytorch

Installs the necessary Python packages for ONNX Runtime Training and configures them to work with your PyTorch installation. This is a prerequisite for using ORTModule.

```bash
pip install torch-ort
python -m torch_ort.configure
```

--------------------------------

### Import ONNX Runtime Web with WebNN Support

Source: https://onnxruntime.ai/docs/get-started/with-javascript/web

Imports ONNX Runtime Web with experimental WebNN support. This enables the use of the WebNN API for hardware-accelerated inference. It provides examples for both ES6 and CommonJS module systems.

```javascript
// use ES6 style import syntax (recommended)
import * as ort from 'onnxruntime-web/experimental';

```

```javascript
// or use CommonJS style import syntax
const ort = require('onnxruntime-web/experimental');

```

--------------------------------

### Install ONNX Runtime OpenVINO EP for Python

Source: https://onnxruntime.ai/docs/execution-providers/OpenVINO-ExecutionProvider

Installs the ONNX Runtime OpenVINO Execution Provider Python package from PyPI. This is the primary method for Python users to get started.

```bash
pip install onnxruntime-openvino
```

--------------------------------

### Install ONNX Runtime for React Native using npm

Source: https://onnxruntime.ai/docs/get-started/with-javascript/react-native

Installs the latest release version of the ONNX Runtime library for React Native using npm. This is the initial step to integrate ONNX Runtime into your project.

```bash
# install latest release version
npm install onnxruntime-react-native

```

--------------------------------

### Install ONNX Runtime GPU with pip

Source: https://onnxruntime.ai/docs/get-started/with-python

These commands demonstrate how to install ONNX Runtime with GPU support for specific CUDA versions using pip. It requires Python and pip. The command installs the necessary packages for ONNX Runtime to leverage GPU acceleration.

```bash
python -m pip install onnxruntime-gpu --extra-index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-11-nightly/pypi/simple/
```

```bash
python -m pip install onnxruntime-gpu --pre --extra-index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/
```

--------------------------------

### C API: Create ONNX Runtime Session and Run Inference

Source: https://onnxruntime.ai/docs/get-started/with-c

This snippet demonstrates the core C API calls for initializing an ONNX Runtime environment, creating a session with a model, preparing input tensors, and executing the model. It highlights the use of execution providers for hardware acceleration. Ensure you have the onnxruntime_c_api.h header included.

```c
#include "onnxruntime_c_api.h"

// ... (error handling and environment setup)

// 1. Create Environment
OrtEnv* env = OrtCreateEnv(ORT_LOGGING_LEVEL_WARNING, "ONNXRuntime");

// 2. Create Session Options (optional: add execution providers)
OrtSessionOptions* session_options;
OrtCreateSessionOptions(&session_options);
// Example: OrtSessionOptionsAppendExecutionProvider_CUDA(session_options, 0);

// 3. Create Session
const char* model_uri = "path/to/your/model.onnx";
OrtSession* session;
OrtCreateSession(env, model_uri, session_options, &session);

// 4. Create Input Tensor (example for a float tensor)
OrtMemoryInfo* memory_info;
OrtCreateMemoryInfo("Cpu" /* or "Cuda" */, ORT_MEMORY_STYLE_DEFAULT, &memory_info);

const char* input_name = "input_tensor_name"; // Replace with actual input name
float input_data[] = {1.0f, 2.0f, 3.0f, 4.0f}; // Example data
size_t data_count = sizeof(input_data) / sizeof(float);
int64_t shape[] = {1, data_count}; // Example shape

OrtValue* input_tensor;
OrtCreateTensorWithDataAsOrtValue(memory_info, input_data, data_count * sizeof(float), shape, 2 /* rank */, ORT_TYPE_FLOAT, &input_tensor);

// 5. Prepare Inputs and Outputs lists
OrtValue* input_list[] = {input_tensor};
const char* output_names[] = {"output_tensor_name"}; // Replace with actual output name

// 6. Run Inference
OrtValue* output_list[];
OrtRun(session, input_list, 1, output_names, 1, &output_list);

// ... (process output_list, release resources)

OrtReleaseMemoryInfo(memory_info);
OrtReleaseValue(input_tensor);
OrtReleaseSession(session);
OrtReleaseSessionOptions(session_options);
OrtReleaseEnv(env);

```

--------------------------------

### Create ONNX Runtime Session in Java

Source: https://onnxruntime.ai/docs/get-started/with-java

Initializes the ONNX Runtime environment and creates a session to load an ONNX model. This is the first step to running inference. Requires the ONNX Runtime Java library.

```java
var env = OrtEnvironment.getEnvironment();
var session = env.createSession("model.onnx",new OrtSession.SessionOptions());
```

--------------------------------

### Load and Check ONNX Model

Source: https://onnxruntime.ai/docs/get-started/with-python

Loads an ONNX model from a file and checks its validity using the ONNX library. Requires the `onnx` package to be installed.

```python
import onnx
onnx_model = onnx.load("fashion_mnist_model.onnx")
onnx.checker.check_model(onnx_model)
```

--------------------------------

### CoreML Execution Provider Setup (C++ API)

Source: https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider

Example demonstrating how to set up and use the CoreML Execution Provider with C++ API, including specifying provider options like ModelFormat.

```APIDOC
## CoreML Execution Provider Setup (C++ API)

### Description
This section shows how to register and configure the CoreML Execution Provider using the C++ API. It demonstrates specifying provider options such as `ModelFormat`.

### Method
AppendExecutionProvider

### Endpoint
N/A (API call)

### Parameters
#### Provider Options (Map)
- **ModelFormat** (string) - Required - Specifies the model format. Example: "MLProgram"

### Request Example
```cpp
Ort::Env env = Ort::Env{ORT_LOGGING_LEVEL_ERROR, "Default"};
Ort::SessionOptions so;
std::unordered_map<std::string, std::string> provider_options;
provider_options["ModelFormat"] = "MLProgram";
so.AppendExecutionProvider("CoreML", provider_options);
Ort::Session session(env, model_path, so);
```

### Response
#### Success Response (N/A)
N/A

#### Response Example
N/A
```

--------------------------------

### Install ONNX Export Dependencies

Source: https://onnxruntime.ai/docs/get-started/with-python

Installs Python packages required for exporting models to ONNX format from different frameworks. PyTorch, TensorFlow (via tf2onnx), and SciKit Learn (via skl2onnx) are supported.

```shell
pip install torch
```

```shell
pip install tf2onnx
```

```shell
pip install skl2onnx
```

--------------------------------

### Install ONNX Runtime GPU (CUDA 12.x)

Source: https://onnxruntime.ai/docs/get-started/with-python

Installs the ONNX Runtime GPU package with support for CUDA 12.x using pip. This package includes most CPU functionalities. Ensure CUDA 12.x is installed on your system.

```shell
pip install onnxruntime-gpu
```

--------------------------------

### Install ONNX Runtime GPU (CUDA 11.8)

Source: https://onnxruntime.ai/docs/get-started/with-python

Installs the ONNX Runtime GPU package specifically for CUDA 11.8 from a custom Azure DevOps feed. This requires pip and internet access to the specified URL.

```shell
pip install onnxruntime-gpu --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-11/pypi/simple/
```

--------------------------------

### CoreML Execution Provider Setup (Deprecated C++ API)

Source: https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider

Example demonstrating the usage of the deprecated CoreML Execution Provider setup using C++ API.

```APIDOC
## CoreML Execution Provider Setup (Deprecated C++ API)

### Description
This section provides an example of using the deprecated C++ API function `OrtSessionOptionsAppendExecutionProvider_CoreML` for setting up the CoreML Execution Provider. It is recommended to use the newer `OrtSessionOptionsAppendExecutionProvider` instead.

### Method
OrtSessionOptionsAppendExecutionProvider_CoreML

### Endpoint
N/A (API call)

### Parameters
#### Path Parameters
N/A

#### Query Parameters
N/A

#### Request Body
N/A

### Request Example
```cpp
Ort::Env env = Ort::Env{ORT_LOGGING_LEVEL_ERROR, "Default"};
Ort::SessionOptions so;
uint32_t coreml_flags = 0;
Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_CoreML(so, coreml_flags));
Ort::Session session(env, model_path, so);
```

### Response
#### Success Response (N/A)
N/A

#### Response Example
N/A
```

--------------------------------

### Import ONNX Runtime Web with ES6 and CommonJS

Source: https://onnxruntime.ai/docs/get-started/with-javascript/web

Demonstrates how to import the ONNX Runtime Web library using both ES6 style import syntax and CommonJS require syntax. This is the standard way to include the library in JavaScript projects.

```javascript
// use ES6 style import syntax (recommended)
import * as ort from 'onnxruntime-web';

```

```javascript
// or use CommonJS style import syntax
const ort = require('onnxruntime-web');

```

--------------------------------

### Clone ONNX Runtime GenAI C++ Examples

Source: https://onnxruntime.ai/docs/genai/tutorials/snapdragon

Clones the ONNX Runtime GenAI C++ example repository from GitHub and navigates into the C++ examples directory. This is the first step to building and running the C++ application. Requires 'git'.

```bash
git clone https://github.com/microsoft/onnxruntime-genai
cd examples\c

```

--------------------------------

### Create InferenceSession from Model File

Source: https://onnxruntime.ai/docs/get-started/with-c

This snippet demonstrates how to create an InferenceSession object from a model file stored on disk, along with a set of SessionOptions. This is a fundamental step for running ONNX models.

```c++
OrtStatus* status = ort_api->CreateSession(env, model_path, &session_options, &session);

```

--------------------------------

### Install ONNX from Source

Source: https://onnxruntime.ai/docs/build/inferencing

Commands to install ONNX from source code, including setting an environment variable for ONNX_ML, building a wheel package, and installing it using pip. It also recommends uninstalling protobuf before building ONNX Runtime.

```shell
export ONNX_ML=1
python3 setup.py bdist_wheel
pip3 install --upgrade dist/*.whl

```

--------------------------------

### Configure ONNX Runtime Session with VitisAI Execution Provider (C++)

Source: https://onnxruntime.ai/docs/execution-providers/Vitis-AI-ExecutionProvider

This C++ example demonstrates how to initialize an ONNX Runtime environment, configure session options with the VitisAI execution provider, and create an inference session. It includes setting provider-specific options like cache directory, cache key, and log level. The example also shows how to retrieve input and output names and shapes, and prepare for running inference.

```cpp
// ...
#include <onnxruntime_cxx_api.h>
// include user header files
// ...

std::basic_string<ORTCHAR_T> model_file = "resnet50.onnx" // Replace resnet50.onnx with your model name
Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "resnet50_pt");
auto session_options = Ort::SessionOptions();

auto options = std::unorderd_map<std::string,std::string>({});
// optional, eg: cache path : /tmp/my_cache/abcdefg // Replace abcdefg with your model name, eg. onnx_model_md5
options["cache_dir"] = "/tmp/my_cache";
options["cache_key"] = "abcdefg"; // Replace abcdefg with your model name, eg. onnx_model_md5
options["log_level"] = "info";

// Create an inference session using the Vitis AI execution provider
session_options.AppendExecutionProvider_VitisAI(options);

auto session = Ort::Session(env, model_file.c_str(), session_options);

// get inputs and outputs
Ort::AllocatorWithDefaultOptions allocator;
std::vector<std::string> input_names;
std::vector<std::int64_t> input_shapes;
auto input_count = session.GetInputCount();
for (std::size_t i = 0; i < input_count; i++) {
    input_names.emplace_back(session.GetInputNameAllocated(i, allocator).get());
    input_shapes = session.GetInputTypeInfo(i).GetTensorTypeAndShapeInfo().GetShape();
}
std::vector<std::string> output_names;
auto output_count = session.GetOutputCount();
for (std::size_t i = 0; i < output_count; i++) {
   output_names.emplace_back(session.GetOutputNameAllocated(i, allocator).get());
}
// Create input tensors and populate input data
std::vector<Ort::Value> input_tensors;
...

auto output_tensors = session.Run(Ort::RunOptions(), input_names.data(), input_tensors.data(),
                    input_count, output_names.data(), output_count);
// postprocess output data
// ...

```

--------------------------------

### ONNX Runtime DLL Deployment on Windows

Source: https://onnxruntime.ai/docs/get-started/with-c

This section details how to deploy the ONNX Runtime DLL (`onnxruntime.dll`) on Windows 10. It explains the importance of placing the DLL in the same folder as the application or consuming DLL and recommends using run-time dynamic linking to avoid conflicts with system-wide DLLs.

```C++
#include <windows.h>
#include <string>
#include <iostream>

// Function to get the directory of the current module (DLL)
std::wstring GetModulePath()
{
    wchar_t path[MAX_PATH];
    if (GetModuleFileNameW(NULL, path, MAX_PATH) != 0)
    {
        std::wstring wstrPath(path);
        return wstrPath.substr(0, wstrPath.find_last_of(L"\/"));
    }
    return L"";
}

int main()
{
    std::wstring modulePath = GetModulePath();
    std::wstring onnxRuntimeDllPath = modulePath + L"\\onnxruntime.dll";

    // Use LoadLibraryEx with LOAD_WITH_ALTERED_SEARCH_PATH or explicitly specify the path
    // HMODULE hModule = LoadLibraryExW(onnxRuntimeDllPath.c_str(), NULL, LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR | LOAD_LIBRARY_SEARCH_DEFAULT_DIRS);
    // OR
    // HMODULE hModule = LoadLibraryW(onnxRuntimeDllPath.c_str());

    // ... rest of your application using ONNX Runtime ...

    // FreeLibrary(hModule);
    return 0;
}
```

--------------------------------

### OrtEpFactory Implementation Example (C++)

Source: https://onnxruntime.ai/docs/execution-providers/plugin-ep-libraries

Illustrates example implementations for required and optional functions of an `OrtEpFactory`. These functions are crucial for an EP to interact with ONNX Runtime, providing details about the EP, device support, and methods for creating resources like allocators and sessions.

```cpp
#include <onnxruntime/core/session/onnx_inference_session.h>
#include <onnxruntime/core/session/ort_api.h>

// Example implementation for required functions
inline const char* ExampleEpFactory::GetNameImpl() {
    return "ExampleEP";
}

inline const char* ExampleEpFactory::GetVendor() {
    return "ExampleVendor";
}

inline const char* ExampleEpFactory::GetVersion() {
    return "1.0.0"; // Semantic Versioning 2.0
}

inline std::vector<OrtHardwareDevice> ExampleEpFactory::GetSupportedDevicesImpl() {
    // Return information about supported hardware devices
    return {};
}

inline OrtEp* ExampleEpFactory::CreateEpImpl(OrtEnv* env, const OrtSessionOptions* options) {
    // Create and return an OrtEp instance
    return nullptr;
}

// Example implementation for optional functions
inline void ExampleEpFactory::ValidateCompiledModelCompatibilityInfo(const char* info) {
    // Validate model compatibility
}

inline OrtAllocator* ExampleEpFactory::CreateAllocatorImpl(OrtMemoryInfo* mem_info) {
    // Create and return an OrtAllocator instance
    return nullptr;
}

inline void ExampleEpFactory::ReleaseAllocatorImpl(OrtAllocator* allocator) {
    // Release the OrtAllocator instance
}

inline OrtDataTransferImpl* ExampleEpFactory::CreateDataTransferImpl() {
    // Create and return an OrtDataTransferImpl instance
    return nullptr;
}

inline bool ExampleEpFactory::IsStreamAwareImpl() {
    return false; // Or true if the EP is stream-aware
}

inline void* ExampleEpFactory::CreateSyncStreamForDeviceImpl(OrtMemoryDevice* device) {
    // Create and return a synchronization stream for the device
    return nullptr;
}

```

--------------------------------

### Install ONNX Runtime GPU with CUDA and cuDNN (Shell)

Source: https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider

This command installs the `onnxruntime-gpu` package along with the necessary CUDA and cuDNN runtime DLLs using pip. This simplifies the setup process for GPU acceleration.

```bash
pip install onnxruntime-gpu[cuda,cudnn]

```

--------------------------------

### Verify Converted ONNX Model with ONNX Runtime

Source: https://onnxruntime.ai/docs/tutorials/tf-get-started

Verifies a converted ONNX model by comparing its output with the original TensorFlow model's output using ONNX Runtime and NumPy. Requires onnxruntime and numpy to be installed. This snippet demonstrates loading the ONNX model, running inference, and asserting the results against the TensorFlow model's execution.

```python
import onnxruntime as ort
import numpy as np

# Change shapes and types to match model
input1 = np.zeros((1, 100, 100, 3), np.float32)

# Start from ORT 1.10, ORT requires explicitly setting the providers parameter if you want to use execution providers
# other than the default CPU provider (as opposed to the previous behavior of providers getting set/registered by default
# based on the build flags) when instantiating InferenceSession.
# Following code assumes NVIDIA GPU is available, you can specify other execution providers or don't include providers parameter
# to use default CPU provider.
sess = ort.InferenceSession("dst/path/model.onnx", providers=["CUDAExecutionProvider"])

# Set first argument of sess.run to None to use all model outputs in default order
# Input/output names are printed by the CLI and can be set with --rename-inputs and --rename-outputs
# If using the python API, names are determined from function arg names or TensorSpec names.
results_ort = sess.run(["output1", "output2"], {"input1": input1})

import tensorflow as tf
model = tf.saved_model.load("path/to/savedmodel")
results_tf = model(input1)

for ort_res, tf_res in zip(results_ort, results_tf):
    np.testing.assert_allclose(ort_res, tf_res, rtol=1e-5, atol=1e-5)

print("Results match")

```

--------------------------------

### Export PyTorch NLP Model to ONNX

Source: https://onnxruntime.ai/docs/get-started/with-python

Exports a PyTorch Natural Language Processing model to ONNX format. This example shows how to prepare text input and offsets, then uses `torch.onnx.export` with dynamic axes for variable batch sizes.

```python
# Export the model
torch.onnx.export(model,                     # model being run
                (text, offsets),           # model input (or a tuple for multiple inputs)
                "ag_news_model.onnx",      # where to save the model (can be a file or file-like object)
                export_params=True,        # store the trained parameter weights inside the model file
                opset_version=10,          # the ONNX version to export the model to
                do_constant_folding=True,  # whether to execute constant folding for optimization
                input_names = ['input', 'offsets'],   # the model's input names
                output_names = ['output'], # the model's output names
                dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                              'output' : {0 : 'batch_size'}})
```

--------------------------------

### Install ONNX Runtime QNN Nightly (Python)

Source: https://onnxruntime.ai/docs/install

Installs the nightly build of the QNN version of ONNX Runtime. Includes prerequisite package installations for testing.

```python
pip install flatbuffers numpy packaging protobuf sympy
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ onnxruntime-qnn

```

--------------------------------

### Import ONNX Runtime Node.js Binding (ES6)

Source: https://onnxruntime.ai/docs/get-started/with-javascript/node

Demonstrates how to import the ONNX Runtime Node.js binding using the recommended ES6 style import syntax. This allows access to the ONNX Runtime functionalities within your JavaScript modules.

```javascript
// use ES6 style import syntax (recommended)
import * as ort from 'onnxruntime-node';
```

--------------------------------

### Configure ONNX Runtime Session with VitisAI Execution Provider (Python)

Source: https://onnxruntime.ai/docs/execution-providers/Vitis-AI-ExecutionProvider

This Python example shows how to create an ONNX Runtime inference session using the VitisAIExecutionProvider. It specifies the model file and the provider with optional configuration settings. The example also demonstrates how to retrieve input details and run the model inference.

```python
import onnxruntime

# Add user imports
# ...

# Load inputs and do preprocessing
# ...

# Create an inference session using the Vitis AI execution provider
session = onnxruntime.InferenceSession(
    '[model_file].onnx',
    providers=["VitisAIExecutionProvider"],
    provider_options=[{"log_level": "info"}])

input_shape = session.get_inputs()[0].shape
input_name = session.get_inputs()[0].name

# Load inputs and do preprocessing by input_shape
input_data = [...] # Replace with actual input data
result = session.run([], {input_name: input_data})

```

--------------------------------

### Install ONNX Runtime Training for C# on Windows

Source: https://onnxruntime.ai/docs/install

Installs the ONNX Runtime Training package for C# on Windows using the .NET CLI. This is a prerequisite for on-device training with C#.

```bash
dotnet add package Microsoft.ML.OnnxRuntime.Training
```

--------------------------------

### Initialize ONNX Runtime Training C API

Source: https://onnxruntime.ai/docs/api/c/training_c_cpp_api

This snippet demonstrates the initialization process for the ONNX Runtime Training C API. It involves getting the base API, then the training-specific API, creating an environment, session options, and loading a checkpoint. Dependencies include the onnxruntime_training_api.h and onnxruntime_c_api.h headers.

```c
#include <onnxruntime_training_api.h>

OrtApi* g_ort_api = OrtGetApiBase()->GetApi(ORT_API_VERSION);
OrtTrainingApi* g_ort_training_api = g_ort_api->GetTrainingApi(ORT_API_VERSION);

OrtEnv* env = NULL;
g_ort_api->CreateEnv(logging_level, logid, &env);

OrtSessionOptions* session_options = NULL;
g_ort_api->CreateSessionOptions(&session_options);

OrtCheckpointState* state = NULL;
g_ort_training_api->LoadCheckpoint(path_to_checkpoint, &state);
```

--------------------------------

### Install Other Dependencies

Source: https://onnxruntime.ai/docs/genai/tutorials/finetune

Installs additional Python libraries required for model fine-tuning and handling, specifically 'optimum' and 'peft'.

```shell
pip install optimum peft
```

--------------------------------

### Installation and Import

Source: https://onnxruntime.ai/docs/genai/api/python

Instructions on how to install the onnxruntime-genai package and import it into your Python environment.

```APIDOC
## Install and import

The Python API is delivered by the onnxruntime-genai Python package.

```python
pip install onnxruntime-genai
```

```python
import onnxruntime_genai
```
```

--------------------------------

### Run Model with Inputs

Source: https://onnxruntime.ai/docs/get-started/with-c

This snippet shows how to execute an ONNX model with specified inputs. Inputs must be in CPU memory. The function can also handle models with multiple outputs, allowing users to select specific ones.

```c++
OrtStatus* status = ort_api->Run(session, run_options, input_names.data(), input_values.data(), input_count, output_names.data(), output_count, output_values.data());

```

--------------------------------

### Install Olive Package

Source: https://onnxruntime.ai/docs/genai/tutorials/finetune

Installs the Olive library from its GitHub repository. This is a prerequisite for using Olive's model fine-tuning and optimization capabilities.

```shell
pip install git+https://github.com/microsoft/olive
```

--------------------------------

### Install ONNX Runtime for OpenVINO

Source: https://onnxruntime.ai/docs/install

Installs the ONNX Runtime package optimized for Intel's OpenVINO toolkit. This provides enhanced performance on Intel hardware.

```bash
pip install intel/onnxruntime
```

--------------------------------

### Install ONNX Runtime DirectML for C# and C++

Source: https://onnxruntime.ai/docs/install

Installs the ONNX Runtime DirectML package for C# and C++ on Windows. This enables hardware acceleration using DirectML on compatible GPUs.

```bash
dotnet add package Microsoft.ML.OnnxRuntime.DirectML
```

--------------------------------

### Initialize and Train with ONNX Runtime C++ API

Source: https://onnxruntime.ai/docs/api/c/training_c_cpp_api

Demonstrates initializing the ONNX Runtime environment, session options, loading a checkpoint, creating a training session, and performing training steps. It also shows how to save checkpoints and export the model for inference. Ensure the Ort::CheckpointState instance outlives the Ort::TrainingSession instance.

```cpp
#include <onnxruntime_training_cxx_api.h>

// Initialize environment and session options
Ort::Env env;
Ort::SessionOptions session_options;

// Load checkpoint state
const std::string path_to_checkpoint = "your_checkpoint_path";
auto state = Ort::CheckpointState::LoadCheckpoint(path_to_checkpoint);

// Define model paths
const std::string training_model_path = "your_training_model.onnx";
const std::string eval_model_path = "your_eval_model.onnx";
const std::string optimizer_model_path = "your_optimizer_model.onnx";

// Create a training session
auto training_session = Ort::TrainingSession(env, session_options, state, training_model_path,
eval_model_path, optimizer_model_path);

// Training Loop
{
    // Perform a training step
    training_session.TrainStep(...);
    // Update optimizer
    training_session.OptimizerStep(...);
    // Reset gradients
    training_session.LazyResetGrad(...);
}

// Export model for inference
const std::string inference_model_path = "your_inference_model.onnx";
training_session->ExportModelForInferencing(inference_model_path, ...);

// Save the checkpoint state
Ort::CheckpointState::SaveCheckpoint(state, path_to_checkpoint, false);

```

--------------------------------

### Example Script Execution

Source: https://onnxruntime.ai/docs/tutorials/azureml

This Python code block demonstrates the execution flow of the defined functions. It first calls an initialization function 'init()', then prepares sample input data, runs the PyTorch model, and finally runs the ONNX Runtime model, printing its results. This serves as a basic test case.

```python
# Assuming 'init', 'run_pytorch', and 'run' are defined previously

if __name__ == '__main__':
    init()

    input = "{\"question\": \"What is Dolly Parton's middle name?\", \"context\": \"Dolly Rebecca Parton is an American singer-songwriter\"}"

    run_pytorch(input)
    print(run(input))
```

--------------------------------

### DirectML Execution Provider Installation and Requirements

Source: https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider

Information on how to install and the requirements for using the DirectML Execution Provider with ONNX Runtime.

```APIDOC
## DirectML Execution Provider

**Note:** DirectML is in sustained engineering. New feature development has moved to WinML for Windows-based ONNX Runtime deployments.

The DirectML Execution Provider uses DirectML to accelerate inference of ONNX models, improving evaluation time on commodity GPU hardware.

### Install

Pre-built packages of ORT with the DirectML EP are published on Nuget.org. Refer to: [Install ONNX Runtime](link-to-install-onnx-runtime).

### Requirements

The DirectML execution provider requires a DirectX 12 capable device. Compatible hardware includes:

*   NVIDIA Kepler (GTX 600 series) and above
*   AMD GCN 1st Gen (Radeon HD 7000 series) and above
*   Intel Haswell (4th-gen core) HD Integrated Graphics and above
*   Qualcomm Adreno 600 and above

DirectML was introduced in Windows 10, version 1903.

### Build

Requirements for building the DirectML execution provider:

1.  Visual Studio 2017 toolchain
2.  The Windows 10 SDK (10.0.17134.0) for Windows 10, version 1803 (or newer)

To build onnxruntime with the DML EP included, use the `--use_dml` flag with `build.bat`:

```bash
build.bat --config RelWithDebInfo --build_shared_lib --parallel --use_dml
```

The DirectML execution provider supports building for x64 (default) and x86 architectures. Building ONNX Runtime with DirectML allows for automatic download of the DirectML re-distributable package.
```

--------------------------------

### Verify CMake Installation

Source: https://onnxruntime.ai/docs/build/inferencing

Verifies the installed version of CMake. This command should be run after installing CMake to ensure it is properly set up.

```bash
cmake --version
```

--------------------------------

### Install ONNX Runtime (Nightly Build)

Source: https://onnxruntime.ai/docs/reference/ort-format-models

Installs the nightly build of the ONNX Runtime Python package from a test PyPI repository. This is recommended when using the main branch of the ONNX Runtime git repository.

```bash
pip install -U -i https://test.pypi.org/simple/ ort-nightly

```

--------------------------------

### Initialize OpenVINO Environment

Source: https://onnxruntime.ai/docs/build/eps

Initializes the OpenVINO™ environment by running the setupvars script. This is a required step before building or running with the OpenVINO™ Execution Provider. It sets up necessary environment variables for OpenVINO™ tools and libraries.

```batch
C:\<openvino_install_directory>\setupvars.bat
```

```shell
source <openvino_install_directory>/setupvars.sh
```

--------------------------------

### Install CocoaPods Dependencies

Source: https://onnxruntime.ai/docs/tutorials/on-device-training/ios-app

This command installs all the dependencies listed in your Podfile, including the 'onnxruntime-training-objc' pod. After running this, a '.xcworkspace' file will be generated, which should be used to open the project in Xcode.

```bash
pod install

```

--------------------------------

### Display Pre-processing Help (Command Line)

Source: https://onnxruntime.ai/docs/performance/quantization

Displays help information for the ONNX Runtime pre-processing tool, outlining available options and controls for preparing models for quantization. This command is useful for understanding the full range of pre-processing capabilities.

```bash
python -m onnxruntime.quantization.preprocess --help
```

--------------------------------

### Configure ONNX Runtime for GPU in Java

Source: https://onnxruntime.ai/docs/get-started/with-java

Enables the CUDA execution provider for ONNX Runtime when creating an OrtSession. This allows inference to be run on a GPU, provided CUDA is installed and supported. Requires specifying the GPU device ID.

```java
int gpuDeviceId = 0; // The GPU device ID to execute on
var sessionOptions = new OrtSession.SessionOptions();
sessionOptions.addCUDA(gpuDeviceId);
var session = environment.createSession("model.onnx", sessionOptions);
```

--------------------------------

### Convert TensorFlow SavedModel to ONNX using CLI

Source: https://onnxruntime.ai/docs/tutorials/tf-get-started

Converts a TensorFlow SavedModel to ONNX format using the tf2onnx command-line interface. Requires tf2onnx to be installed. The command specifies the input SavedModel directory, output ONNX file path, and the ONNX opset version.

```bash
python -m tf2onnx.convert --saved-model path/to/savedmodel --output dst/path/model.onnx --opset 13

```

--------------------------------

### Install ONNX Runtime DirectML

Source: https://onnxruntime.ai/docs/install

Installs the ONNX Runtime package with DirectML support for Windows. This leverages DirectML for hardware acceleration on DirectX-compatible GPUs.

```bash
pip install onnxruntime-directml
```

--------------------------------

### Pre-process Prompt and Setup Generation in C++

Source: https://onnxruntime.ai/docs/genai/tutorials/snapdragon

Pre-processes a user prompt into tokens using the tokenizer and sets up the generator with specified parameters. This involves encoding the prompt, creating generator parameters, and initializing the generator with the model and token sequences.

```cpp
auto sequences = OgaSequences::Create();
tokenizer->Encode(prompt.c_str(), *sequences);

auto params = OgaGeneratorParams::Create(*model);
params->SetSearchOption("max_length", 1024);
auto generator = OgaGenerator::Create(*model, *params);
generator->AppendTokenSequences(*sequences);
```

--------------------------------

### Get Profiling Start Time

Source: https://onnxruntime.ai/docs/api/c/struct_ort_1_1detail_1_1_session_impl

Retrieves the start time of the current profiling session in nanoseconds.

```APIDOC
## GET /profiling/start_time

### Description
Wraps `OrtApi::SessionGetProfilingStartTimeNs` to retrieve the start time of the profiling session.

### Method
GET

### Endpoint
/profiling/start_time

### Parameters
None

### Response
#### Success Response (200)
- **start_time_ns** (uint64_t) - The profiling start time in nanoseconds.
```

--------------------------------

### Install Xcode Command Line Tools

Source: https://onnxruntime.ai/docs/tutorials/mobile/deploy-ios

Installs essential command-line developer tools for Xcode, which may be required for various build and development tasks on macOS.

```shell
xcode-select --install
```

--------------------------------

### Create C# Console Project (dotnet CLI)

Source: https://onnxruntime.ai/docs/tutorials/csharp/yolov3_object_detection_csharp

This command initializes a new C# console application project. It sets up the basic project structure and configuration files required for a .NET Core application.

```bash
dotnet new console
```

--------------------------------

### Convert TFLite Model to ONNX using CLI

Source: https://onnxruntime.ai/docs/tutorials/tf-get-started

Converts a TensorFlow Lite (TFLite) model to ONNX format using the tf2onnx command-line interface. Requires tf2onnx to be installed. The command specifies the input TFLite model file, output ONNX file path, and the ONNX opset version.

```bash
python -m tf2onnx.convert --tflite path/to/model.tflite --output dst/path/model.onnx --opset 13

```

--------------------------------

### Install ONNX Runtime Python Wheel

Source: https://onnxruntime.ai/docs/build/training

Installs the built ONNX Runtime Python wheel package using pip. Assumes the wheel file is located in the specified build output directory.

```bash
python -m pip install build/Linux/RelWithDebInfo/dist/*.whl
```

--------------------------------

### Install ONNX Runtime Python Wheel

Source: https://onnxruntime.ai/docs/build/eps

Installs a locally built ONNX Runtime Python wheel. The filename may vary based on version and system architecture.

```bash
pip install "build\Release\Release\dist\onnxruntime-1.23.0-cp312-cp312-win_amd64.whl"
```

--------------------------------

### Get Profiling Start Time

Source: https://onnxruntime.ai/docs/api/c/struct_ort_1_1detail_1_1_session_impl-members

Retrieves the start time in nanoseconds for profiling operations within the ONNX Runtime session.

```cpp
GetProfilingStartTimeNs() const
```

--------------------------------

### Download Phi-3 Model for DirectML

Source: https://onnxruntime.ai/docs/genai/tutorials/phi3-python

Downloads the Phi-3 mini 4k instruct ONNX model specifically for DirectML acceleration. The `--include directml/*` flag ensures only DirectML related files are downloaded, and `--local-dir .` places them in the current directory.

```bash
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-onnx --include directml/* --local-dir .
```

--------------------------------

### Linux/macOS Installation from Source for ONNX Runtime Extensions (Python)

Source: https://onnxruntime.ai/docs/extensions

Installs ONNX Runtime Extensions from its GitHub repository for Linux and macOS. This method requires a C++ compiler toolkit (gcc later than g++ 8.0 or clang) to be installed. It installs the package directly from the source code.

```bash
python -m pip install git+https://github.com/microsoft/onnxruntime-extensions.git
```

--------------------------------

### Install Ninja Build Tool

Source: https://onnxruntime.ai/docs/build/web

Installs the Ninja build tool using pip, which is a prerequisite for building ONNX Runtime for Web.

```bash
pip install ninja
```

--------------------------------

### Run Ubuntu Docker Container with QEMU

Source: https://onnxruntime.ai/docs/build/inferencing

Starts an Ubuntu Docker container for aarch64 architecture, mounting the QEMU static binary for cross-architecture emulation. This is used to prepare manylinux environments.

```bash
docker run -v /usr/bin/qemu-aarch64-static:/usr/bin/qemu-aarch64-static -it --rm quay.io/pypa/manylinux2014_aarch64 /bin/bash
```

--------------------------------

### Convert Keras Model to ONNX using Python API

Source: https://onnxruntime.ai/docs/tutorials/tf-get-started

Converts a TensorFlow Keras model or tf function to ONNX format using the tf2onnx Python API. Requires TensorFlow and tf2onnx to be installed. The function takes the model, input signature, and opset version as input, and outputs an ONNX model object that can be saved.

```python
import tensorflow as tf
import tf2onnx
import onnx

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(4, activation="relu"))

input_signature = [tf.TensorSpec([3, 3], tf.float32, name='x')]
# Use from_function for tf functions
onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature, opset=13)
onnx.save(onnx_model, "dst/path/model.onnx")

```

--------------------------------

### Install WinML for Windows Machine Learning

Source: https://onnxruntime.ai/docs/install

Installs the WinML package, recommended for Windows Machine Learning applications. This provides optimized performance on Windows devices.

```bash
dotnet add package Microsoft.AI.MachineLearning
```

--------------------------------

### Run Phi-3 QA Example on CPU

Source: https://onnxruntime.ai/docs/genai/tutorials/phi3-python

This snippet first downloads the 'phi3-qa.py' script and then executes it. It points to the model files downloaded for CPU execution and specifies 'cpu' as the execution provider. This allows you to interact with the Phi-3 model using your system's CPU.

```bash
curl https://raw.githubusercontent.com/microsoft/onnxruntime-genai/main/examples/python/phi3-qa.py -o phi3-qa.py
python phi3-qa.py -m cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4 -e cpu

```

--------------------------------

### Install Specific ONNX Runtime Release

Source: https://onnxruntime.ai/docs/performance/model-optimizations/ort-format-models

Installs a specific version of the ONNX Runtime Python package. This is useful when building from source to match the Python package version to the ONNX Runtime repository branch. For example, installing version 1.7.2.

```bash
git checkout rel-1.7.2
pip install onnxruntime==1.7.2
```

--------------------------------

### Import ONNX Runtime Node.js Binding (CommonJS)

Source: https://onnxruntime.ai/docs/get-started/with-javascript/node

Shows how to import the ONNX Runtime Node.js binding using the CommonJS style import syntax. This is an alternative method for importing the library in Node.js environments that utilize CommonJS modules.

```javascript
// or use CommonJS style import syntax
const ort = require('onnxruntime-node');
```

--------------------------------

### Install ONNX Runtime Training CPU (pip)

Source: https://onnxruntime.ai/docs/install

Installs ONNX Runtime for on-device training on CPU, along with necessary Python dependencies like `numpy`, `protobuf`, and `setuptools`. It uses a specific package index for ORT builds.

```bash
python -m pip install cerberus flatbuffers h5py numpy>=1.16.6 onnx packaging protobuf sympy setuptools>=41.4.0
pip install -i https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT/pypi/simple/ onnxruntime-training-cpu

```

--------------------------------

### Install ONNX Runtime GenAI for CPU

Source: https://onnxruntime.ai/docs/genai/tutorials/deepseek-python

Installs the onnxruntime-genai and olive libraries along with their dependencies for CPU usage. It requires creating and activating a virtual environment before running the pip install command.

```shell
python -m venv .venv && source .venv/bin/activate
pip install requests numpy --pre onnxruntime-genai olive-ai
```

--------------------------------

### Get Profiling Start TimeNs - C++

Source: https://onnxruntime.ai/docs/api/c/struct_ort_1_1detail_1_1_const_session_impl

Retrieves the profiling start time in nanoseconds for the ONNX session. This function within ConstSessionImpl wraps OrtApi::SessionGetProfilingStartTimeNs, providing timing information for performance analysis.

```cpp
#include <onnxruntime_cxx_api.h>

// Assuming session_object is an instance of Ort::ConstSessionImpl<SomeType>
uint64_t start_time_ns = session_object.GetProfilingStartTimeNs();
```

--------------------------------

### Install Python Wheel

Source: https://onnxruntime.ai/docs/genai/howto/build-from-source

Installs the generated Python wheel package into your application's environment. Ensure you are in the directory containing the wheel file.

```bash
# Change dir to the folder containing the onnxruntime-genai wheel
# Example for Linux: cd build/Linux/Release/wheel/
pip install *.whl
```

--------------------------------

### Custom Op - Get Start Version (C)

Source: https://onnxruntime.ai/docs/api/c/onnxruntime__cxx__api_8h_source

Retrieves the starting ONNX operator version supported by this custom operation implementation. This is part of the OrtCustomOp definition for version compatibility.

```c
int(* GetStartVersion)(const struct OrtCustomOp *op)
```

--------------------------------

### Install Dependencies with Pip

Source: https://onnxruntime.ai/docs/tutorials/azureml

Installs necessary Python libraries for PyTorch, HuggingFace Transformers, AzureML, ONNX Runtime, and Matplotlib. These are essential for model conversion and deployment.

```bash
pip install torch
pip install transformers
pip install azureml azureml.core
pip install onnxruntime
pip install matplotlib

```

--------------------------------

### Install ONNX Runtime Training for Python

Source: https://onnxruntime.ai/docs/install

Installs the ONNX Runtime Training package for Python using pip. This enables on-device training capabilities within Python environments.

```bash
pip install onnxruntime-training
```

--------------------------------

### Install ONNX Runtime TVM EP Package

Source: https://onnxruntime.ai/docs/execution-providers/community-maintained/TVM-ExecutionProvider

Installs the ONNX Runtime with TVM Execution Provider from a locally built wheel file. This step follows the installation of the TVM package.

```bash
cd <path_to_onnx_runtime>
python3 -m pip uninstall onnxruntime onnxruntime-tvm -y
whl_path=$(find ./build/<OS_NAME>/Release/dist -name "*.whl")
python3 -m pip install $whl_path
```

--------------------------------

### Example RISC-V Cross-Compilation Build Command

Source: https://onnxruntime.ai/docs/build/inferencing

Example command for building ONNX Runtime for RISC-V 64-bit on Linux. It includes parallel build, debug configuration, toolchain paths, and skipping tests.

```bash
./build.sh --parallel --config Debug --rv64 --riscv_toolchain_root=/path/to/toolchain/root --riscv_qemu_path=/path/to/qemu-riscv64 --skip_tests
```

--------------------------------

### Get Profiling Start Time

Source: https://onnxruntime.ai/docs/api/python/modules/onnxruntime/capi/onnxruntime_inference_collection

Retrieves the profiling start time in nanoseconds. This value can be compared with `time.monotonic_ns()` in Python 3.3+. Note that precision may vary by platform (e.g., ~100ns on Windows/macOS).

```python
return self._sess.get_profiling_start_time_ns
```

--------------------------------

### Install ONNX Runtime CPU (Python)

Source: https://onnxruntime.ai/docs/install

Installs the CPU version of ONNX Runtime using pip. This is the most basic installation and does not require specific hardware accelerators.

```python
pip install onnxruntime

```

--------------------------------

### Build with TensorRT Execution Provider

Source: https://onnxruntime.ai/docs/build/eps

To build ONNX Runtime with the TensorRT Execution Provider, specify the TensorRT installation path using `--tensorrt_home <path>`. This requires CUDA and cuDNN to be installed. Example: `--tensorrt_home /usr/local/tensorrt`.

```bash
onnxruntime_build_script --use_cuda --tensorrt_home /usr/local/tensorrt
```

--------------------------------

### Setup emsdk for WebAssembly Build

Source: https://onnxruntime.ai/docs/build/web

These commands are used to set up the Emscripten SDK (emsdk), which is necessary for compiling C/C++ code to WebAssembly. This is typically done on non-Windows systems.

```bash
git submodule sync --recursive
git submodule update --init --recursive

./emsdk/emsdk install latest
./emsdk/emsdk activate latest
source ./emsdk_env.sh
```

--------------------------------

### Get Profiling Start Time

Source: https://onnxruntime.ai/docs/api/java/index-all

Returns the timestamp, in nanoseconds, when profiling began for an OrtSession. This is useful for performance analysis and debugging.

```java
getProfilingStartTimeInNs() - Method in class ai.onnxruntime.OrtSession
    
Returns the timestamp that profiling started in nanoseconds.
```