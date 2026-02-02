"""
VR Image Optimizer
Compresses JPG images with minimal quality loss using:
- High quality (95%) JPEG compression
- Progressive encoding (faster perceived load)
- Optimized Huffman tables
- Stripped metadata
"""

import os
from PIL import Image
import shutil

# Configuration
INPUT_DIR = r"c:\Users\resha\OneDrive\문서\ELGI_VR_360-main\ELGI_VR_360-main\Assets"
OUTPUT_DIR = r"c:\Users\resha\OneDrive\문서\ELGI_VR_360-main\ELGI_VR_360-main\Assets_Optimized"
BACKUP_DIR = r"c:\Users\resha\OneDrive\문서\ELGI_VR_360-main\ELGI_VR_360-main\Assets_Backup"

# Quality settings (95 = nearly lossless, 85 = good balance, 75 = smaller files)
JPEG_QUALITY = 92  # High quality - minimal visible difference
MAX_DIMENSION = 8192  # Max width/height for 8K quality

def optimize_images():
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    total_original = 0
    total_optimized = 0
    
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    print(f"\n📸 Found {len(files)} images to optimize\n")
    print("-" * 60)
    
    for filename in sorted(files):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)
        backup_path = os.path.join(BACKUP_DIR, filename)
        
        original_size = os.path.getsize(input_path)
        total_original += original_size
        
        try:
            # Open image
            img = Image.open(input_path)
            
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Resize if too large (optional - comment out to keep original size)
            # width, height = img.size
            # if width > MAX_DIMENSION or height > MAX_DIMENSION:
            #     img.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.LANCZOS)
            
            # Save with optimization
            img.save(
                output_path,
                'JPEG',
                quality=JPEG_QUALITY,
                optimize=True,        # Optimize Huffman tables
                progressive=True,     # Progressive JPEG (faster perceived load)
            )
            
            optimized_size = os.path.getsize(output_path)
            total_optimized += optimized_size
            
            reduction = ((original_size - optimized_size) / original_size) * 100
            
            print(f"✅ {filename}")
            print(f"   Original: {original_size / 1024 / 1024:.1f} MB → Optimized: {optimized_size / 1024 / 1024:.1f} MB ({reduction:.0f}% smaller)")
            
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
            # Copy original if optimization fails
            shutil.copy2(input_path, output_path)
            total_optimized += original_size
    
    print("-" * 60)
    print(f"\n📊 SUMMARY:")
    print(f"   Total Original: {total_original / 1024 / 1024:.1f} MB")
    print(f"   Total Optimized: {total_optimized / 1024 / 1024:.1f} MB")
    print(f"   Space Saved: {(total_original - total_optimized) / 1024 / 1024:.1f} MB ({((total_original - total_optimized) / total_original) * 100:.0f}%)")
    print(f"\n📁 Optimized images saved to: {OUTPUT_DIR}")
    print(f"\n⚠️  To use optimized images:")
    print(f"   1. Backup your current Assets folder")
    print(f"   2. Replace Assets contents with Assets_Optimized contents")

if __name__ == "__main__":
    print("\n🚀 VR Image Optimizer")
    print("=" * 60)
    optimize_images()
