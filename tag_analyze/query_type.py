file_name = "query.txt"
data = open(file_name, encoding="utf-8")

file_name = "doctor.txt"
data_doctor = open(file_name, encoding="utf-8")

file_name = "hospital.txt"
data_hospital = open(file_name, encoding="utf-8")

doctor_list = list()
hospital_list = list()
query_list = list()
all_data = list()

doctor_file = open("doctor_query.txt","w", encoding="utf-8")
hospital_file = open("hospital_query.txt", "w",encoding="utf-8")
all_file = open("all_query.txt","w", encoding="utf-8")

for i in data_doctor:
    st = i.strip()
    doctor_list.append(st)
#
for i in data_hospital:
    hospital_list.append(i.strip())

for i in data:
    print(i)
    query_str = i.split()[0]
    query_str_pv = i.split()[1]
    query_str_uv = i.split()[2]

    if query_str in doctor_list:
        doctor_file.write(query_str)
        doctor_file.write(",")
        doctor_file.write(query_str_pv)
        doctor_file.write(",")
        doctor_file.write(query_str_uv)
        doctor_file.write(",")
        doctor_file.write("doctor")
        doctor_file.write("\n")


    elif query_str in hospital_list:
        hospital_file.write(query_str)
        hospital_file.write(",")
        hospital_file.write(query_str_pv)
        hospital_file.write(",")
        hospital_file.write(query_str_uv)
        hospital_file.write(",")
        hospital_file.write("hospital")
        hospital_file.write("\n")

    else:
        all_file.write(query_str)
        all_file.write(",")
        all_file.write(query_str_pv)
        all_file.write(",")
        all_file.write(query_str_uv)
        all_file.write(",")
        all_file.write("other")
        all_file.write("\n")
