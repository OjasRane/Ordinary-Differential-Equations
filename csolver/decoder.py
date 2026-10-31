import numpy as np

def load(path, dtype=np.float64):
    with open(path, "rb") as file:
        file.seek(-3, 2)
        footer = file.read(3)
        file.seek(0)
        header = file.read(4)
        if header != b"CARL" or footer != b"QED":
            raise ValueError("Not a .jcbi file")
        version = int.from_bytes(file.read(1), byteorder="little")
        if version == 1:
            payload_type = file.read(1)
            if payload_type == b'V':
                length = int.from_bytes(file.read(8), byteorder="little")
                payload = np.frombuffer(file.read(np.dtype(dtype).itemsize * length), dtype=np.dtype(dtype))
                # if len(file.read(np.dtype(dtype).itemsize * length)) != np.dtype(dtype).itemsize * length:
                #     raise ValueError("File corrupted")
            elif payload_type == b'M':
                rows = int.from_bytes(file.read(8), byteorder="little")
                cols = int.from_bytes(file.read(8), byteorder="little")
                payload = np.frombuffer(file.read(np.dtype(dtype).itemsize * rows * cols), dtype=np.dtype(dtype))
                # if len(file.read(np.dtype(dtype).itemsize * rows * cols)) != np.dtype(dtype).itemsize * rows * cols:
                #     raise ValueError("File corrupted")
                payload = payload.reshape(rows, cols)
            else:
                raise ValueError("Not a valid .jcbi file")
        else:
            raise ValueError("Version not supported")

    return payload