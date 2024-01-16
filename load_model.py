import ssl
import easyocr
ssl._create_default_https_context = ssl._create_unverified_context
if __name__ == '__main__':
    reader = easyocr.Reader(['ja'])
    result = reader.readtext('test.jpg')
    print(result)
