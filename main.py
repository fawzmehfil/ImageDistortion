from PIL import Image
from typing import List


def mirror(raw: List[List[List[int]]])-> None:
  if raw == []:
      return []

  for image in raw:
    image.reverse()


def grey(raw: List[List[List[int]]]) -> None:
    if raw == []:
      return []

    avg=0
    for image in raw:
        for row in image:
            avg=(sum(row))//len(row)
            for i in range(len(row)):
                row[i] = avg


def invert(raw: List[List[List[int]]]) -> None:
    if raw == []:
      return []

    for image in range(len(raw)):
        for row in range(len(raw[image])):

            maxi = max(raw[image][row])
            mini = min(raw[image][row])

            for item in range(len(raw[image][row])):
              if raw[image][row][item] == maxi:
                raw[image][row][item] = mini
              elif raw[image][row][item] == mini:
                raw[image][row][item] = maxi


def merge(raw1: List[List[List[int]]], raw2: List[List[List[int]]])-> List[List[List[int]]]:
    
    if raw1 == [] or raw2 == []:
      return []

    mh1, mw1 = len(raw1), max(len(row) for row in raw1)
    mh2, mw2 = len(raw2), max(len(row) for row in raw2)

    mh = max(mh1, mh2)
    mw = max(mw1, mw2)

    endlist = []
    merged_rows = []

    for i in range(mh):
        row_to_merge = []

        for j in range(mw):
            item1 = item_index(i, j, raw1)
            item2 = item_index(i, j, raw2)

            if item1 == [255, 255, 255]:
                row_to_merge.append(item2)

            elif item2 == [255, 255, 255]:
                row_to_merge.append(item1)

            elif i % 2 == 0:
                row_to_merge.append(item1)

            else:
                row_to_merge.append(item2)

        merged_rows.append(row_to_merge)

    endlist.append(merged_rows)
    return endlist

def item_index(a,b,c):
        if a < len(c) and b < len(c[a]):
            return c[a][b]
        return [255, 255, 255]
    
    


def compress(raw: List[List[List[int]]])-> List[List[List[int]]]:

  if raw == []:
    return []

  list_compressed = []

  for i in range(0, len(raw),2):
    row=[]
    for j in range(0, len(raw[i]), 2):
      items = [raw[i][j]]

      if i + 1 < len(raw):
          items.append(raw[i + 1][j])

          if j + 1 < len(raw[i]):
              items.append(raw[i][j + 1])
              
          if i + 1 < len(raw) and j + 1 < len(raw[i]):
              items.append(raw[i + 1][j + 1])
          
          avg = [sum(val) // len(val) for val in zip(*items)]
          row.append(avg)

      list_compressed.append(row)

      new_row = []

      for r1 in list_compressed:

        if r1 not in new_row:

          new_row.append(r1)

  return new_row


"""
**********************************************************

Do not worry about the code below. However, if you wish,
you can us it to read in images, modify the data, and save
new images.

**********************************************************
"""

def get_raw_image(name: str)-> List[List[List[int]]]:
    
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data


def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)
                      
                      




    
