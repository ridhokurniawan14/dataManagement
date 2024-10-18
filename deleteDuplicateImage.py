import os
import hashlib

def file_hash(file_path, chunk_size=1024):
    """Menghitung hash SHA256 dari sebuah file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            sha256.update(chunk)
    return sha256.hexdigest()

def remove_duplicate_photos(directory, extensions=['jpg', 'jpeg', 'png', 'mov', 'mp4', 'heic', 'heif']):
    """Menghapus foto duplikat berdasarkan isi (bukan nama), menyisakan file yang paling besar."""
    file_dict = {}  # Dictionary untuk menyimpan file dengan hash sebagai kuncinya
    
    for root, _, files in os.walk(directory):
        for file in files:
            # Cek apakah file punya ekstensi yang sesuai
            if file.lower().endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                
                # Dapatkan hash file
                file_hash_value = file_hash(file_path)
                
                # Cek apakah hash ini sudah ada
                if file_hash_value in file_dict:
                    # Jika sudah ada file dengan hash yang sama, bandingkan ukuran file
                    existing_file_path = file_dict[file_hash_value]
                    existing_size = os.path.getsize(existing_file_path)
                    current_size = os.path.getsize(file_path)
                    
                    # Jika ukuran file sama, hapus salah satu
                    if current_size == existing_size:
                        print(f"Menghapus duplikat: {file_path}")
                        os.remove(file_path)
                    else:
                        # Hapus file yang lebih kecil
                        if current_size > existing_size:
                            print(f"Menghapus file lebih kecil: {existing_file_path}")
                            os.remove(existing_file_path)
                            file_dict[file_hash_value] = file_path  # Simpan yang lebih besar
                        else:
                            print(f"Menghapus file lebih kecil: {file_path}")
                            os.remove(file_path)
                else:
                    # Jika hash belum ada, simpan ke dictionary
                    file_dict[file_hash_value] = file_path

# Contoh penggunaan
directory = r"C:\Users\Windows\Downloads\Foto Pribadi\restore"
remove_duplicate_photos(directory)