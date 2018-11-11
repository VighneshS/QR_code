import os
from datetime import datetime

import qrcode

qrMessage = 'https://qa.revature.com'
timestampFormat = "%d-%m-%Y_%H-%M-%S"
directoryName = "generatedQRS/"
saveFormat = "png"
img = qrcode.make(qrMessage)
fileName = str(datetime.now().strftime(timestampFormat))
fullFilePath = directoryName + fileName + '.' + saveFormat
directory = os.path.dirname(fullFilePath)

if not os.path.exists(directory):
    os.makedirs(directory)

img.save(fullFilePath)
img.show()
