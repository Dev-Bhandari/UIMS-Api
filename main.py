from uims_api import SessionUIMS

UID = "YOUR UID"
Password = "YOUR PASSWORD"
# replace these with your credentials
my_account = SessionUIMS(UID, Password)

# `my_acc.attendance` returns attendance info for available subjects in JSON format
subjects = my_account.attendance

# display attendance for each subject
for subject in subjects:
    subject_attendance = "{} - {}%".format(subject["Title"], subject["TotalPercentage"])
    print(subject_attendance)