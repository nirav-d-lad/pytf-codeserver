import torch

print("=" * 50)
print("PyTorch GPU Environment Check")
print("=" * 50)

print("PyTorch Version:", torch.__version__)
print("CUDA Available:", torch.cuda.is_available())

if not torch.cuda.is_available():
    raise RuntimeError("❌ No GPU detected by PyTorch!")

print("CUDA Version (built with):", torch.version.cuda)
print("Number of GPUs:", torch.cuda.device_count())

for i in range(torch.cuda.device_count()):
    print("\n" + "-" * 30)
    print(f"GPU {i}")
    print("-" * 30)

    print("  Name:", torch.cuda.get_device_name(i))
    print("  Compute Capability:", torch.cuda.get_device_capability(i))

    props = torch.cuda.get_device_properties(i)
    print("  Total Memory (GB):", round(props.total_memory / 1e9, 2))

print("\nRunning test tensor operation on GPU...")

x = torch.randn(3, 3, device="cuda")
print("Tensor device:", x.device)

print("\n✅ GPU is working correctly!")
