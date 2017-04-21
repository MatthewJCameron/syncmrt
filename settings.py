import numpy as np

class settings():
	def __init__(self):
		self.markerQuantity = 3
		self.markerSize = 2.00

		self.chairOrientation = '-ap-hf'

		self.hamamatsuPixelSize = 0.16145
		self.hamamatsuAlignmentIsoc = np.array([637.5,239.5,637.5])*self.hamamatsuPixelSize

		self.xrayIsLoaded = False
		self.ctIsLoaded = False