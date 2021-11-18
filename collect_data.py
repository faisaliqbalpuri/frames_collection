import yaml
config = lambda: None
import cv2 
import schedule
import datetime
from threading import Thread

with open(r'./config.yaml') as file:
	documents = yaml.full_load(file)
	for item, doc in documents.items():
		setattr(config, item, doc)


def time_in_range(start, end, current):
	return start <= current <= end

def read_rtsp(rtsp,index):
	cap = cv2.VideoCapture(rtsp)
	ret, frame = cap.read()
	frame_name= "{}/{}_frame_{}.jpg".format(config.save_path,config.image_name_prefix[index],datetime.datetime.now())
	cv2.imwrite(frame_name, frame)
	print('writing frame: '+frame_name)



def get_frame():
	for index,rtsp in enumerate(config.rtsp_link):
		api_thread = Thread(target=read_rtsp,args=(rtsp,index))
		api_thread.daemon = True
		api_thread.start()
		


	
schedule.every(config.minute_after_save_frame).minutes.do(get_frame)
while 1:
	if time_in_range(datetime.time(config.start_time[0],config.start_time[1],config.start_time[2]), datetime.time(config.end_time[0], config.end_time[1], config.end_time[2]), datetime.datetime.now().time()) :
		schedule.run_pending()
	else:
		break
	