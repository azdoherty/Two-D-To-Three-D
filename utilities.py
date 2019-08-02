import numpy as np
import cv2
import os


class ImageMatcher:
    def __init__(self, *args):
        """
        set up the image matcher
        
        """
        if len(args) == 0:
            self.detector = cv2.xfeatures2d.SURF_create()

        self.save_path = None

    def match2(self, img_file_1, img_file_2):
        if not self.save_path:
            self.save_path = os.path.split(img_file_1)[0]

        img1 = cv2.imread(img_file_1)
        img2 = cv2.imread(img_file_2)
        m1 = self.find_matches(img1, save=True)

    def find_matches(self, img, save=False):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kps = self.detector.detect(gray, None)
        if save:
            img = cv2.drawKeypoints(gray, kps)
            img_path = os.path.join(self.save_path, 'test.png')
            cv2.imwrite(img_path, img)
        return kps

class SiftExtractor:
    def __init__(self):
        self.scales = 4 # number of levels of gaussian to create
        self.kernel = cv2.getGaussianKernel(ksize=5, sigma=1)



    def make_levels(self, img):
        levels = [img]
        for i in range(1, self.scales):
            half = resized_image = cv2.resize(levels[i-1], (.5, .5)) 
            levels.append(half)
        return levels



if __name__ == "__main__":
    """
    test code to verify utilities are working
    """
    img_file_1 = os.path.join('data', 'benchy', 'IMG_1569.JPG')
    img_file_2 = os.path.join('data', 'benchy', 'IMG_1570.JPG')
    s = SiftExtractor()
    print(s.kernel)



    