import gzip
import pickle
import os

# Test loading compressed model
try:
    print("Testing compressed model loading...")
    
    # Check if file exists
    if os.path.exists('random_forest_final_model.pkl.gz'):
        print("✅ File random_forest_final_model.pkl.gz found")
        
        # Check file size
        size_mb = os.path.getsize('random_forest_final_model.pkl.gz') / 1024 / 1024
        print(f"✅ File size: {size_mb:.2f} MB")
        
        if size_mb < 25:
            print("✅ File size OK for GitHub (<25MB)")
        else:
            print("❌ File still too large for GitHub (>25MB)")
        
        # Try loading
        with gzip.open('random_forest_final_model.pkl.gz', 'rb') as f:
            model = pickle.load(f)
        
        print("✅ Model loaded successfully!")
        print(f"✅ Model type: {type(model)}")
        
        # Test prediction (dummy)
        if hasattr(model, 'predict'):
            print("✅ Model has predict method")
        
        if hasattr(model, 'predict_proba'):
            print("✅ Model has predict_proba method")
            
    else:
        print("❌ File random_forest_final_model.pkl.gz not found")
        print("Available files:")
        for f in os.listdir('.'):
            if f.endswith('.pkl.gz'):
                print(f"  - {f}")
        
except Exception as e:
    print(f"❌ Error loading model: {e}")
    
print("\nTest completed!")