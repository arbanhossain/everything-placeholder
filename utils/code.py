def send_code(lang, dirpath):
  if lang == None: lang = 'c'
  try:
    with open(f'{dirpath}/{lang}.txt') as f:
      return f.read()
  except:
    return send_code('c', dirpath)

if __name__ == "__main__":
  pass