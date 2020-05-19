#tic tac toe - peli terminaaliin. Testattu macOS Catalina. Pitäisi toimia myös linuxissa.
import os

#Globaalit muuttujat
game_board = [['-','-','-'],['-','-','-'],['-','-','-']]

#Pelin funktiot


def kysy_siirtoa():    #Funktio joka ottaa pelaajan siirron vastaan
    siirto_rivi = 4
    while siirto_rivi not in range(1,4):
        siirto_r = input('Anna rivi mihin sijoitetaan!')
        if siirto_r == 'q' or siirto_r == 'Q':
            quit()
        siirto_r = int(siirto_r)
        if siirto_r not in range(1,4):
            print('Anna rivinumero väliltä 1-3')
        siirto_rivi = int(siirto_r)
    siirto_sarake = 4
    while siirto_sarake not in range(1,4):
        siirto_s = input('Anna sarake mihin sijoitetaan!')
        if siirto_s == 'q' or siirto_s == 'Q':
            quit()
        siirto_s = int(siirto_s)
        if siirto_s not in range(1,4):
            print('Anna rivinumero väliltä 1-3')
        siirto_sarake = int(siirto_s)
    return siirto_rivi, siirto_sarake
    
def sijoita_peliin(siirto_x, siirto_y, vuoro):  #Funktio joka sijoittaa pelilaudalle siirron
    if game_board[siirto_x - 1][siirto_y - 1] == '-':
        game_board[siirto_x - 1][siirto_y - 1] = vuoro
    return

def print_board():  #Funktio joka näyttää pelilaudan
    print(' # ')
    print(' # ' + ' | ' + ' 1 ' + ' | ' + ' 2 ' + ' | ' + ' 3 ' + ' | ')
    print(' 1 ' + ' |  ' + game_board[0][0] + '  |  ' + game_board[0][1] + '  |  ' + game_board[0][2] + '  |  ')
    print(' 2 ' + ' |  ' + game_board[1][0] + '  |  ' + game_board[1][1] + '  |  ' + game_board[1][2] + '  |  ')
    print(' 3 ' + ' |  ' + game_board[2][0] + '  |  ' + game_board[2][1] + '  |  ' + game_board[2][2] + '  |  ')
    print(' # ')
    return

def vaihda_vuoro(vuoro):
    if vuoro == 'X':
        vaihtuu = 'O'
    else:
        vaihtuu = 'X'
    return vaihtuu

def tarkista_tulos(game_board, vuoro):  #Funktio joka tarkistaa onko kolmen suoraa ja voittoa
    kolme_pistetta=0
    voitto = True
    for rivi in game_board: #Silmukka joka tarkistaa kaikki rivit
        for sarake in rivi:
            if sarake == vuoro:
                kolme_pistetta=kolme_pistetta+1
            if kolme_pistetta==3:
                print_board()
                print('Voitto, kiitoksia pelaamisesta.')    
                quit()
        kolme_pistetta=0    
    kolme_pistetta=0
    for rivi in range(0,3): #Silmukka joka tarkistaa kaikki sarakkeet
        for sarake in range(0,3):
            if game_board[rivi][sarake] == vuoro:
                kolme_pistetta = kolme_pistetta+1
            if kolme_pistetta==3:
                print_board()
                print('Voitto, kiitoksia pelaamisesta.')   
                quit()
                voitto = False
        kolme_pistetta=0    
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == vuoro: #Ehto joka tarkistaa vasemmalta ylhäältä alas oikealle vinosti
        print_board()
        print(vuoro + 'voittaa, kiitoksia pelaamisesta.')   
        quit()
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == vuoro: #Ehto joka tarkistaa oikealta ylhäältä alas vasemmalle vinosti
        print_board()
        print(vuoro + 'voittaa, kiitoksia pelaamisesta.')    
        quit()
    return voitto

if __name__ == "__main__":
    os.system('clear')
    print('Aloitetaan pelaamaan!')
    print('Peli tilanne on:')
    game_is_on = True
    vuoro = 'X'
    while game_is_on:
        print_board()
        print('Nyt on vuoro on pelaajan: ' + vuoro + ' pelata.')
        siirto_x, siirto_y = kysy_siirtoa()
        if game_board[siirto_x-1][siirto_y-1] != '-':
            print('Siirto ei onnistu, ruutu on varattu')
            siirto_x, siirto_y = kysy_siirtoa() 
        sijoita_peliin(siirto_x, siirto_y, vuoro)
        game_is_on = tarkista_tulos(game_board, vuoro)
        vuoro = vaihda_vuoro(vuoro)
        os.system('clear')
    pass