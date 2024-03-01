from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
root=Tk()
root.title("My UI")
pi=22/7
Label(root, text='Do you want to open Shapes Calculator, Password Generator, Temperature Converter, or MS Office guide?').pack()
#converter Mahma
def convert():
    label_converter=Label(root,text="Temprature Converter: Celcius to Fahrenheit",font=('Arial',10))
    label_converter.pack(padx=10,pady=10)
    def MyCalculateFunction():
        temprature=float(box_temprature.get())
        result=(temprature*1.8)+32.0
        label_result.config(text=result)
    box_temprature=Entry(root)
    box_temprature.pack()
    button_calculate=Button(root,text="Calculate", command=MyCalculateFunction)
    button_calculate.pack()
    label_result = Label(root)
    label_result.pack()
#Guide Mahma and Fatima
def guide():
    Label(root, text='Click any button below', fg='Royal Blue').pack()
    def copy_text():
        Label(root, text="(Ctrl+C)").pack()
    def save_document():
        Label(root, text="(Ctrl+S)").pack()
    def open_document():
        Label(root, text="(Ctrl+O)").pack()
    def create_new_document():
        Label(root, text="(Ctrl+N)").pack()
    def cut_text():
        Label(root, text="(Ctrl+X)").pack()
    def paste_text():
        Label(root, text="(Ctrl+V)").pack()
    def select_all_text():
        Label(root, text="(Ctrl+A)").pack()
    def make_bold():
        Label(root, text="(Ctrl+B)").pack()
    def make_italic():
        Label(root, text="(Ctrl+I)").pack()
    def make_underline():
        Label(root, text="(Ctrl+U)").pack()
    # Create buttons
    copy_button = Button(root, text="Copy", command=copy_text)
    save_button = Button(root, text="Save a Document", command=save_document)
    open_button = Button(root, text="Open a Document", command=open_document)

    create_button = Button(root, text="Create New Document", command=create_new_document)
    cut_button = Button(root, text="Cut", command=cut_text)
    paste_button = Button(root, text="Paste", command=paste_text)
    select_all_button = Button(root, text="Select All", command=select_all_text)
    bold_button = Button(root, text="Bold", command=make_bold)
    italic_button = Button(root, text="Italic", command=make_italic)
    underline_button = Button(root, text="Underline", command=make_underline)
    # Pack buttons
    copy_button.pack()
    save_button.pack()
    open_button.pack()
    create_button.pack()
    cut_button.pack()
    paste_button.pack()
    select_all_button.pack()
    bold_button.pack()
    italic_button.pack()
    underline_button.pack()

