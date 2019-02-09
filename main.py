import cv2
import os

vidcap = cv2.VideoCapture(r'yourpath.avi')
success, image = vidcap.read()
count = 0
success = True
while success:
    cv2.imwrite("frame%d.png" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    count += 1

vidcap = cv2.VideoCapture(r'yourpath2')
success, image = vidcap.read()
success = True
while success:
    cv2.imwrite("frame%d.png" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    count += 1

image_folder = r'where_is_project'
video_name = 'output.mp4'
frame_rate = float(24) #masterrace
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
images = []
for i in range(500):
    images.append(os.path.join(image_folder, "frame%d.png" % i))

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, fourcc, frame_rate, (width, height))
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
video.release()
cv2.destroyAllWindows()
