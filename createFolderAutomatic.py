import os
import shutil
from datetime import datetime

def organize_files(directory, extensions=['jpg', 'jpeg', 'png', 'mov', 'mp4', 'heic', 'heif']):
  """Mengorganisir file berdasarkan tanggal modifikasi.

  Args:
    directory: Direktori sumber file.
    extensions: List ekstensi file yang akan diproses.
  """

  for root, _, files in os.walk(directory):
    for file in files:
      # Cek ekstensi file
      if file.lower().endswith(tuple(ext.lower() for ext in extensions)):
        file_path = os.path.join(root, file)

        # Hapus sufiks angka (asumsi sufiks selalu berupa angka)
        filename, ext = os.path.splitext(file)
        if "_" in filename:
            filename = filename.rsplit("_", 1)[0]
        new_filename = filename + ext
        
        # Dapatkan tanggal modifikasi dan format ke string
        mod_time = os.path.getmtime(file_path)
        mod_date = datetime.fromtimestamp(mod_time).strftime('%d-%m-%Y')

        # Buat folder berdasarkan tanggal
        dest_dir = os.path.join(root, mod_date)
        if not os.path.exists(dest_dir):
          os.makedirs(dest_dir)

        # Pindahkan file ke folder baru
        dest_file = os.path.join(dest_dir, file)
        shutil.move(file_path, dest_file)
        print(f"Memindahkan {file} ke {dest_dir}")

# Contoh penggunaan
directory = r"C:\Users\Windows\Downloads\Foto Pribadi\restore"
organize_files(directory)