# Long-exposure simulation from video. Usage: vid_long_expose_max.py source_video target_image
import sys
import numpy as np
import imageio
filename = sys.argv[1]
vid = imageio.get_reader(filename)
target = vid.get_data(0)
last_frame = len(vid)
for i, img in enumerate(vid):
    percent = int((i*100+1)/last_frame)
    sys.stdout.write("\r["+('#'*int(percent/4))+('.'*(25-int(percent/4)))+("] %d"%percent+"%"+" (%d"%i+"/%d"%last_frame+")"))
    sys.stdout.flush()
    target = np.maximum(target, img)
vid.close()
imageio.imwrite(sys.argv[2], target)
