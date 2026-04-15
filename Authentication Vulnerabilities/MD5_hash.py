import hashlib
from pathlib import Path
import base64

def md5_hash(data: str) -> str:
    # chuyển string -> bytes
    data_bytes = data.encode('utf-8')
    
    # tạo object md5
    md5 = hashlib.md5()
    
    # update dữ liệu
    md5.update(data_bytes)
    
    # trả về hex digest
    return md5.hexdigest()


def generate_cookie(input_path: str, ouput_path: str, username: str):
    in_file = Path(input_path)
    out_file = Path(ouput_path)

    lines_out = []

    with in_file.open("r", encoding="utf-8") as f:
        for line in f:
            password = line.strip()
            if not password:
                continue
            
            hashed = md5_hash(password)
            encoded = base64.b64encode(f"{username}:{hashed}".encode()).decode()
            lines_out.append(encoded)

    with out_file.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines_out))


if __name__ == "__main__":
    generate_cookie("password.txt", "stay-logged-in-cookie.txt", "carlos")