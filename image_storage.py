from google.cloud import storage
from firebase import firebase as fb
import encrypt
import os
import time


def upload_image(path_to_image, poster_name):
    ts = time.time()
    encrypt.decrypt('encrypted', os.environ['encryption_key'], 'credentials.json')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
    fb.FirebaseApplication('https://tribe-images.appspot.com')
    client = storage.Client()
    bucket = client.get_bucket('tribe-images.appspot.com')
    # posting to firebase storage
    image_blob = bucket.blob(poster_name + "/" + path_to_image + str(ts))
    image_blob.upload_from_filename(path_to_image)

#
# def images_to_movie():
#     # Construct the argument parser and parse the arguments
#     ap = argparse.ArgumentParser()
#     ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
#     ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
#     args = vars(ap.parse_args())
#
#     # Arguments
#     dir_path = '.'
#     ext = args['extension']
#     output = args['output']
#
#     images = []
#     for f in os.listdir(dir_path):
#         if f.endswith(ext):
#             images.append(f)
#
#     # Determine the width and height from the first image
#     image_path = os.path.join(dir_path, images[0])
#     frame = cv2.imread(image_path)
#     cv2.imshow('video', frame)
#     height, width, channels = frame.shape
#
#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
#     out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
#
#     for image in images:
#
#         image_path = os.path.join(dir_path, image)
#         frame = cv2.imread(image_path)
#
#         out.write(frame)  # Write out frame to video
#
#         cv2.imshow('video', frame)
#         if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
#             break
#
#     # Release everything if job is finished
#     out.release()
#     cv2.destroyAllWindows()
#     return output