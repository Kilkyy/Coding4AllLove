import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Load the YOLO v4-tiny model and weights
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

# Initialize the ROS node and CvBridge object
rospy.init_node('object_tracker')
bridge = CvBridge()

# Create a subscriber to the camera image topic
def image_callback(msg):
    try:
        # Convert the ROS image message to a NumPy array
        image = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    else:
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

