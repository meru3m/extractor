import zipfile

def extract_archive(archive_path, destination_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_dir)

if __name__ == "__main__":
    extract_archive(r"D:\File Compressor\destination\compressed.zip", r"D:\Python Udemy\todo\Exercise\extracted")
