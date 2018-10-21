from tkinter import *

global count
global i
i = 0
k = 0
global started1
started1 = 0
count =0
started = False
class App():
    
    def reset(self):
        global started1
        if started1 == 0:
            global started
            global i
            i=0
            started = False
            global count
            count=1
            self.bt1["text"] = "Start"
            self.t.set('00:00:00')
            for u in range(12):
                self.ar[u]["text"] = ""
        else:
            self.stop()
            
        
    def start(self):
        global started
        global count
        global started1
        global i
        global k
        global h,m,s
        if started is False:
            count=0
            self.start_timer()
            started1 = 1
            started = True
            self.bt1["text"] = "Lap"
            self.bt3["text"] = "Stop" 
        else:
            
            self.ar[i]["text"] = str(k+1)+')  '+str(h)+' : '+str(m)+' : '+str(s)
            i+=1
            k= int(k)
            k+=1
             
            if i == 12:
                i=0
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global started
        global started1
        started = False
        self.bt3["text"] = "Reset"
        global count
        count=1
        self.bt1["text"] = "Start"
        started1 = 0
    
    
        
        
    def timer(self):
        global count
        global h,m,s
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.root.after(900,self.start_timer)
            
        
    def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")
        self.root.resizable(False,False)
        self.t = StringVar()
        self.t.set("00:00:00")
        '''self.spa1 = Label(self.root, width = 10, bg = "white")
        self.spa1.grid(row = 0,column = 0, columnspan = 2)
        self.lb = Label(self.root,textvariable=self.t, width = 10, justify = "center")
        self.lb.config(font=("Courier 40 bold "))                
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Courier 12 bold"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Courier 12 bold"))
        self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Courier 12 bold"))
        self.lb.grid(row = 1, column = 0, columnspan = 2)
        self.bt1.grid(row = 3,column =0)
        self.bt2.grid(row =3,column =1)
        self.bt3.grid(row = 3, column =2)
        '''
        


        self.lb0 = Label(self.root, width = 60, height =2)
        self.lb0.grid(row = 0, column = 0, columnspan = 3)

        self.lb = Label(self.root, textvariable = self.t)
        self.lb.grid(row = 1, column = 0, columnspan = 3)
        self.lb.config(font=("Courier 60 bold "))  


        self.lb1 = Label(self.root, width = 60, height =2)
        self.lb1.grid(row = 2, column = 0, columnspan = 3)

        self.bt1 = Button(self.root, text = "Start",command = self.start, bd =3, )
        self.bt1.grid(row = 3, column =0)
        self.bt1.config(font=("Courier 20 bold "))  


        

        '''self.bt2 = Button(self.root, text = "Stop",command = self.stop, bd =3, width = 15, height = 2)
        self.bt2.grid(row = 3, column = 1)'''

        self.bt3 = Button(self.root, text = "Reset",command = self.reset, bd =3)
        self.bt3.grid(row = 3, column = 2)
        self.bt3.config(font=("Courier 20 bold "))  

        self.lb2 = Label(self.root, width = 60, height =2)
        self.lb2.grid(row = 4, column = 0, columnspan = 3)

        self.laplb = Label(self.root, height = 2, width = 30)
        self.laplb.grid(row = 5, column = 0)
        self.laplb1 = Label(self.root, height = 2, width = 30)
        self.laplb1.grid(row = 6, column = 0)
        self.laplb2 = Label(self.root, height = 2, width = 30)
        self.laplb2.grid(row = 7, column = 0)
        self.laplb3 = Label(self.root, height = 2, width = 30)
        self.laplb3.grid(row = 8, column = 0)
        self.laplb4 = Label(self.root, height = 2, width = 30)
        self.laplb4.grid(row = 9, column = 0)
        self.laplb5 = Label(self.root, height = 2, width = 30)
        self.laplb5.grid(row = 10, column = 0)
        
        self.laplb6 = Label(self.root, height = 2, width = 30)
        self.laplb6.grid(row = 5, column = 2)
        self.laplb7 = Label(self.root, height = 2, width = 30)
        self.laplb7.grid(row = 6, column = 2)
        self.laplb8 = Label(self.root, height = 2, width = 30)
        self.laplb8.grid(row = 7, column = 2)
        self.laplb9 = Label(self.root, height = 2, width = 30)
        self.laplb9.grid(row = 8, column = 2)
        self.laplb10 = Label(self.root, height = 2, width = 30)
        self.laplb10.grid(row = 9, column = 2)
        self.laplb11 = Label(self.root, height = 2, width = 30)
        self.laplb11.grid(row = 10, column = 2)

        self.lb3 = Label(self.root, width = 60, height =2)
        self.lb3.grid(row = 11, column = 0, columnspan = 3)

        self.ar = [self.laplb,self.laplb1,self.laplb2,self.laplb3,self.laplb4,self.laplb5,self.laplb6,self.laplb7,self.laplb8,self.laplb9,self.laplb10,self.laplb11]
        
    


create = App()
