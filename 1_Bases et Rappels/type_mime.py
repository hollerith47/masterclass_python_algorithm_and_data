# codingame.com

def extract_file_extension(filename):
    s = filename.split(".")
    ext = ''
    if len(s) == 1:
        return None
    return s[-1]


t = {"name": "Herman", "age": 25}
print(t.get('firstname'))
print(extract_file_extension("testhtml"))
