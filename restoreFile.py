import os
import shutil

def restore_files(directory):
    """Mengembalikan semua file ke direktori induk dengan penambahan angka jika nama file sudah ada."""

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Gabungkan path file
            file_path = os.path.join(root, file)
            new_filename = file

            # Tambahkan angka jika nama file sudah ada
            i = 1
            while os.path.exists(os.path.join(directory, new_filename)):
                new_filename, ext = os.path.splitext(file)  # Pisahkan nama dan ekstensi
                new_filename = f"{new_filename}_{i}{ext}"  # Tambahkan angka ke nama file
                i += 1

            # Pindahkan file dengan nama baru
            shutil.move(file_path, os.path.join(directory, new_filename))

        # Hapus folder kosong atau folder yang hanya berisi file dengan nama folder tersebut
        for subdir in dirs[:]:  # Copy dirs list to avoid modification during iteration
            subdir_path = os.path.join(root, subdir)
            try:
                if not os.listdir(subdir_path):
                    os.rmdir(subdir_path)
                elif len(os.listdir(subdir_path)) == 1 and os.listdir(subdir_path)[0] == subdir:
                    # Check if the only file has the same name as the subfolder
                    file_path = os.path.join(subdir_path, os.listdir(subdir_path)[0])
                    if file_path != os.path.join(directory, subdir):  # Avoid deleting the renamed file
                        os.remove(file_path)
                        os.rmdir(subdir_path)
            except PermissionError:
                print(f"Permission denied: {subdir_path}. Skipping.")

# Contoh penggunaan
directory = r"C:\Users\Windows\Downloads\Foto Pribadi\restore"
restore_files(directory)
