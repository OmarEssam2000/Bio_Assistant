from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from PIL import ImageTk , Image
from tkinter import messagebox
from tkinter import scrolledtext
import sqlite3
from tkinter import filedialog
#from PIL import Image , ImageTk
#===================
#create a database or connect to one
def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

root = Tk()
make_menu(root)
db = sqlite3.connect("app.db")
root.geometry('500x500')
root.title('Bio Assistant')
root.configure(bg='#45748C')

present = Label(root, text='Bio Assistant' , bg='#45748C' , fg='#FFF' ,
 font=('Calibri' , '35'), bd=5 , relief="groove", 
 justify='center' , width='25').pack(pady='40' , ipadx='5', ipady='5')

re_present = Label(root, text="An assistant program for a bioinformaticians in basic operations \n on DNA and RNA sequences" , bg='#FFF' , fg='#45748C' ,
 font=('Calibri' , '25'), bd=5 , relief="sunken", 
 justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
frame_buttons = LabelFrame(root, text='You are ready !', font=('Calibri' , '25') ,bg='#45748C' , fg='#FFF')
frame_buttons.pack(padx=50 , pady=100, ipadx=15 , ipady=15) 

#The function to begin the program !
def Start_window():
     
    # Toplevel object which will
    # be treated as a new window
    start_window = Toplevel(root)
     
    
 
    # sets the title of the
    # Toplevel widget
    start_window.title("Bio Assistant")
 
    # sets the geometry of toplevel
    start_window.geometry("600x600")
     
    start_window.configure(bg='#45748c')
    
    #create note book
    style = ttk.Style(start_window)
    style.configure('lefttab.TNotebook', tabposition='wn')

    notebook = ttk.Notebook(start_window, style='lefttab.TNotebook')
    

    #Complement of DNA experiment
    f1 = Frame(notebook, bg='#b5cef7' , width=1500 , height=1500)
    f1.configure(background='#45748c')
    
    make_menu(f1)
    
    
    l1 = Label(f1, text="Enter DNA sequence" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    e1 = Entry(f1, width=65, font=('Helvetica', 24))
    e1.pack(padx=15)
    e1.insert(0, "Enter DNA sequence !")
    e1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    
    
    def comp():
        seq1 = e1.get()
        seq1 = seq1.upper()
        
        d = { 'A':'T', 'T':'A' , 'C':'G' , 'G':'C'}
        c = ''
        for x in seq1:
            c = c + d[x]
        global output_1
        output_1 = Text(f1, height = 5, width = 25, bg = "light cyan" )
        output_1.pack(pady=15, ipady=5)
        output_1.insert(END , c)
        
        
        
    
    def UploadAction():
        filename = filedialog.askopenfilename() 
        sequences = []
        qualities = []
        with open(filename , 'r') as fo:
             
                # notice that in fastaq we have four lines for each read
                # we only care about the sequence and the qualities score

                fo.readline()  # we don't care about it

                seq = fo.readline().rstrip()  # this is the second line ( the sequence

                fo.readline()  # the third line is of no importance to us in the function

                qual = fo.readline().rstrip()  # the qualities score

                if len(seq) == 0:  # means we reached the end of the file
                   
                    sequences.append(seq)
                    qualities.append(qual)
                d2 = { 'A':'T', 'T':'A' , 'C':'G' , 'G':'C'}
                c2 = ''
                for n in seq:
                    c2 = c2 + d2[n]
                global output_11
                output_11 = Text(f1, height = 5, width = 25, bg = "light cyan")
                output_11.pack(pady=15, ipady=5)
                output_11.insert(END , c2)
                

                
    button_upload1 = Button(f1, text='Open fastq file', font='calibri' , command=UploadAction)
    button_upload1.pack()  
        
        
    Button_f1 = Button(f1, text="Complement your DNA sequence !", font='calibri' , command=comp)
    Button_f1.pack(pady=8)
    def delete_complement():
            output_1.destroy()
    def delete_complement2():        
            output_11.destroy()  
    
    Button_f1delete = Button(f1 , text='Delete result !', font='calibri' ,bg='red', command= delete_complement).pack(pady=5)
    Button_f1delete = Button(f1 , text='Delete result of file uploaded', font='calibri' , bg='red' ,command= delete_complement2).pack(pady=5)

    #DNA to RNA second experiment
    f2 = Frame(notebook, bg='#45748c', width=1200 , height=1200)
    
    l2 = Label(f2, text="Enter DNA sequence" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    make_menu(f2)
    
    e2 = Entry(f2, width=65, font=('Helvetica', 24))
    e2.pack()
    e2.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

    e2.insert(0, "Enter any Dna sequence !")
    def UploadAction():
        filename = filedialog.askopenfilename() 
        sequences = []
        qualities = []
        with open(filename , 'r') as fo:
             
                # notice that in fastaq we have four lines for each read
                # we only care about the sequence and the qualities score

                fo.readline()  # we don't care about it

                seq = fo.readline().rstrip()  # this is the second line ( the sequence

                fo.readline()  # the third line is of no importance to us in the function

                qual = fo.readline().rstrip()  # the qualities score

                if len(seq) == 0:  # means we reached the end of the file
                   
                    sequences.append(seq)
                    qualities.append(qual)
                
                seq = seq.replace('T','U')    
                global output_21
                output_21 = Text(f2, height = 5, width = 25, bg = "light cyan")
                output_21.pack(pady=15, ipady=5)
                output_21.insert(END , seq)
    def myClick():
        hello = e2.get()
        hello1 = hello.upper()
        RNA_seq = hello1.replace('T','U')
        global output2
        output2 = Text(f2, height = 5, width = 25, bg = "light cyan")
        output2.pack(pady=15, ipady=5)
        output2.insert(END , RNA_seq)
        
         
        
    myButton = Button(f2, text="Transcript to RNA !", font='Arial' , command=myClick)
    myButton.pack(padx= 9 , pady=9)
    button_upload2 = Button(f2, text='Open fastq file', font='calibri' , command=UploadAction)
    button_upload2.pack()
    def delete_complement():
            output2.destroy()
    def delete_complement2():        
            output_21.destroy()  
    
    Button_f1delete = Button(f2 , text='Delete result !', font='calibri' ,bg='red', command= delete_complement).pack(pady=5)
    Button_f1delete = Button(f2 , text='Delete result of file uploaded', font='calibri' , bg='red' ,command= delete_complement2).pack(pady=5)
    #==================================================================
    #Start experiment of counting nucleus
    f3 = Frame(notebook, bg='#45748c', width=1200 , height=1200)
    l3 = Label(f3, text="Enter DNA sequence" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    make_menu(f3)
    e3 = Entry(f3, width=65, font=('Helvetica', 24))
    e3.pack()
    e3.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    e3.insert(0, "Enter any Dna sequence !")
    
    
    def countingnuc():
        seq3 = e3.get()
        seq3 = seq3.upper()
        ns = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for n in seq3:
          ns[n] += 1
        global output3  
        output3 = Text(f3, height = 5, width = 25, bg = "light cyan" )
        
        output3.insert(END , ns)
        output3.pack(pady=15, ipady=5)
        
    
    

    
        
   
    def UploadAction():
        filename = filedialog.askopenfilename() 
        sequences = []
        qualities = []
        with open(filename , 'r') as fo:
             
                # notice that in fastaq we have four lines for each read
                # we only care about the sequence and the qualities score

                fo.readline()  # we don't care about it

                seq = fo.readline().rstrip()  # this is the second line ( the sequence

                fo.readline()  # the third line is of no importance to us in the function

                qual = fo.readline().rstrip()  # the qualities score

                if len(seq) == 0:  # means we reached the end of the file
                   
                    sequences.append(seq)
                    qualities.append(qual)
                
                ns = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
                for j in seq:
                    ns[j] += 1
                
                global output_31
                output_31 = Text(f3, height = 5, width = 25, bg = "light cyan")
                output_31.pack(pady=15, ipady=5)
                output_31.insert(END , ns)
    
        
         
        
    myButton = Button(f3, text="Count neocleotides !", font='Arial' , command=countingnuc)
    myButton.pack(padx= 9 , pady=9)
    button_upload3 = Button(f3, text='Open fastq file', font='calibri' , command=UploadAction)
    button_upload3.pack()
    def delete_complement():
            output3.destroy()
    def delete_complement3():        
            output_31.destroy()  
   
    Button_f1delete = Button(f3 , text='Delete result !', font='calibri' ,bg='red', command= delete_complement).pack(pady=5)
    Button_f1delete = Button(f3 , text='Delete result of file uploaded', font='calibri' , bg='red' ,command= delete_complement3).pack(pady=5)
    #======================================================
    f4 = Frame(notebook, bg='#45748c', width=1200 , height=1200)
    l4 = Label(f4, text="Enter RNA sequence" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    make_menu(f4)
    e4 = Entry(f4, width=65, font=('Helvetica', 24))
    e4.pack()
    e4.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    e4.insert(0, "Enter Sequence !")
    
    codons = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G"}
    
    def translating():
        seq4 = e4.get()
        seq4 = seq4.upper()
        amino =''
        
        for j in range(0, len(seq4), 3):
            if codons[seq4[j:j + 3]] != 'Stop':
                amino = amino + codons[seq4[j:j + 3]]
        global output4        
        output4 = Text(f4, height = 5, width = 25, bg = "light cyan")
        output4.pack(pady=15, ipady=5)
        output4.insert(END , 'The opposite protein is '+ amino)      
        
        
    def UploadAction():
        filename = filedialog.askopenfilename() 
        sequences = []
        qualities = []
        with open(filename , 'r') as fo:
             
                # notice that in fastaq we have four lines for each read
                # we only care about the sequence and the qualities score

                fo.readline()  # we don't care about it

                seq = fo.readline().rstrip()  # this is the second line ( the sequence

                fo.readline()  # the third line is of no importance to us in the function

                qual = fo.readline().rstrip()  # the qualities score

                if len(seq) == 0:  # means we reached the end of the file
                   
                    sequences.append(seq)
                    qualities.append(qual)
                
                for j in range(0, len(seq), 3):
                    if codons[seq[j:j + 3]] != 'Stop':
                        amino = amino + codons[seq[j:j + 3]]
                        global output_4
                        output_4 = Text(f4, height = 5, width = 25, bg = "light cyan")
                        output_4.pack(pady=15, ipady=5)
                        output_4.insert(END , 'The opposite protein is '+ amino )    
        
                
                
    
        
   
    Button_f4 = Button(f4, text='Translate to protein !', font='Arial' , command=translating)
    Button_f4.pack(padx= 9 , pady=9)
    button_upload4 = Button(f4, text='Open fastq file', font='calibri' , command=UploadAction)
    button_upload4.pack()
    def delete_complement():
            output4.destroy()
    def delete_complement4():        
            output_4.destroy()  
   
    Button_f1delete = Button(f4 , text='Delete result !', font='calibri' ,bg='red', command= delete_complement).pack(pady=5)
    Button_f1delete = Button(f4 , text='Delete result of file uploaded', font='calibri' , bg='red' ,command= delete_complement4).pack(pady=5)
    #======================================================
    
    f5 = Frame(notebook, bg='#45748c', width=1200 , height=1200)
    l5 = Label(f5, text="Enter any sequence" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    make_menu(f5)
    e5 = Entry(f5, width=65, font=('Helvetica', 24))
    e5.pack()
    e5.insert(0, "Enter Sequence !")
    e5.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    DNA='ACGT'
    RNA='ACGU'
    def validation():
        seq5 = e5.get()
        seq5 = seq5.upper()
        seq5.split()
        valid='This is valid nuclec acid sequence'
        wrong='This is wrong nuclec acid sequence'
        global label_f5
        for n in seq5:
            
            if n not in DNA :
                truth = 'not'
                break
            else :  
                truth = 'valid'
        if truth == 'valid' :  
            global output5      
            output5 = Text(f5,height = 5, width = 25, bg = "light cyan"  )
                    
            output5.pack(ipady=15 , pady=15)
            output5.insert(END , 'The sequence is '+ truth )
             
        else:
            output5 = Text(f5,height = 5, width = 25, bg = "light cyan"  )
                    
            output5.pack(ipady=15 , pady=15)
            output5.insert(END , 'The sequence is wrong ')
        
            
    def UploadAction():
        filename = filedialog.askopenfilename() 
        sequences = []
        qualities = []
        with open(filename , 'r') as fo:
             
                # notice that in fastaq we have four lines for each read
                # we only care about the sequence and the qualities score

                fo.readline()  # we don't care about it

                seq = fo.readline().rstrip()  # this is the second line ( the sequence

                fo.readline()  # the third line is of no importance to us in the function

                qual = fo.readline().rstrip()  # the qualities score

                if len(seq) == 0:  # means we reached the end of the file
                   
                    sequences.append(seq)
                    qualities.append(qual)
                
                
                seq.split()
                
                global output_5
                for n in seq:
                    
                    if n not in DNA :
                        truth = 'not'
                        break
                    else :  
                        truth = 'valid'
                if truth == 'valid' :        
                    output_5 = Text(f5,height = 5, width = 25, bg = "light cyan"  )
                    
                    output_5.pack(ipady=15 , pady=15)
                    output_5.insert(END , 'The DNA sequence is '+ truth )
                    
                else:
                    output_5 = Text(f5,  )
                    
                    output_5.pack(ipady=15 , pady=15)
                    output_5.insert(END , 'The DNA sequence is wrong' )

                
                
    
        
             
                
                   
            
                
        

         
        
                
                
        
        
              
   
    Button_f5 = Button(f5, text='Validate DNA sequence !', font='Arial' , command=validation)
    Button_f5.pack(padx= 9 , pady=9)
    button_upload5 = Button(f5, text='Open fastq file', font='calibri' , command=UploadAction)
    button_upload5.pack()
    
    def delete_complement5():        
            output_5.destroy()  
    def delete_complement():        
            output5.destroy()         
   
    Button_f1delete = Button(f5, text='Delete result !', font='calibri' ,bg='red', command= delete_complement).pack(pady=5)
    Button_f1delete = Button(f5 , text='Delete result of file uploaded', font='calibri' , bg='red' ,command= delete_complement5).pack(pady=5)
    
    #================================================================================#
    #Point mutations counting
    f6 = Frame(notebook, bg='#45748c', width=1200 , height=1200)
    l6 = Label(f6, text="Enter 2 DNA sequences" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    make_menu(f6)
    e6a = Entry(f6, width=65, font=('Helvetica', 24))
    e6a.pack()
    e6a.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    e6a.insert(0, "Enter first sequence !")
    e6b = Entry(f6, width=65, font=('Helvetica', 24))
    e6b.pack(pady=15)
    e6b.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    e6b.insert(0, "Enter second sequence !")

    def pointmutations():  
            first_seq = e6a.get()
            first_seq = first_seq.upper()
            second_seq = e6b.get()
            second_seq = second_seq.upper()
            m = 0 
            if len(first_seq)!=len(second_seq):
                global label_alarm
                label_alarm = Label(f6, text='Sequences are not equal !', font='calibri',bg='#1b70f7', fg='#FFF')
                label_alarm.pack(ipady=15)
             
            for i in range(0,len(first_seq)):
              if first_seq[i]!=second_seq[i]:   
                 m+=1
            global output6     
            output6 = Text(f6,height = 5, width = 25, bg = "light cyan"  ) 
            output6.pack(ipady=15 , pady=15)
            output6.insert(END , 'Muatations are ' + str(m) )
            
    Button_f6 = Button(f6, text='Count mutations !', font='Arial' , command=pointmutations)
    Button_f6.pack(padx= 9 , pady=9)
    
    
    def delete_complement6():        
            output6.destroy()  
            label_alarm.destroy()
           
   
    Button_f1delete = Button(f6, text='Delete result !', font='calibri' ,bg='red', command= delete_complement6).pack(pady=5)
    #=================================================================================================#
    f7 = Frame(notebook, bg='#45748c', width=1200 , height=1200)
    f7.grid(row=0 , column = 5)
    
    l7 = Label(f7, text="Enter 2 DNA sequences" , bg='#f7a00a' , fg='#FFF' ,
    font=('Calibri' , '15'), bd=5 , relief="sunken", 
    justify='center' , width='55').pack(pady='30' , ipadx='15', ipady='5')
    make_menu(f7)
    global e7b
    e7a = Entry(f7, width=65, font=('Helvetica', 24))
    e7a.pack()
    e7a.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    e7a.insert(0, "Enter sequence !")
    
    e7b = Entry(f7, width=65, font=('Helvetica', 24))
    e7b.pack(pady=15)
    e7b.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    e7b.insert(0, "Enter pattern you want to find !")

    def naive():
                text1 = e7a.get()
                global pattern1
                pattern1 = e7b.get()
                 

                # A loop to slide pat[] one by one */
                for i in range(len(text1) - len(pattern1) + 1):
                    j = 0
                    
                    # For current index i, check
                    # for pattern match */
                    while(j < len(pattern1)):
                        if (text1[i + j] != pattern1[j]):
                            break
                        j += 1

                    if (j == len(pattern1)):
                        global output7    
                        output7 = Text(f7,height = 5, width = 25, bg = "light cyan"  ) 
                        output7.pack(ipady=15 , pady=15)
                        output7.insert(END , 'pattern found at index of ' + str(i) )
                    


    Button_f7 = Button(f7, text='Search pattern !', font='Arial' , command=naive)
    Button_f7.pack(padx= 9 , pady=9)
   
    
      
    def delete_complement():        
            output7.destroy()         
   
    Button_f1delete = Button(f7, text='Delete result !', font='calibri' ,bg='red', command= delete_complement).pack(pady=5)

    #=================================================================================================#
    

    notebook.add(f1, text='complement of dna')
    notebook.add(f2, text='dna to rna')
    notebook.add(f3, text='counting nucletides' )
    notebook.add(f4, text='rnatoprotin' )
    notebook.add(f5, text='validatin of sequence' )
    notebook.add(f6, text='pointmutations' )
    notebook.add(f7, text='Find pattern - naive algorithm' )
   

    notebook.grid(row=0, column=0, sticky="nw")
    
    
    
    
    
    


Start_Button = Button(frame_buttons, text='Start !' , font=('Calibri' , '25') ,bg='#f7a00a' , fg='#FFF' , justify='center' , width='8' , relief='ridge' , command=Start_window).pack(padx=50 ,pady=15, ipadx=5 , side='left')
#Data_Button = Button(frame_buttons, text='My Data' , font=('Calibri' , '25') ,bg='#f7a00a' , fg='#FFF' , justify='center' , width='8' , relief='solid' , command=Database_window).pack(padx=50 ,pady=15, ipadx=5 , side='right')







root.mainloop()