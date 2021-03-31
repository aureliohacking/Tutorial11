from tkinter import *
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import socket,sys,threading,time

def scanPort(target,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c = s.connect_ex((target,port))
	if c ==0:
		#print(' '+ ip + '  puerto %d \t (abierto) ' % (port,))
		resultado = ' Port %d \t[Abierto]' % (port,)
		listbox.insert("end", str(resultado))
		scrolledtext1.insert("end", str(resultado))
		time.sleep(0.5)

	s.close()

def Iniciar():
	global ip, target
	ip = (texto.get())
	target = socket.gethostbyname(ip)
	for i in range(1,1026):
		try:
			scan = threading.Thread(target=scanPort, args=(target, i))
			scan.setDaemon(True)
			scan.start()
		except: time.sleep(0.01)



def limpiar():
	listbox.delete(0, END)
	scrolledtext1.delete("1.0","end")


def Guardar():
	nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
	if nombrearch!='':
		archi1=open(nombrearch, "w", encoding="utf-8")
		archi1.write(scrolledtext1.get("1.0", END))
		archi1.close()
		mb.showinfo("Simple scanner", "El archivos se han guardado satisfactoriamente")


root = Tk()
root.title("Simple scanner de puerto")
root.geometry("500x500")
root['bg'] = '#0059b3'
root.resizable(0,0) 

#label1
etiqueta=Label(root,text='Digite la ip')
etiqueta.place(x=20,y=20)


#caja de texto1
texto = Entry(root, text="localhost")
texto.place(x=100,y=10,width = 140, height = 50)
texto.insert(0, "localhost")
texto.config(font=("Consolas",12),)



#label2
etiqueta2=Label(root,text='Resultado')
etiqueta2.place(x=20,y=80)

#caja de texto2
frame = Frame(root)
frame.place(x = 100, y = 80, width = 370, height = 115)
listbox = Listbox(frame, width = 59, height = 6)
listbox.place(x = 0, y = 0)
listbox.bind('<<ListboxSelect>>')
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.config(font=("Consolas",12))


#scorll
frame = Frame(root)
frame.place(x = 500, y = 80, width = 320, height =215)
scrolledtext1=st.ScrolledText(frame, x = 200, y = 200, width = 0, height = 0)
scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
scrolledtext1.config(font=("Consolas",12))

#boton 1
boton=Button(root,text='Iniciar',command=Iniciar, width=10, height=2, anchor="center")
boton.place(x=20,y=350)


#boton 2
boton=Button(root,text='Guardar',command=Guardar, width=10, height=2, anchor="center")
boton.place(x=120,y=350)

boton=Button(root,text='Limpiar',command=limpiar, width=10, height=2, anchor="center")
boton.place(x=220,y=350)

root.mainloop()