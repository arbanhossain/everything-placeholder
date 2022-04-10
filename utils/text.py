import random

def gen_text(src, paragraphs, words=None):
  if (paragraphs is None and words is None):
    return src
  if words:
    total = src.split()
    if len(total) < int(words):
      for i in range(int(words) - len(total)):
        src += ' ' + random.choice(total)
    return ' '.join(src.split(' ')[:int(words)])
  for i in range(paragraphs - 1):
    src += '\n' + src
  return src

if __name__ == "__main__":
  pass