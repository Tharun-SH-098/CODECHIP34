from tkinter import*
class MyWindow:
            def __init__(self,win):
                        self.lbl1=Label(win,text='Enter Number')
                        self.lbl2=Label(win,text='Result')
                        self.t1=Entry(bd=3)
                        self.t2=Entry()
                        self.btn1=Button(win,text='Find Factorial')
                        self.lbl1.place(x=100,y=50)
                        self.t1.place(x=200,y=50)
                        self.b1=Button(win,text='Find Factorial1',command=self.add)
                        self.b1.place(x=200,y=100)
                        self.lbl2.place(x=150,y=150)
                        self.t2.place(x=200,y=150)

            def add(self):
                        fact=1
                        self.t2.delete(0,'end')
                        num1=int(self.t1.get())
                        for i in range(2,num1+1):
                                       fact=fact*i
                        self.t2.insert(END,str(fact))

window=Tk()
mywin=MyWindow(window)
window.title('Factorial Program')
window.geometry("400x300+10+10")
window.mainloop()
                        
    
