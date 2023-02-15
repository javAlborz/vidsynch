import cv2
import numpy as np

def synchronize_videos(video_list):
    # reading the frames
    frame_list = []
    for video in video_list:
        cap = cv2.VideoCapture(video)
        frames = []
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frames.append(frame)
            else:
                break
        frame_list.append(frames)

    # synchronizing the frames
    min_len = min([len(frames) for frames in frame_list])
    for i in range(len(frame_list)):
        frame_list[i] = frame_list[i][:min_len]

    # writing the synchronized video
    cap = cv2.VideoCapture(video_list[0]) # get dimension of first video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_width = width * len(video_list)
    out = cv2.VideoWriter('synchronized_video.avi',cv2.VideoWriter_fourcc(*'XVID'), 25.0, (total_width, height), True)

    for i in range(min_len):
        concatenated_frame = np.concatenate(
            [frame_list[j][i] for j in range(len(frame_list))],
            axis=1
        )
        out.write(concatenated_frame)
    out.release()

video_list = ['vid1.mp4', 'vid2.mp4']
synchronize_videos(video_list)

print("Synchronized video is saved")
