import cv2
import numpy as np

# Load the YOLO v4-tiny model and weights
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

# Read in the input image
image = cv2.imread("input.jpg")

# Get the dimensions of the input image
(H, W) = image.shape[:2]

# Determine the output layer names for the YOLO v4-tiny model
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Create a blob from the input image and perform a forward pass
# through the network
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                              swapRB=True, crop=False)
net.setInput(blob)
layerOutputs = net.forward(ln)

# Initialize lists to store the bounding box predictions and
# associated confidence scores
boxes = []
confidences = []

# Loop over each of the layer outputs
for output in layerOutputs:
    # Loop over each of the detections
    for detection in output:
        # Extract the class ID and confidence (i.e., probability)
        # of the current object detection
        scores = detection[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]

        # Filter out weak predictions by ensuring the detected
        # probability is greater than the minimum probability
        if confidence > 0.5:
            # Scale the bounding box coordinates back relative to
            # the size of the image, keeping in mind that YOLO
            # actually returns the center (x, y)-coordinates of
            # the bounding box followed by the boxes' width and
            # height
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY, width, height) = box.astype("int")

            # Use the center (x, y)-coordinates to derive the top
            # and and left corner of the bounding box
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))

            # Update our list of bounding box coordinates,
            # confidences, and class IDs
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))

# Apply non-maxima suppression to suppress weak, overlapping
# bounding boxes
idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)

# Ensure at least one detection exists
if len(idxs) > 0:
    # Loop over the indexes we are keeping
    for i in idxs.flatten():
        # Extract the bounding box coordinates
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])


