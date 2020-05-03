import tkinter 
import speedtest
	
m = tkinter.Tk() 
m.iconbitmap('netspeed.ico')
m.title("Internet Speed Test")
m.geometry("180x120")
def speed():
	test = speedtest.Speedtest()
	# Perform download and upload speed tests (bits per second)
	download = test.download()
	upload = test.upload()
	# Convert download and upload speeds to megabits per second
	download_mbs = round(download /(10**6),2)
	upload_mbs = round(upload /(10**6),2)
	label1 = tkinter.Label(m,text=f"Download Speed : {download_mbs} Mbps \n Upload Speed : {upload_mbs} Mbps")
	label1.grid(row=2,column=0)
	
button = tkinter.Button(m, text='Start', width=25,command=speed)
button.grid(row=1,column=0)
m.mainloop()
