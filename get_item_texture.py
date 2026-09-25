import urllib.request
import base64

def get_base64_image():
    # just create a simple 1x1 green pixel base64 for now
    import struct
    import zlib
    def chunk(type, data):
        return struct.pack('>I', len(data)) + type + data + struct.pack('>I', zlib.crc32(type + data) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(b'\x00\x00\xff\x00')) # Green pixel
    png += chunk(b'IEND', b'')
    print(base64.b64encode(png).decode('utf-8'))

get_base64_image()
