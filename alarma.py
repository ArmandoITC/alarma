import time
import winsound
class alarma:
     def __init__(self,freq,dur):
           self.dur=dur
           self.freq=freq
           
     def fallo(self):
           
           
           
           reintento=0
           while reintento==0:
             clave=("01234")
             contraseña=input("dame la contraseña)")
             if contraseña==clave:
                  print("bienvenido")
                  reintento=1
             else:
               
                print("error")
                freq=self.freq
              
                dur=self.dur
                
                s=0
                while(s!=4):
                 
                 winsound.Beep(freq, dur)
                 time.sleep(0.15)
                 winsound.Beep(freq, dur)
                 time.sleep(0.15)
                 s=s+1
                reintento=0      
                



O1=alarma(2500,900)
O1.fallo()
 


