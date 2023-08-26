
import cv2
from pyzbar.pyzbar import decode


class BarCodeManager:
    
    def scan_this_image(self,image):

        image_data = cv2.imread(image)
        detectedBarcodes = decode(image_data)
        if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!")
        else:
        
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes:
                (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                print(barcode.data)
                print(barcode.type)

                 
        #Display the image
        

 
if __name__ == "__main__":
  # Take the image from user
    image="chips_bc.png"
    file = open(image,'r')
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    bcm = BarCodeManager()
    bcm.scan_this_image(file)
