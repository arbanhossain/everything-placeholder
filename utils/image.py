from PIL import Image, ImageColor

def get_image(width: int, height: int, color: str):
  try:
    ImageColor.getrgb(color)
  except ValueError:
    color = 'white'
  img = Image.new('RGB', (width, height), color=color)
  return img

if __name__ == "__main__":
  image = Image.new(mode='RGB', size=(100, 100))

  image.show()