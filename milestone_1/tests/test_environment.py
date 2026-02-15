print("Checking Dask and Ray installation...\n")

# Check Dask
try:
    import dask
    print("Dask is installed successfully!")
except ImportError:
    print("Dask is NOT installed.")

# Check Ray
try:
    import ray
    ray.init(ignore_reinit_error=True)
    print("Ray is installed and initialized successfully!")
    ray.shutdown()
except ImportError:
    print("Ray is NOT installed.")
except Exception as e:
    print("Ray failed to initialize:", e)

print("\nEnvironment check complete!")
