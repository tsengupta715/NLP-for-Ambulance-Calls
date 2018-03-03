

hospital_summary = input("Enter Summary: ")
EMS = "EMS"
ems_detected = hospital_summary.find(EMS)

if ems_detected > -1:
    print("EMS needed")
else:
    print("EMS not needed")
