class markers:
	""" Marker settings for fiducials. """
	quantity = 3
	size = 2.00

class files:
	""" Relative file locations. """
	patientSupports = '/resources/patientSupports.csv'
	detectors = '/resources/detectors.csv'

class imager:
	""" Settings for the imager configuration. """
	isocenter = [630.2,231.5]
	pixelSize = [0.158,0.158]
	sad = 0
	sid = 0

class irradiation:
	""" Settings for the delivery configuration. """
	maskSize = [5,5]
	speed = 2.5