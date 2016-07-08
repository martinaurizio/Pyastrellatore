#slicer
from PIL import Image

def slicer(image, npLato):
	if image.size[1] % npLato != 0 or image.size[0] % npLato != 0:
		raise ValueException("Immagine non divisibile per il numero di lati richiesto")
	else:
		smallL = image.size[0]//npLato
		smallH = image.size[1]//npLato
		for i in range (0, npLato):
			for j in range (0, npLato):
				f = image.crop((i*smallL, j*smallH, (i+1)*smallL, (j+1)*smallH))
				f.save("temp/Immagini{}_{}.png".format(i,j))
				
				
if __name__ == '__main__':
	imtest = Image.open('/home/martina/Scrivania/AhahaCheBello.png')
	print(imtest.size)
	slicer(imtest, 100)