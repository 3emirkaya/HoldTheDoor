import hashlib
import zlib
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def compute_checksums(filepath):
    if not os.path.exists(filepath):
        print(f"HATA: Dosya bulunamadi -> {filepath}")
        return None
    
    with open(filepath, 'rb') as f:
        data = f.read()
    
    crc32_val = f"{zlib.crc32(data) & 0xffffffff:08X}"
    md5_val = hashlib.md5(data).hexdigest().upper()
    sha1_val = hashlib.sha1(data).hexdigest().upper()
    
    return crc32_val, md5_val, sha1_val

def main():
    print("=" * 60)
    print(" YAM415 - G01 Hash Hesaplama Araci (CRC32, MD5, SHA-1)")
    print("=" * 60)
    
    files = [
        "YAM415_G01_ConceptDocument.pdf",
        "YAM415_G01_ProjectPlan.pdf"
    ]
    
    for filename in files:
        p1 = filename
        p2 = os.path.join("YAM415_G01_Midterm", filename)
        target = p1 if os.path.exists(p1) else (p2 if os.path.exists(p2) else None)
        
        print(f"\nDosya: {filename}")
        print("-" * 50)
        if target:
            crc32, md5, sha1 = compute_checksums(target)
            print(f"Yol           : {target}")
            print(f"CRC32         : {crc32}")
            print(f"MD5           : {md5}")
            print(f"SHA-1         : {sha1}")
        else:
            print(f"DURUM: Henuz bulunamadi.")
            print(f"-> {filename} dosyasini olusturdugunuzda buraya veya YAM415_G01_Midterm klasorune koyun.")

if __name__ == '__main__':
    main()
