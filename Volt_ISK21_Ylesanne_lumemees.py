import pygame                              #mooduli pygame importimine
pygame.init()                              #pygame käivitamine
screen=pygame.display.set_mode([300,300])  #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.Akna mõõt 300x300 px.
pygame.display.set_caption("Lumemees-Viljar Volt")    #aknale nimetuse andmine



pygame.draw.circle(screen, [255, 255, 255], [150,74], 30, 0)  #joonistab ringi ekraanile,värvus valge,xy koordinaadid,raadius30,0 täidab kujundi värviga
pygame.draw.circle(screen, [255, 255, 255], [150,140], 41, 0) #joonistab ringi ekraanile,värvus valge,xy koordinaadid,raadius41,0 täidab kujundi värviga
pygame.draw.circle(screen, [255, 255, 255], [150,226], 50, 0) #joonistab ringi ekraanile,värvus valge,xy koordinaadid,raadius 50,0 täidab kujundi värviga
pygame.draw.circle(screen, [0, 0, 0], [140,70], 5, 0)   #joonistab silmad ekraanile,värvus must, xy koordinaadid,raadius5,0 täidab värviga.
pygame.draw.circle(screen, [0, 0, 0], [162,70], 5, 0)   #joonistab silmad ekraanile,värvus must, xy koordinaadid,raadius5,0 täidab värviga.

pygame.draw.line(screen, [255,0,0], [146,80], [155,80], 3) #nina joone joonistamine,värvus punane,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.line(screen, [255,0,0], [155, 80], [150,95], 3)#nina joone joonistamine,värvus punane,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.line(screen, [255,0,0], [150, 95], [146,80], 3)#nina joone joonistamine,värvus punane,algus ja lõpppunktide koordinaadid, joone paksus
pygame.draw.line(screen, [255,0,0], [150, 93], [150,80], 4)#nina joone joonistamine,värvus punane,algus ja lõpppunktide koordinaadid, joone paksus



pygame.display.flip()                                       #ekraani värskendamine





from sys import exit                      #mooduli importimine, et ekraan ei sulguks
while True:                               #korduslause kui õige
        for event in pygame.event.get():  #event omistab mooduli parameetird
            if event.type == pygame.QUIT: #tingimusel kui võrdne
                pygame.quit()             #lõpetab tegevuse kui, kasutaja aktiveerib
                exit()                    #väljub