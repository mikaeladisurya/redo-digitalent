hour = int(input("Starting time (hour) :" ))
mins = int(input("Starting time (minute) :"))

duration = int(input("Duration (minute): "))

hour_passed = (mins + duration) // 60

mins_end = (mins + duration) % 60
hour_end = hour + hour_passed

print("Time passed =", str(hour_end) + ":" + str(mins_end))
