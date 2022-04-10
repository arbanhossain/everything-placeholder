def send_code(lang, dirpath):
  if lang == None: lang = 'c'
  with open(f'{dirpath}/{lang}.txt') as f:
    return f.read()

if __name__ == "__main__":
  pass