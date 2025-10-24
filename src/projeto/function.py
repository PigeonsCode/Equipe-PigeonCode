def calc_media(lista_de_notas):
   n_elementos = len(lista_de_notas)
   total_notas = sum(float(lista_de_notas))
   media = total_notas/n_elementos
   return media