#Shapes Calculator Fatima
#Clicking on the area circle button
def shapescalculator():
    def areacir():
        labelrad = Label(root,bg='steel blue', fg='white', text='Enter the radius below')
        labelrad.pack()
        rad = Entry(root)
        rad.pack()
        def cac():
            if len(rad.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                radi=float(rad.get())
                area=pi*radi*radi
                labelca=Label(root, text= area)
                labelca.pack()
        calccir=Button(root,bg='medium aquamarine', fg='white', text='Calculate area', command=cac)
        calccir.pack()
    #clicking on the area square or rectangle button
    def areasqrect():
        labelbr=Label(root,bg='steel blue', fg='white', text='Enter the breadth below').pack()
        br=Entry(root)
        br.pack()
        labelle=Label(root,bg='steel blue', fg='white', text='Enter the length below').pack()
        le=Entry(root)
        le.pack()
        def casqrect():
            if len(br.get())==0:
                Label(root, text='Invalid Entry').pack()
            elif len(le.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                breadth=float(br.get())
                length=float(le.get())
                area=length*breadth
                labelca=Label(root, text= area)
                labelca.pack()
        calccir=Button(root,bg='medium aquamarine', fg='white', text='Calculate area', command=casqrect)
        calccir.pack()
    #clicking on area triangle button
    def areatri():
        labelbr=Label(root,bg='steel blue', fg='white', text='Enter the breadth below').pack()
        br=Entry(root)
        br.pack()
        labelle=Label(root,bg='steel blue', fg='white', text='Enter the length below').pack()
        ln=Entry(root)
        ln.pack()
        def catri():
            if len(br.get())==0:
                Label(root, text='Invalid Entry').pack()
            elif len(ln.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                breadth=float(br.get())
                length=float(ln.get())
                area=0.5*length*breadth
                labelca=Label(root, text= area)
                labelca.pack()
        calccir=Button(root,bg='medium aquamarine', fg='white', text='Calculate area', command=catri)
        calccir.pack()
    # clicking on area trapezium button
    def areatrap():
        pr=Label(root,bg='rosy brown', fg='white', text='You will be asked to give the lengths of the trapezium in different prompt boxes.')
        pr.pack()
        po=Label(root,bg='rosy brown', fg='white', text='First you will be asked for the two parallel lengths respectively and then the heights.')
        po.pack()
        pl=Label(root, bg='steel blue', fg='white', text='Enter the first parallel length')
        pl.pack()
        pl1=Entry(root)
        pl1.pack()
        pl=Label(root, bg='steel blue', fg='white', text='Enter the second parallel length')
        pl.pack()
        pl2=Entry(root)
        pl2.pack()
        ph=Label(root, bg='steel blue', fg='white', text='Enter the perpendicular height').pack()
        ph=Entry(root)
        ph.pack()
        def catrap():
            if len(pl1.get())==0:
                Label(root, text='Invalid Entry').pack()
            elif len(pl2.get())==0:
                Label(root, text='Invalid Entry').pack()
            elif len(ph.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                pl11=float(pl1.get())
                pl22=float(pl2.get())
                ph1=float(ph.get())
                area=0.5*(pl11+pl22)*ph1
                labelca=Label(root, text= area)
                labelca.pack()
        calccir=Button(root, bg='medium aquamarine', fg='white', text='Calculate area', command=catrap)
        calccir.pack()

    #clicking on missing length circle button
    def cirml():
        w=Label(root, bg='rosy brown', fg='white', text='Takes area of circle and finds radius')
        w.pack()
        pr=Label(root, bg='steel blue', fg='white', text='Enter area:')
        pr.pack()
        area=Entry(root)
        area.pack()
        def cab():
            if len(area.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                nrad=(float(area.get()))/pi
                import math
                rad=math.sqrt(nrad)
                areapr=Label(root, text=rad)
                areapr.pack()
        calcarea=Button(root, bg='medium orchid', fg='white', text='Calculate Radius', command=cab)
        calcarea.pack()
    #clicking on missing length triangle button
    def triml():
        w=Label(root, bg='rosy brown', fg='white', text='Takes area and given length of triangle to find missing length')
        w.pack()
        pr=Label(root, bg='steel blue', fg='white', text='Enter area:')
        pr.pack()
        area=Entry(root)
        area.pack()
        prl=Label(root, bg='steel blue', fg='white', text='Enter given length:')
        prl.pack()
        ml=Entry(root)
        ml.pack()
        def cab():
            if len(area.get())==0:
                Label(root, text='Invalid Entry').pack()
            elif len(ml.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                mltri=float(ml.get())
                areatri=float(area.get())
                ln=(areatri*2)/mltri
                mlpr=Label(root, text=ln)
                mlpr.pack()
        calcarea=Button(root, bg='DeepPink2', fg='white', text='Calculate missing length', command=cab)
        calcarea.pack()
    #clicking on missing length rectangle button
    def sqrectml():
        w=Label(root, bg='rosy brown', fg='white', text='Takes area and given length to find missing length')
        w.pack()
        pr=Label(root, bg='steel blue', fg='white', text='Enter area:')
        pr.pack()
        area=Entry(root)
        area.pack()
        le=Label(root, bg='steel blue', fg='white', text='Enter given length:')
        le.pack()
        ele=Entry(root)
        ele.pack()
        def cab():
            if len(area.get())==0:
                Label(root, text='Invalid Entry').pack()
            elif len(ele.get())==0:
                Label(root, text='Invalid Entry').pack()
            else:
                length=float(ele.get())
                tarea=float(area.get())
                mlength=tarea/length
                prlength=Label(root, text=mlength)
                prlength.pack()
        calcarea=Button(root, bg='pale violet red', fg='white', text='Calculate missing length', command=cab)
        calcarea.pack()
    #clicking on missing length trapezium button
    def trapml():
        w=Label(root, bg='sky blue', fg='white', text='Do you want to find the height or a missing parallel length?')
        w.pack()
        def findmpl():
            lab=Label(root, bg='steel blue', fg='white', text='Enter area').pack()
            a=Entry(root)
            a.pack()
            lab1=Label(root, bg='steel blue', fg='white', text='Enter one of the given parallel lengths').pack()
            pl=Entry(root)
            pl.pack()
            lab2=Label(root, bg='steel blue', fg='white', text='Enter height').pack()
            h=Entry(root)
            h.pack()
            def cmpl():
                if len(a.get())==0:
                    Label(root, text='Invalid Entry').pack()
                elif len(pl.get())==0:
                    Label(root, text='Invalid Entry').pack()
                elif len(h.get())==0:
                    Label(root, text='Invalid Entry').pack()
                else:
                    area=float(a.get())
                    plength=float(pl.get())
                    height=float(h.get())
                    parlen=((area*2)/height)-plength
                    printa=Label(root, text=parlen).pack()
            calcarea=Button(root, bg='cornsilk3', fg='black', text='Calculate Missing Parallel length', command=cmpl)
            calcarea.pack()
        def findheight():
            lab=Label(root, bg='steel blue', fg='white', text='Enter area').pack()
            a=Entry(root)
            a.pack()
            lab1=Label(root, bg='steel blue', fg='white', text='Enter first parallel length').pack()
            pl1=Entry(root)
            pl1.pack()
            lab2=Label(root, bg='steel blue', fg='white', text='Enter second parallel length').pack()
            pl2=Entry(root)
            pl2.pack()
            def showheight():
                if len(a.get())==0:
                    Label(root, text='Invalid Entry').pack()
                elif len(pl1.get())==0:
                    Label(root, text='Invalid Entry').pack()
                elif len(pl2.get())==0:
                    Label(root, text='Invalid Entry').pack()
                else:
                    area=float(a.get())
                    l1=float(pl1.get())
                    l2=float(pl2.get())
                    height=(area*2)/(l1+l2)
                    printheight=Label(root, text=height)
                    printheight.pack()
            h=Button(root, bg='cornsilk3', fg='black', text='Calculate Height', command=showheight)
            h.pack()
        missl=Button(root, bg='thistle', fg='black', text="Find missing parallel length", command=findmpl)
        missl.pack()
        fh=Button(root, bg='thistle', fg='black', text='Find height', command=findheight)
        fh.pack()
        


    #shape buttons for area
    acir=Button(root, bg='medium violet red', fg='white', text='Circle Area', command=areacir)
    atri=Button(root, bg='hot pink', fg='white', text='Triangle Area', command=areatri)
    arect=Button(root, bg='hot pink', fg='white', text='Rectangle Area', command=areasqrect)
    asq=Button(root, bg='medium violet red', fg='white', text='Square Area', command=areasqrect)
    atrap=Button(root, bg='medium violet red', fg='white', text='Trapezium Area', command=areatrap)

    #shape buttons for ml
    mlcir=Button(root, bg='cornflower blue', fg='white', text='Circle Missing Length', command=cirml)
    mltri=Button(root, bg='light slate blue', fg='white', text='Triangle Missing Length', command=triml)
    mlrect=Button(root, bg='light slate blue', fg='white', text='Rectangle Missing Length', command=sqrectml)
    mlsq=Button(root, bg='cornflower blue', fg='white', text='Square Missing Length', command=sqrectml)
    mltrap=Button(root, bg='cornflower blue', fg='white', text='Trapezium Missing Length', command=trapml)

    #button commands area/length
    def clicka():
        labelsc=Label(root, text='Choose any of the shapes below').pack()
        acir.pack()
        atri.pack()
        asq.pack()
        arect.pack()
        atrap.pack()
    def clickml():
        labelsc=Label(root, text='Choose any of the shapes below:').pack()
        mlcir.pack()
        mltri.pack()
        mlsq.pack()
        mlrect.pack()
        mltrap.pack()
    # Area or missing length
    label1=Label(root, text='This program can find the area or a missing length of any given shape').pack()
    label2=Label(root, text='Do you want to find the area or a missing length? ').pack()
    buttona=Button(root, bg='dark slate gray', fg='white', text="Area", command=clicka).pack()
    buttonL=Button(root, bg='dark slate gray', fg='white', text='Missing length', command=clickml).pack()
    buttonq=Button(root, bg='dark slate gray', fg='white', text='End', command= root.quit).pack()

#Password generator Abeera
def passgen():
    def generate_password():
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890"
        special_characters = "!@#$%^&*_+"
        
        password = ""
        if upper_check_var.get():
            password += uppercase
        if lower_check_var.get():
            password += lowercase
        if numbers_check_var.get():
            password += numbers
        if special_check_var.get():
            password += special_characters
        if not (upper_check_var.get() or lower_check_var.get() or numbers_check_var.get() or special_check_var.get()):
            messagebox.showerror("Error", "Please select at least one option.")
            return

        # Ensure that the sample size is not greater than the population size
        sample_size = min(9, len(password))

        generated_password = "".join(random.choices(password, k=sample_size))
        password_label.config(text=generated_password)

    def reset_checkboxes():
        upper_check_var.set(0)
        lower_check_var.set(0)
        numbers_check_var.set(0)
        special_check_var.set(0)

    # GUI
    password_window = Toplevel(root)
    password_window.title("Password Generator")

    upper_check_var = IntVar()
    lower_check_var = IntVar()
    numbers_check_var = IntVar()
    special_check_var = IntVar()

    upper_check = Checkbutton(password_window, text="Uppercase", variable=upper_check_var)
    upper_check.pack(anchor=W)
    lower_check = Checkbutton(password_window, text="Lowercase", variable=lower_check_var)
    lower_check.pack(anchor=W)
    numbers_check = Checkbutton(password_window, text="Numbers", variable=numbers_check_var)
    numbers_check.pack(anchor=W)
    special_check = Checkbutton(password_window, text="Special Characters", variable=special_check_var)
    special_check.pack(anchor=W)

    generate_button = Button(password_window, text="Generate Password", command=generate_password)
    generate_button.pack(pady=10)
    password_label = Label(password_window, text="")
    password_label.pack()

    reset_button = Button(password_window, text="Reset", command=reset_checkboxes)
    reset_button.pack(pady=5)


#buttons for choice
Button(root, text='MS Office Guide', command=guide).pack()
Button(root, text='Celsius to Farenheit Converter', command=convert).pack()
Button(root, text='Shapes Calculator', command=shapescalculator).pack()
Button(root, text='Password Generator', command=passgen).pack()
# Start the main event loop
root.mainloop()
