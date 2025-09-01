from random import randint
import tkinter

main_window = tkinter.Tk()
tkinter.mainloop()


anoAtual = 2023
mesAtual = 0
diaAtual = 0
diaSemAtual = 0



while mesAtual < 12:
    mesAtual += 1
    print ("MÊS ATUAL É ", mesAtual)
    while diaAtual < 31:
        diaAtual += 1
        print ("dia atual é ", diaAtual)
    if diaAtual == 31:
        diaAtual = 0
    if mesAtual == 12:
        anoAtual += 1
        print ("ano corrente",anoAtual)
    kaliYugaInicioAno = 3102
    kaliYugaInicioMes = 1
    kaliYugaInicioDia = 23
    anoKaliYuga = 0


    if mesAtual > kaliYugaInicioMes:
        anoKaliYuga = kaliYuhaInicioAno + anoAtual
        print(anoKaliYuga)
    elif mesAtual == kaliYugaInicioMes:
        if diaAtual >= kaliYugaInicioDia:
            anoKaliYuga = kaliYuhaInicioAno + anoAtual
            print(anoKaliYuga)
        else:
            anoKaliYuga = kaliYuhaInicioAno + anoAtual - 1
            print(anoKaliYuga)

    diaSemAtual = randint(0,6) #atribuição para teste

    #VERIFICAÇÃO DO DIA DA SEMANA

    if diaSemAtual == 0:
        print("Somavāsara (Segunda-Feira)")
        print("Astro: Lua")
        print("Deus: Shiva")
        print("Cor: Branco")
    elif diaSemAtual == 1:
        print("maṅgalavāsara (Terça-Feira)")
        print("Astro: Marte")
        print("Deus: Hanuman")
        print("Cor: Laranja")
    elif diaSemAtual == 2:
        print("budhavāsara (Quarta-Feira)")
        print("Astro: Mercúrio")
        print("Deus: Ganesha")
        print("Cor: Verde")
    elif diaSemAtual == 3:
        print("guruvāsara (Quinta-Feira)")
        print("Astro: Jupiter")
        print("Deus: Bhihaspati")
        print("Cor: Amarelo")
    elif diaSemAtual == 4:
        print("śukravāsara (Sexta-Feira)")
        print("Astro: Vênus")
        print("Deus: Mahalakshmi")
        print("Cor: Branco")
    elif diaSemAtual == 5:
        print("śanivāsara (Sábado)")
        print("Astro: Saturno")
        print("Deus: Shani Dev")
        print("Cor: Preto")
    else:
        print("ravivāsara (Domingo)")
        print("Astro: Sol")
        print("Deus: Surya")
        print("Cor: Vermelho")


    #VERIFICAÇÃO DO MÊS 

    if mesAtual == 3:
        print("Mês no calendário Gregoriano: Março")
        if diaAtual >= 21:
            print("Mês no calendário Hindu: Chaitra")
        else:
            print("Mês no calendário Hindu: Phãlguna")
        if diaAtual >= 13:
            print("O Sol está no signo Védico de Meena ")
        else:
            print("O Sol está no signo Védico de Khumbha ")

    elif mesAtual == 4:
        print("Mês no calendário Gregoriano: Abril")
        if diaAtual >= 21:
            print("Mês no calendário Hindu: vaishākha")
        else:
            print("Mês no calendário Hindu: Chaitra")
        
        if diaAtual >= 14:
            print("O Sol está no signo Védico de Mesha ")
        else:
            print("O Sol está no signo Védico de Meena")
    elif mesAtual == 5:
        print("Mês no calendário Gregoriano: Maio")
        if diaAtual >= 22:
            print("Mês no calendário Hindu: jyaishtha")
        else:
            print("Mês no calendário Hindu: vaishākha")
        
        if diaAtual >= 15:
            print("O Sol está no signo Védico de Vrishabha ")
        else:
            print("O Sol está no signo Védico de Mesha")

    elif mesAtual == 6:
        print("Mês no calendário Gregoriano: Junho")
        if diaAtual >= 22:
            print("Mês no calendário Hindu: āshādha")
        else:
            print("Mês no calendário Hindu: jyaishtha")
        if diaAtual >= 14:
            print("O Sol está no signo Védico de Mithuna ")
        else:
            print("O Sol está no signo Védico de Vrishabha ")

    elif mesAtual == 7:
        print("Mês no calendário Gregoriano: Julho")
        if diaAtual >= 23:
            print("Mês no calendário Hindu: shrāvana")
        else:
            print("Mês no calendário Hindu: āshādha")
        if diaAtual >= 15:
            print("O Sol está no signo Védico de Karkataka ")
        else:
            print("O Sol está no signo Védico de Mithuna ")

    elif mesAtual == 8:
        print("Mês no calendário Gregoriano: Agosto")
        if diaAtual >= 23:
            print("Mês no calendário Hindu: bhādrapada")
        else:
            print("Mês no calendário Hindu: shrāvana")
        if diaAtual >= 16:
            print("O Sol está no signo Védico de Shimha ")
        else:
            print("O Sol está no signo Védico de Karkataka ")

    elif mesAtual == 9:
        print("Mês no calendário Gregoriano: Setembro")
        if diaAtual >= 23:
            print("Mês no calendário Hindu: āshwin")
        else:
            print("Mês no calendário Hindu: bhādrapada")
        if diaAtual >= 16:
            print("O Sol está no signo Védico de Kanya ")
        else:
            print("O Sol está no signo Védico de Shimha ")

    elif mesAtual == 10:
        print("Mês no calendário Gregoriano: Outubro")
        if diaAtual >= 23:
            print("Mês no calendário Hindu: kārtika")
        else:
            print("Mês no calendário Hindu: āshwin")
        if diaAtual >= 16:
            print("O Sol está no signo Védico de Thula ")
        else:
            print("O Sol está no signo Védico de Kanya ")

    elif mesAtual == 11:
        print("Mês no calendário Gregoriano: Novembro")
        if diaAtual >= 22:
            print("Mês no calendário Hindu: agrahayana")
        else:
            print("Mês no calendário Hindu: kārtika")
        if diaAtual >= 15:
            print("O Sol está no signo Védico de Vrishkha ")
        else:
            print("O Sol está no signo Védico de Thula ")

    elif mesAtual == 12:
        print("Mês no calendário Gregoriano: Dezembro")
        if diaAtual >= 22:
            print("Mês no calendário Hindu: pausha")
        else:
            print("Mês no calendário Hindu: agrahayana")
        if diaAtual >= 15:
            print("O Sol está no signo Védico de Dhanus ")
        else:
            print("O Sol está no signo Védico de Vrishkha ")

    elif mesAtual == 1:
        print("Mês no calendário Gregoriano: Janeiro")
        if diaAtual >= 21:
            print("Mês no calendário Hindu: māgha")
        else:
            print("Mês no calendário Hindu: pausha")
        if diaAtual >= 15:
            print("O Sol está no signo Védico de Makara ")
        else:
            print("O Sol está no signo Védico de Dhanus ")

    else:
        print("Mês no calendário Gregoriano: Fevereiro")
        if diaAtual >= 20:
            print("Mês no calendário Hindu: phālguna")
        else:
            print("Mês no calendário Hindu: māgha")
        if diaAtual >= 13:
            print("O Sol está no signo Védico de Khumbha ")
        else:
            print("O Sol está no signo Védico de Makara ") 