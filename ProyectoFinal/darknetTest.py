import cv2
# import darknet functions to perform object detections
from darknet import *

# load in our YOLOv4 architecture network
network, class_names, class_colors = load_network("model/yolov4-obj.cfg", "model/obj.data", "model/yolov4-obj_best.weights")
width = network_width(network)
height = network_height(network)

# darknet helper function to run detection on image
def darknet_helper(img, width, height):
  darknet_image = make_image(width, height, 3)
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img_resized = cv2.resize(img_rgb, (width, height),
                              interpolation=cv2.INTER_LINEAR)

  # get image ratios to convert bounding boxes to proper size
  img_height, img_width, _ = img.shape
  width_ratio = img_width/width
  height_ratio = img_height/height

  # run model on darknet style image to get detections
  copy_image_from_bytes(darknet_image, img_resized.tobytes())
  detections = detect_image(network, class_names, darknet_image)
  free_image(darknet_image)
  return detections, width_ratio, height_ratio

def set_bounding_boxes(img):
  detections, width_ratio, height_ratio = darknet_helper(img, width, height)
  for label, confidence, bbox in detections:
      left, top, right, bottom = bbox2points(bbox)
      left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
      cv2.rectangle(img, (left, top), (right, bottom), class_colors[label], 2)
      cv2.putText(img, "{} [{:.2f}]".format(label, float(confidence)),
                          (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                          class_colors[label], 2)

if __name__ == "__main__":

    WINDOW_WIDTH    = 640
    WINDOW_HEIGHT   = 480

    cap = cv2.VideoCapture(0)
    cap.set(3,WINDOW_WIDTH)     #width=640
    cap.set(4,WINDOW_HEIGHT)    #height=480

    cv2.namedWindow('video_feed')

    frame = None

    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break
        # Display the resulting frame
        set_bounding_boxes(frame)
        cv2.imshow('video_feed',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()