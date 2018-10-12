#!/usr/bin/env python
import openpyxl
import openpyxl.drawing

IMAGE = 'NOTEBOOKS/images/guido.png'
wb = openpyxl.Workbook()
ws = wb.worksheets[0]
img = openpyxl.drawing.image.Image(IMAGE)
img.anchor(ws['Z100'])
ws.add_image(img)
wb.save('image_test.xlsx')
