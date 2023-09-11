import calendar

def exibir_calendario(ano, mes):
    cal = calendar.monthcalendar(ano, mes)
    
    print(calendar.month_name[mes], ano)
    print("Seg Ter Qua Qui Sex Sáb Dom")
    
    for semana in cal:
        for dia in semana:
            if dia == 0:
                print("    ", end="")
            else:
                print(f"{dia:2d} ", end="")
        print()
    print()

ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))

exibir_calendario(ano, mes)