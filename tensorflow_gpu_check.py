import os

# Hide INFO logs but keep warnings and errors
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf


print("=" * 50)
print("TensorFlow GPU Environment Check")
print("=" * 50)

# Basic version info
print("TF Version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())

gpus = tf.config.list_physical_devices("GPU")
print("Detected GPUs:", gpus)

# Fail clearly if GPU not detected
if not gpus:
    raise RuntimeError("❌ No GPU detected by TensorFlow!")

print("\nBuild info:")
build_info = tf.sysconfig.get_build_info()
for key in sorted(build_info):
    print(f"  {key}: {build_info[key]}")

# Simple GPU computation test
print("\nRunning test computation on GPU...")

with tf.device("/GPU:0"):
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    c = tf.matmul(a, b)

print("Result:")
print(c)

print("\n✅ GPU is working correctly!")
