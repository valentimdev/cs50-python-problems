from datetime import date
import sys
import inflect


def main():
    minutos=convert_to_minutes(input("Date of Birth: "))
    p = inflect.engine()
    print((p.number_to_words(minutos)).capitalize().replace(" and","")+" minutes")



def convert_to_minutes(birthday):
    try:
        ano_birthday, mes_birthday, dia_birthday = birthday.split("-")
    except:
        print("Invalid date")
        sys.exit(1)
    birthday = date(int(ano_birthday),int(mes_birthday),int(dia_birthday))
    data_hoje=((str(date.today()).split(" ")))[0]
    ano_hoje,mes_hoje,dia_hoje=data_hoje.split("-")
    day = date(int(ano_hoje),int(mes_hoje),int(dia_hoje))
    dias=(str(day-birthday)).split(" ")
    dias_final=int(dias[0])
    minutos_final=dias_final*24*60
    print(minutos_final)
    return minutos_final

if __name__ == '__main__':
    main()
