from turtle import *
def  polígono(lado, num_lados):
    #Desenha um poligono de num_lado.
    color('red', 'purple')
    begin_fill()
    for i in range(num_lados):
        forward(lado)
        left(360/num_lados)
    end_fill()
polígono(130,8)
done()
