import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm

# Read the image
img = cv2.imread('/path/to/your/image')
s = img.shape

# Determine the center points
p = s[0] // 2
o = s[1] // 2

# Define ranges for sampling
if p > o:
    y = x = list(range(0, o-1, o // 20))
    a = b = list(range(o, 2*o, o // 20))
else:
    y = x = list(range(0, p, p // 20))
    a = b = list(range(p+1, 2*p, p // 20))

if len(a) > len(x):
    b = a = a[:-(len(a)-len(x))]

# Sample points from the image
t = img[x, y]
e = img[a, b]

# Prepare data for KMeans
X = []
if len(a) > len(x):
    for i in range(len(x)):
        X.append(t[i].flatten())
        X.append(e[i].flatten())
else:
    for i in range(len(a)):
        X.append(t[i].flatten())
        X.append(e[i].flatten())

# Convert X to a numpy array
X = np.array(X)

# Fit KMeans
kmeans = KMeans(n_clusters=1)
kmeans.fit(X)
centroid = kmeans.cluster_centers_

# Extract centroid coordinates
x1 = centroid[0][0]
y1 = centroid[0][1]

# Prepare SVM data
data = [
    [121, 83], [83, 230], [112, 110], [79, 31], [110, 85], [57, 64], [127, 121], [45, 99], [33, 59], [29, 65], [79, 31], 
    [108, 79], [108, 107], [54, 45], [41, 120], [62, 94], [57, 25], [97, 51], [59, 38], [58, 54], [136, 114], [60, 84], 
    [66, 54], [148, 52], [96, 136], [97, 125], [65, 70], [106, 85], [124, 123], [37, 66], [55, 88], [78, 129], [157, 70], 
    [49, 60], [90, 88], [56, 32], [80, 94], [60, 81], [36, 103], [70, 99], [80, 80], [168, 152], [167, 115], [196, 164], 
    [151, 145], [181, 135], [175, 182], [151, 145], [181, 135], [193, 94], [150, 162], [184, 38], [202, 59], [164, 178], 
    [113, 167], [72, 178], [201, 140], [61, 161], [73, 216], [152, 80], [203, 186], [165, 175], [182, 125], [159, 116], 
    [160, 240], [157, 180], [199, 140], [212, 124], [128, 154], [196, 154], [207, 175], [157, 157], [185, 130], [181, 228], 
    [196, 186], [110, 175], [177, 159], [155, 120], [216, 77], [186, 130], [188, 167], [185, 142]
]

target = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]

# Train the SVM classifier
clf = svm.SVC(gamma=0.0001, C=100)
clf.fit(data, target)

# Predict the fabric type
arraypred = [x1, y1]
x = clf.predict([arraypred])

if x == 0:
    print("COTTON")
elif x == 1:
    print("SILK")
else:
    print("NA")
