def calc_media(lista_de_notas):
   total_notas=0
   n_elementos = len(lista_de_notas)
   
   for i in lista_de_notas:
      total_notas+=float(i)

   media = total_notas/n_elementos
   return round(media, 2)