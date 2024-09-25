meses=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    data=input("Date: ")
    if len(data)<=10:
        mes,dia,ano=data.strip().split("/")
        mes = mes.zfill(2)
        dia = dia.zfill(2)
        if int(mes)>12 or int(dia)>31:
            main()
        else:
            print(f"{ano}-{mes}-{dia}")
    else:
        month,day,year=data.split(" ")
        if not month.isalpha or day[-1] != "," or int(day[:-1]) >= 31:
            main()
        for i in range(len(meses)):
            if meses[i]==month:
                final_month=str(i+1)
        final_month = final_month.zfill(2)
        day = day[:-1].zfill(2)
        print(f"{year}-{final_month}-{day}")

while True:
    try:
        main()
        break
    except EOFError and KeyError and KeyboardInterrupt and ValueError:
        main()
        break