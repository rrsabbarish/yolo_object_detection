import cv2
img_size = (416,416)
for i in range(1,3001):
    filename = 'armas ('+str(i)+').jpg'
    path = '../data/artifacts/images/' + filename
    img = cv2.imread(path)
    img = cv2.resize(img, img_size, cv2.INTER_LINEAR)
    cv2.imwrite(path,img)