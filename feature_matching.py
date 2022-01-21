import cv2 as cv # 4.5.5
import numpy as np
from glob import glob
from matplotlib import pyplot as plt
import utils

assets_loaded = utils.load_test_assets()
# print(assets_loaded)


assets = glob('output/*.png')
base_image = 'simple2.png'
base = cv.imread('screens/1080x1920/'+str(base_image))
# cv.imshow('base', base)
# cv.waitKey(0)
# cv.destroyAllWindows()


sift = cv.SIFT_create() # features extractor

base_img = cv.imread('screens/1080x1920/simple2.png' ,cv.IMREAD_GRAYSCALE)
kp_base, des_base = sift.detectAndCompute(base_img, None)

MIN_MATCH_COUNT = 10
FLANN_INDEX_KDTREE = 1 # align exposures 
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=100)
flann = cv.FlannBasedMatcher(index_params, search_params)

colors = [(255,0,0), (0,255,0), (0,0,255), (0,255,255), (255,255,255)]
i = 0

# for asset in 
# for asset in assets[57:58]:
# for asset in assets[54:63]:
for asset in assets_loaded['monsters']:
# for asset in assets[77:82]:

    img = cv.imread(asset) # read asset 

    # rescale x4
    scale_percent = 400 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    cv.imwrite('test/'+asset+'.png', img)
    # cv.imshow('frame', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    # look up 
    # cv.imshow('img', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # to gray

    # find descriptors and match
    kp, des = sift.detectAndCompute(gray, None)
    matches = flann.knnMatch(des, des_base, k=2)
    print(matches)
    
    good = []
    for m, n in matches:
        if m.distance < 0.8*n.distance: # you may adjust value here
            good.append(m)
    

    if len(good) > MIN_MATCH_COUNT:

        src_pts = np.float32(
            [kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32(
            [kp_base[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        
        for point in dst_pts:
            cv.circle(base,(int(point[0][0]), int(point[0][1])),3,colors[i%len(colors)],5)
    i += 1

scale_percent = 40 # percent of original size
width = int(base.shape[1] * scale_percent / 100)
height = int(base.shape[0] * scale_percent / 100)
dim = (width, height)
base = cv.resize(base, dim, interpolation = cv.INTER_AREA)

cv.imshow('frame', base)
cv.imwrite('feature_matching2.jpg', base)
cv.waitKey(0)
cv.destroyAllWindows()

