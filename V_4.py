import tkinter as tk 
import random

# global root
def main_window():
    mw = tk.Tk()
    mw.title('Sudoko')
    mw.geometry('433x495+0+0')

    easy = 35
    medium = 50
    hard = 65
    b1 = tk.Button(mw,text='Easy',font = ('arial 20 bold'), height = 3, width = 25, command = lambda: create(easy))
    b1.grid(row=0,column=0)

    b2 = tk.Button(mw,text='Medium',font = ('arial 20 bold'), height = 3, width = 25, command = lambda: create(medium))
    b2.grid(row=1,column=0)

    b3 = tk.Button(mw,text='Hard',font = ('arial 20 bold'), height = 3, width = 25, command = lambda: create(hard))
    b3.grid(row=3,column=0)

    # b4 = tk.Button(mw,text='Exit',font = ('arial 20 bold'), height = 3, width = 25, command = lambda: exit_1())
    # b4.grid(row=4,column=0)


    mw.mainloop()


def create(easy):
    root.update()
    root.deiconify()
    

    def fn_00():
        num = random.choice(numbers)
        # f_00.delete(0,'end')
        f_00.insert(0,num)
        # f_00.config(state="readonly")
        fn_01()

        # f_01
    def fn_01():
        num = random.choice(numbers)
        f_01.delete(0,'end')
        f_01.insert(0,num)
        if(st_01.get() == st_00.get()):
            fn_01()
        else:
            # f_01.delete(0,'end')
            # f_01.insert(0,num)
            fn_02()
        
    def fn_02():
        num = random.choice(numbers)
        f_02.delete(0,'end')
        f_02.insert(0,num)
        if(st_02.get()==st_00.get() or st_02.get()==st_01.get()):
            fn_02()
        else:
            # f_02.delete(0,'end')
            # f_02.insert(0,num)
            fn_03()

    def fn_03():
        num = random.choice(numbers)
        f_03.delete(0,'end')
        f_03.insert(0,num)
        if(st_03.get()==st_00.get() or st_03.get()==st_01.get() or st_03.get()==st_02.get()):
            fn_03()
        else:
            # f_03.delete(0,'end')
            # f_03.insert(0,num)
            fn_04()

    def fn_04():
        num = random.choice(numbers)
        f_04.delete(0,'end')
        f_04.insert(0,num)
        if(st_04.get()==st_00.get() or st_04.get()==st_01.get() or st_04.get()==st_02.get() or st_04.get()==st_03.get()):
            fn_04()
        else:
            # f_04.delete(0,'end')
            # f_04.insert(0,num)
            fn_05()

    def fn_05():
        num = random.choice(numbers)
        f_05.delete(0,'end')
        f_05.insert(0,num)
        if(st_05.get()==st_00.get() or st_05.get()==st_01.get() or st_05.get()==st_02.get() or st_05.get()==st_03.get() or st_05.get()==st_04.get()):
            fn_05()
        else:
            # f_05.delete(0,'end')
            # f_05.insert(0,num)
            fn_06()

    def fn_06():
        num = random.choice(numbers)
        f_06.delete(0,'end')
        f_06.insert(0,num)
        if(st_06.get()==st_00.get() or st_06.get()==st_01.get() or st_06.get()==st_02.get() or st_06.get()==st_03.get() or st_06.get()==st_04.get() or st_06.get()==st_05.get()):
            fn_06()
        else:
            # f_06.delete(0,'end')
            # f_06.insert(0,num)
            fn_07()

    def fn_07():
        num = random.choice(numbers)
        f_07.delete(0,'end')
        f_07.insert(0,num)
        if(st_07.get()==st_00.get() or st_07.get()==st_01.get() or st_07.get()==st_02.get() or st_07.get()==st_03.get() or st_07.get()==st_04.get() or st_07.get()==st_05.get() or st_07.get()==st_06.get()):
            fn_07()
        else:
            # f_07.delete(0,'end')
            # f_07.insert(0,num)
            fn_08()
    
    def fn_08():
        num = random.choice(numbers)
        f_08.delete(0,'end')
        f_08.insert(0,num)
        if(st_08.get()==st_00.get() or st_08.get()==st_01.get() or st_08.get()==st_02.get() or st_08.get()==st_03.get() or st_08.get()==st_04.get() or st_08.get()==st_05.get() or st_08.get()==st_06.get() or st_08.get()==st_07.get()):
            fn_08()
        else:
            # f_08.delete(0,'end')
            # f_08.insert(0,num)
            row_1()
        
    def row_1():
        # Row 1
        # values shift by 3 from row 0
        f_10.insert(0,st_03.get())
        f_11.insert(0,st_04.get())
        f_12.insert(0,st_05.get())

        f_13.insert(0,st_06.get())
        f_14.insert(0,st_07.get())
        f_15.insert(0,st_08.get())

        f_16.insert(0,st_00.get())
        f_17.insert(0,st_01.get())
        f_18.insert(0,st_02.get())


        # Row 2
        # values shift by 3 from row 1
        f_20.insert(0,st_13.get())
        f_21.insert(0,st_14.get())
        f_22.insert(0,st_15.get())

        f_23.insert(0,st_16.get())
        f_24.insert(0,st_17.get())
        f_25.insert(0,st_18.get())

        f_26.insert(0,st_10.get())
        f_27.insert(0,st_11.get())
        f_28.insert(0,st_12.get())


        # Row 3
        # values shift by 1 from row 2
        f_30.insert(0,st_21.get())
        f_31.insert(0,st_22.get())
        f_32.insert(0,st_23.get())

        f_33.insert(0,st_24.get())
        f_34.insert(0,st_25.get())
        f_35.insert(0,st_26.get())

        f_36.insert(0,st_27.get())
        f_37.insert(0,st_28.get())
        f_38.insert(0,st_20.get())


        # Row 4
        # values shift by 3 from row 3
        f_40.insert(0,st_33.get())
        f_41.insert(0,st_34.get())
        f_42.insert(0,st_35.get())

        f_43.insert(0,st_36.get())
        f_44.insert(0,st_37.get())
        f_45.insert(0,st_38.get())

        f_46.insert(0,st_30.get())
        f_47.insert(0,st_31.get())
        f_48.insert(0,st_32.get())


        # Row 5
        # values shift by 3 from row 4
        f_50.insert(0,st_43.get())
        f_51.insert(0,st_44.get())
        f_52.insert(0,st_45.get())

        f_53.insert(0,st_46.get())
        f_54.insert(0,st_47.get())
        f_55.insert(0,st_48.get())

        f_56.insert(0,st_40.get())
        f_57.insert(0,st_41.get())
        f_58.insert(0,st_42.get())


        # Row 6
        # values shift by 1 from row 5
        f_60.insert(0,st_51.get())
        f_61.insert(0,st_52.get())
        f_62.insert(0,st_53.get())

        f_63.insert(0,st_54.get())
        f_64.insert(0,st_55.get())
        f_65.insert(0,st_56.get())

        f_66.insert(0,st_57.get())
        f_67.insert(0,st_58.get())
        f_68.insert(0,st_50.get())


        # Row 7
        # values shift by 3 from row 6
        f_70.insert(0,st_63.get())
        f_71.insert(0,st_64.get())
        f_72.insert(0,st_65.get())

        f_73.insert(0,st_66.get())
        f_74.insert(0,st_67.get())
        f_75.insert(0,st_68.get())

        f_76.insert(0,st_60.get())
        f_77.insert(0,st_61.get())
        f_78.insert(0,st_62.get())


        # Row 8
        # values shift by 3 from row 7
        f_80.insert(0,st_73.get())
        f_81.insert(0,st_74.get())
        f_82.insert(0,st_75.get())

        f_83.insert(0,st_76.get())
        f_84.insert(0,st_77.get())
        f_85.insert(0,st_78.get())

        f_86.insert(0,st_70.get())
        f_87.insert(0,st_71.get())
        f_88.insert(0,st_72.get())

    fn_00()
    blank(easy)


def blank(easy):
    cell = [f_00,f_01,f_02,f_03,f_04,f_05,f_06,f_07,f_08,f_10,f_11,f_12,f_13,f_14,f_15,f_16,f_17,f_18,f_20,f_21,f_22,f_23,f_24,f_25,f_26,f_27,f_28,f_30,f_31,f_32,f_33,f_34,f_35,f_36,f_37,f_38,f_40,f_41,f_42,f_43,f_44,f_45,f_46,f_47,f_48,f_50,f_51,f_52,f_53,f_54,f_55,f_56,f_57,f_58,f_60,f_61,f_62,f_63,f_64,f_65,f_66,f_67,f_68,f_70,f_71,f_72,f_73,f_74,f_75,f_76,f_77,f_78,f_80,f_81,f_82,f_83,f_84,f_85,f_86,f_87,f_88]
    for i in range(easy):
        cell_num = random.choice(cell)
        # print(cell_num)
        cell1.append(cell_num)
        cell_num.delete(0,'end')
    # for i in cell1:
        # print(i)
    unedit(cell1)


def unedit(cell1):
    global cell
    # global cell1
    cell2 = []
    for q in cell1:
        for i in cell:
            if q == i:
                cell.remove(q)
    for x in cell:
        x.config(state="readonly")



def check():
    
    # Frame 0,0
    if(st_00.get()==st_01.get() or st_00.get()==st_02.get() or st_00.get()==st_10.get() or st_00.get()==st_11.get() or st_00.get()==st_12.get() or st_00.get()==st_20.get() or st_00.get()==st_21.get() or st_00.get()==st_22.get() or st_00.get()==st_03.get() or st_00.get()==st_04.get() or st_00.get()==st_05.get() or st_00.get()==st_06.get() or st_00.get()==st_07.get() or st_00.get()==st_08.get() or st_00.get()==st_10.get() or st_00.get()==st_20.get() or st_00.get()==st_30.get() or st_00.get()==st_40.get() or st_00.get()==st_50.get() or st_00.get()==st_60.get() or st_00.get()==st_70.get() or st_00.get()==st_80.get()):
        popupmsg()
        

    elif(st_01.get()==st_02.get() or st_01.get()==st_10.get() or st_01.get()==st_11.get() or st_01.get()==st_12.get() or st_01.get()==st_20.get() or st_01.get()==st_21.get() or st_01.get()==st_22.get() or st_01.get()==st_02.get() or st_01.get()==st_03.get() or st_01.get()==st_04.get() or st_01.get()==st_05.get() or st_01.get()==st_06.get() or st_01.get()==st_07.get() or st_01.get()==st_08.get() or st_01.get()==st_11.get() or st_01.get()==st_21.get() or st_01.get()==st_31.get() or st_01.get()==st_41.get() or st_01.get()==st_51.get() or st_01.get()==st_61.get() or st_01.get()==st_71.get() or st_01.get()==st_81.get()):
        popupmsg()

    elif(st_02.get()==st_10.get() or st_02.get()==st_11.get() or st_02.get()==st_12.get() or st_02.get()==st_20.get() or st_02.get()==st_21.get() or st_02.get()==st_22.get() or st_02.get()==st_03.get or st_02.get()==st_04.get or st_02.get()==st_05.get or st_02.get()==st_06.get or st_02.get()==st_07.get or st_02.get()==st_08.get or st_02.get()==st_12.get or st_02.get()==st_22.get or st_02.get()==st_32.get or st_02.get()==st_42.get or st_02.get()==st_52.get or st_02.get()==st_62.get or st_02.get()==st_72.get or st_02.get()==st_82.get):
        popupmsg()    

    elif(st_10.get()==st_11.get() or st_10.get()==st_12.get() or st_10.get()==st_20.get() or st_10.get()==st_21.get() or st_10.get()==st_22.get() or st_10.get()==st_13.get() or st_10.get()==st_14.get() or st_10.get()==st_15.get() or st_10.get()==st_16.get() or st_10.get()==st_17.get() or st_10.get()==st_18.get() or st_10.get()==st_20.get() or st_10.get()==st_30.get() or st_10.get()==st_40.get() or st_10.get()==st_50.get() or st_10.get()==st_60.get() or st_10.get()==st_70.get() or st_10.get()==st_80.get()):
        popupmsg()

    elif(st_11.get==st_12.get() or st_11.get==st_20.get() or st_11.get==st_21.get() or st_11.get==st_22.get() or st_11.get()==st_13.get() or st_11.get()==st_14.get() or st_11.get()==st_15.get() or st_11.get()==st_16.get() or st_11.get()==st_17.get() or st_11.get()==st_18.get() or st_11.get()==st_21.get() or st_11.get()==st_31.get() or st_11.get()==st_41.get() or st_11.get()==st_51.get() or st_11.get()==st_61.get() or st_11.get()==st_71.get() or st_11.get()==st_81.get()):
        popupmsg()
    
    elif(st_12.get()==st_20.get() or st_12.get()==st_21.get() or st_12.get()==st_22.get() or st_12.get()==st_13.get() or st_12.get()==st_13.get() or st_12.get()==st_14.get() or st_12.get()==st_15.get() or st_12.get()==st_16.get() or st_12.get()==st_17.get() or st_12.get()==st_18.get() or st_12.get()==st_32.get() or st_12.get()==st_42.get() or st_12.get()==st_52.get() or st_12.get()==st_62.get() or st_12.get()==st_72.get() or st_12.get()==st_82.get()):
        popupmsg()

    elif(st_20.get()==st_21.get() or st_20.get()==st_22.get() or st_20.get()==st_23.get() or st_20.get()==st_24.get() or st_20.get()==st_25.get() or st_20.get()==st_26.get() or st_20.get()==st_27.get() or st_20.get()==st_28.get() or st_20.get()==st_30.get() or st_20.get()==st_40.get() or st_20.get()==st_50.get() or st_20.get()==st_60.get() or st_20.get()==st_70.get() or st_20.get()==st_80.get()):
        popupmsg()
    
    elif(st_21.get()==st_22.get() or st_21.get()==st_23.get() or st_21.get()==st_24.get() or st_21.get()==st_25.get() or st_21.get()==st_26.get() or st_21.get()==st_27.get() or st_21.get()==st_28.get() or st_21.get()==st_31.get() or st_21.get()==st_41.get() or st_21.get()==st_51.get() or st_21.get()==st_61.get() or st_21.get()==st_71.get() or st_21.get()==st_81.get()):
        popupmsg()

    elif(st_22.get()==st_23.get() or st_22.get()==st_24.get() or st_22.get()==st_25.get() or st_22.get()==st_26.get() or st_22.get()==st_27.get() or st_22.get()==st_28.get() or st_22.get()==st_32.get() or st_22.get()==st_42.get() or st_22.get()==st_52.get() or st_22.get()==st_62.get() or st_22.get()==st_72.get() or st_22.get()==st_82.get()):
        popupmsg()

    # Frame 0,1
    elif(st_03.get()==st_04.get() or st_03.get()==st_05.get() or st_03.get()==st_13.get() or st_03.get()==st_14.get() or st_03.get()==st_15.get() or st_03.get()==st_23.get() or st_03.get()==st_24.get() or st_03.get()==st_25.get() or st_03.get()==st_06.get() or st_03.get()==st_07.get() or st_03.get()==st_08.get() or st_03.get()==st_33.get() or st_03.get()==st_43.get() or st_03.get()==st_53.get() or st_03.get()==st_63.get() or st_03.get()==st_73.get() or st_03.get()==st_83.get()):
        popupmsg()
    
    elif(st_04.get()==st_05.get() or st_04.get()==st_13.get() or st_04.get()==st_14.get() or st_04.get()==st_15.get() or st_04.get()==st_23.get() or st_04.get()==st_24.get() or st_04.get()==st_25.get() or st_04.get()==st_06.get() or st_04.get()==st_07.get() or st_04.get()==st_08.get() or st_04.get()==st_34.get() or st_04.get()==st_44.get() or st_04.get()==st_54.get() or st_04.get()==st_64.get() or st_04.get()==st_74.get() or st_04.get()==st_84.get()):
        popupmsg()

    elif(st_05.get()==st_13.get() or st_05.get()==st_14.get() or st_05.get()==st_15.get() or st_05.get()==st_23.get() or st_05.get()==st_24.get() or st_05.get()==st_25.get() or st_05.get()==st_06.get() or st_05.get()==st_07.get() or st_05.get()==st_08.get() or st_05.get()==st_35.get() or st_05.get()==st_45.get() or st_05.get()==st_55.get() or st_05.get()==st_65.get() or st_05.get()==st_75.get() or st_05.get()==st_85.get()):
        popupmsg()

    elif(st_13.get()==st_14.get() or st_13.get()==st_15.get() or st_13.get()==st_23.get() or st_13.get()==st_24.get() or st_13.get()==st_25.get() or st_13.get()==st_16.get() or st_13.get()==st_17.get() or st_13.get()==st_18.get() or st_13.get()==st_33.get() or st_13.get()==st_43.get() or st_13.get()==st_53.get() or st_13.get()==st_63.get() or st_13.get()==st_73.get() or st_13.get()==st_83.get()):
        popupmsg()
    
    elif(st_14.get()==st_15.get() or st_14.get()==st_23.get() or st_14.get()==st_24.get() or st_14.get()==st_25.get() or st_14.get()==st_16.get() or st_14.get()==st_17.get() or st_14.get()==st_18.get() or st_14.get()==st_34.get() or st_14.get()==st_44.get() or st_14.get()==st_54.get() or st_14.get()==st_64.get() or st_14.get()==st_74.get() or st_14.get()==st_84.get()):
        popupmsg()
    
    elif(st_15.get==st_23.get() or st_15.get==st_24.get() or st_15.get==st_25.get() or st_15.get()==st_16.get() or st_15.get()==st_17.get() or st_15.get()==st_18.get() or st_15.get()==st_35.get() or st_15.get()==st_45.get() or st_15.get()==st_55.get() or st_15.get()==st_65.get() or st_15.get()==st_75.get() or st_15.get()==st_85.get()):
        popupmsg()
    
    elif(st_23.get()==st_24.get() or st_23.get()==st_25.get() or st_23.get()==st_26.get() or st_23.get()==st_27.get() or st_23.get()==st_28.get() or st_23.get()==st_33.get() or st_23.get()==st_43.get() or st_23.get()==st_53.get() or st_23.get()==st_63.get() or st_23.get()==st_73.get() or st_23.get()==st_83.get()):
        popupmsg()
    
    elif(st_24.get()==st_25.get() or st_24.get()==st_26.get() or st_24.get()==st_27.get() or st_24.get()==st_28.get() or st_24.get()==st_34.get() or st_24.get()==st_44.get() or st_24.get()==st_54.get() or st_24.get()==st_64.get() or st_24.get()==st_74.get() or st_24.get()==st_84.get()):
        popupmsg()

    elif(st_25.get==st_26.get() or st_25.get==st_27.get() or st_25.get==st_28.get() or st_25.get==st_35.get() or st_25.get==st_45.get() or st_25.get==st_55.get() or st_25.get==st_65.get() or st_25.get==st_75.get() or st_25.get==st_85.get()):
        popupmsg()

    # Frame 02
    elif(st_06.get()==st_07.get() or st_06.get()==st_08.get() or st_06.get()==st_16.get() or st_06.get()==st_17.get() or st_06.get()==st_18.get() or st_06.get()==st_26.get() or st_06.get()==st_27.get() or st_06.get()==st_28.get() or st_06.get()==st_36.get() or st_06.get()==st_46.get() or st_06.get()==st_56.get() or st_06.get()==st_66.get() or st_06.get()==st_76.get() or st_06.get()==st_86.get()):
        popupmsg()
    
    elif(st_07.get()==st_08.get() or st_07.get()==st_16.get() or st_07.get()==st_17.get() or st_07.get()==st_18.get() or st_07.get()==st_26.get() or st_07.get()==st_27.get() or st_07.get()==st_28.get()) or st_07.get()==st_37.get() or st_07.get()==st_47.get() or st_07.get()==st_57.get() or st_07.get()==st_67.get() or st_07.get()==st_77.get() or st_07.get()==st_87.get():                                 
        popupmsg()

    elif(st_08.get()==st_16.get() or st_08.get()==st_17.get() or st_08.get()==st_18.get() or st_08.get()==st_26.get() or st_08.get()==st_27.get() or st_08.get()==st_28.get() or st_08.get()==st_38.get() or st_08.get()==st_48.get() or st_08.get()==st_58.get() or st_08.get()==st_68.get() or st_08.get()==st_78.get() or st_08.get()==st_88.get()):
        popupmsg()
    
    elif(st_16.get()==st_17.get() or st_16.get()==st_18.get() or st_16.get()==st_26.get() or st_16.get()==st_27.get() or st_16.get()==st_28.get() or st_16.get()==st_36.get() or st_16.get()==st_46.get() or st_16.get()==st_56.get() or st_16.get()==st_66.get() or st_16.get()==st_76.get() or st_16.get()==st_86.get()):
        popupmsg()

    elif(st_17.get()==st_18.get() or st_17.get()==st_26.get() or st_17.get()==st_27.get() or st_17.get()==st_28.get() or st_17.get()==st_37.get() or st_17.get()==st_47.get() or st_17.get()==st_57.get() or st_17.get()==st_67.get() or st_17.get()==st_77.get() or st_17.get()==st_87.get()):
        popupmsg()
    
    elif(st_18.get()==st_26.get() or st_18.get()==st_27.get() or st_18.get()==st_28.get() or st_18.get()==st_38.get() or st_18.get()==st_48.get() or st_18.get()==st_58.get() or st_18.get()==st_68.get() or st_18.get()==st_78.get() or st_18.get()==st_88.get()):
        popupmsg()

    elif(st_26.get()==st_27.get() or st_26.get()==st_28.get() or st_26.get()==st_36.get() or st_26.get()==st_46.get() or st_26.get()==st_56.get() or st_26.get()==st_66.get() or st_26.get()==st_76.get() or st_26.get()==st_86.get()):
        popupmsg()

    elif(st_27.get()==st_28.get() or st_27.get()==st_37.get() or st_27.get()==st_47.get() or st_27.get()==st_57.get() or st_27.get()==st_67.get() or st_27.get()==st_77.get() or st_27.get()==st_87.get()):
        popupmsg()

    elif(st_28.get()==st_38.get() or st_28.get()==st_48.get() or st_28.get()==st_58.get() or st_28.get()==st_68.get() or st_28.get()==st_78.get() or st_28.get()==st_88.get()):
        popupmsg()

    # Frame 1,0
    elif(st_30.get()==st_31.get() or st_30.get()==st_32.get() or st_30.get()==st_40.get() or st_30.get()==st_41.get() or st_30.get()==st_42.get() or st_30.get()==st_50.get() or st_30.get()==st_51.get() or st_30.get()==st_52.get() or st_30.get()==st_33.get() or st_30.get()==st_34.get() or st_30.get()==st_35.get() or st_30.get()==st_36.get() or st_30.get()==st_37.get() or st_30.get()==st_38.get() or st_30.get()==st_60.get() or st_30.get()==st_70.get() or st_30.get()==st_80.get()):
        popupmsg()
    
    elif(st_31.get()==st_32.get() or st_31.get()==st_40.get() or st_31.get()==st_41.get() or st_31.get()==st_42.get() or st_31.get()==st_50.get() or st_31.get()==st_51.get() or st_31.get()==st_52.get() or st_31.get()==st_33.get() or st_31.get()==st_34.get() or st_31.get()==st_35.get() or st_31.get()==st_36.get() or st_31.get()==st_37.get() or st_31.get()==st_38.get() or st_31.get()==st_61.get() or st_31.get()==st_71.get() or st_31.get()==st_81.get()):
        popupmsg()

    elif(st_32.get()==st_40.get() or st_32.get()==st_41.get() or st_32.get()==st_42.get() or st_32.get()==st_50.get() or st_32.get()==st_51.get() or st_32.get()==st_52.get() or st_32.get()==st_33.get() or st_32.get()==st_34.get() or st_32.get()==st_35.get() or st_32.get()==st_36.get() or st_32.get()==st_37.get() or st_32.get()==st_38.get() or st_32.get()==st_62.get() or st_32.get()==st_72.get() or st_32.get()==st_82.get()):
        popupmsg()
    
    elif(st_40.get()==st_41.get() or st_40.get()==st_42.get() or st_40.get()==st_50.get() or st_40.get()==st_51.get() or st_40.get()==st_52.get() or st_40.get()==st_43.get() or st_40.get()==st_44.get() or st_40.get()==st_45.get() or st_40.get()==st_46.get() or st_40.get()==st_47.get() or st_40.get()==st_48.get() or st_40.get()==st_60.get() or st_40.get()==st_70.get() or st_40.get()==st_80.get()):
        popupmsg()
    
    elif(st_41.get()==st_42.get() or st_41.get()==st_50.get() or st_41.get()==st_51.get() or st_41.get()==st_52.get() or st_41.get()==st_43.get() or st_41.get()==st_44.get() or st_41.get()==st_45.get() or st_41.get()==st_46.get() or st_41.get()==st_47.get() or st_41.get()==st_48.get() or st_41.get()==st_61.get() or st_41.get()==st_71.get() or st_41.get()==st_81.get()):
        popupmsg()

    elif(st_42.get()==st_50.get() or st_42.get()==st_51.get() or st_42.get()==st_52.get() or st_42.get()==st_43.get() or st_42.get()==st_44.get() or st_42.get()==st_45.get() or st_42.get()==st_46.get() or st_42.get()==st_47.get() or st_42.get()==st_48.get() or st_42.get()==st_62.get() or st_42.get()==st_72.get() or st_42.get()==st_82.get()):
        popupmsg()

    elif(st_50.get()==st_51.get() or st_50.get()==st_52.get() or st_50.get()==st_53.get() or st_50.get()==st_54.get() or st_50.get()==st_55.get() or st_50.get()==st_56.get() or st_50.get()==st_57.get() or st_50.get()==st_58.get() or st_50.get()==st_60.get() or st_50.get()==st_70.get() or st_50.get()==st_80.get()):
        popupmsg()

    elif(st_51.get()==st_52.get() or st_51.get()==st_53.get() or st_51.get()==st_54.get() or st_51.get()==st_55.get() or st_51.get()==st_56.get() or st_51.get()==st_57.get() or st_51.get()==st_58.get() or st_51.get()==st_61.get() or st_51.get()==st_71.get() or st_51.get()==st_81.get()):
        popupmsg()
    
    elif(st_52.get()==st_53.get() or st_52.get()==st_54.get() or st_52.get()==st_55.get() or st_52.get()==st_56.get() or st_52.get()==st_57.get() or st_52.get()==st_58.get() or st_52.get()==st_62.get() or st_52.get()==st_72.get() or st_52.get()==st_82.get()):
        popupmsg()
    
    # Frame 1,1
    elif(st_33.get()==st_34.get() or st_33.get()==st_35.get() or st_33.get()==st_43.get() or st_33.get()==st_44.get() or st_33.get()==st_45.get() or st_33.get()==st_53.get() or st_33.get()==st_54.get() or st_33.get()==st_55.get() or st_33.get()==st_36.get() or st_33.get()==st_37.get() or st_33.get()==st_38.get() or st_33.get()==st_63.get() or st_33.get()==st_73.get() or st_33.get()==st_83.get()):
        popupmsg()
    
    elif(st_34.get()==st_35.get() or st_34.get()==st_43.get() or st_34.get()==st_44.get() or st_34.get()==st_45.get() or st_34.get()==st_53.get() or st_34.get()==st_54.get() or st_34.get()==st_55.get() or st_34.get()==st_36.get() or st_34.get()==st_37.get() or st_34.get()==st_38.get() or st_34.get()==st_64.get() or st_34.get()==st_74.get() or st_34.get()==st_84.get()):
        popupmsg()

    elif(st_35.get()==st_43.get() or st_35.get()==st_44.get() or st_35.get()==st_45.get() or st_35.get()==st_53.get() or st_35.get()==st_54.get() or st_35.get()==st_55.get() or st_35.get()==st_36.get() or st_35.get()==st_37.get() or st_35.get()==st_38.get() or st_35.get()==st_65.get() or st_35.get()==st_75.get() or st_35.get()==st_85.get()):
        popupmsg()

    elif(st_43.get()==st_44.get() or st_43.get()==st_45.get() or st_43.get()==st_53.get() or st_43.get()==st_54.get() or st_43.get()==st_55.get() or st_43.get()==st_46.get() or st_43.get()==st_47.get() or st_43.get()==st_48.get() or st_43.get()==st_63.get() or st_43.get()==st_73.get() or st_43.get()==st_83.get()):
        popupmsg()
    
    elif(st_44.get()==st_45.get() or st_44.get()==st_53.get() or st_44.get()==st_54.get() or st_44.get()==st_55.get() or st_44.get()==st_46.get() or st_44.get()==st_47.get() or st_44.get()==st_48.get() or st_44.get()==st_64.get() or st_44.get()==st_74.get() or st_44.get()==st_84.get()):
        popupmsg()
    
    elif(st_45.get==st_53.get() or st_45.get==st_54.get() or st_45.get==st_55.get() or st_45.get()==st_46.get() or st_45.get()==st_47.get() or st_45.get()==st_48.get() or st_45.get()==st_65.get() or st_45.get()==st_75.get() or st_45.get()==st_85.get()):
        popupmsg()
    
    elif(st_53.get()==st_54.get() or st_53.get()==st_55.get() or st_53.get()==st_56.get() or st_53.get()==st_57.get() or st_53.get()==st_58.get() or st_53.get()==st_63.get() or st_53.get()==st_73.get() or st_53.get()==st_83.get()):
        popupmsg()
    
    elif(st_54.get()==st_55.get() or st_54.get()==st_56.get() or st_54.get()==st_57.get() or st_54.get()==st_58.get() or st_54.get()==st_64.get() or st_54.get()==st_74.get() or st_54.get()==st_84.get()):
        popupmsg()

    elif(st_55.get()==st_56.get() or st_55.get()==st_57.get() or st_55.get()==st_58.get() or st_55.get()==st_65.get() or st_55.get()==st_75.get() or st_55.get()==st_85.get()):
        popupmsg()

    # Frame 1,2
    elif(st_36.get()==st_37.get() or st_36.get()==st_38.get() or st_36.get()==st_46.get() or st_36.get()==st_47.get() or st_36.get()==st_48.get() or st_36.get()==st_56.get() or st_36.get()==st_57.get() or st_36.get()==st_58.get() or st_36.get()==st_66.get() or st_36.get()==st_76.get() or st_36.get()==st_86.get()):
        popupmsg()
    
    elif(st_37.get()==st_38.get() or st_37.get()==st_46.get() or st_37.get()==st_47.get() or st_37.get()==st_48.get() or st_37.get()==st_56.get() or st_37.get()==st_57.get() or st_37.get()==st_58.get() or st_37.get()==st_67.get() or st_37.get()==st_77.get() or st_37.get()==st_87.get()):                                 
        popupmsg()

    elif(st_38.get()==st_46.get() or st_38.get()==st_47.get() or st_38.get()==st_48.get() or st_38.get()==st_56.get() or st_38.get()==st_57.get() or st_38.get()==st_58.get() or st_38.get()==st_68.get() or st_38.get()==st_78.get() or st_38.get()==st_88.get()):
        popupmsg()
    
    elif(st_46.get()==st_47.get() or st_46.get()==st_48.get() or st_46.get()==st_56.get() or st_46.get()==st_57.get() or st_46.get()==st_58.get() or st_46.get()==st_66.get() or st_46.get()==st_76.get() or st_46.get()==st_86.get()):
        popupmsg()

    elif(st_47.get()==st_48.get() or st_47.get()==st_56.get() or st_47.get()==st_57.get() or st_47.get()==st_58.get() or st_47.get==st_67.get() or st_47.get==st_77.get() or st_47.get==st_87.get()):
        popupmsg()
    
    elif(st_48.get()==st_56.get() or st_48.get()==st_57.get() or st_48.get()==st_58.get() or st_48.get()==st_68.get() or st_48.get()==st_78.get() or st_48.get()==st_88.get()):
        popupmsg()

    elif(st_56.get()==st_57.get() or st_56.get()==st_58.get() or st_56.get()==st_66.get() or st_56.get()==st_76.get() or st_56.get()==st_86.get()):
        popupmsg()

    elif(st_57.get()==st_58.get() or st_57.get()==st_67.get() or st_57.get()==st_77.get() or st_57.get()==st_87.get()):
        popupmsg()

    elif(st_58.get()==st_68.get() or st_58.get()==st_78.get() or st_58.get()==st_88.get()):
        popupmsg()
    
    # Frame 2,0
    elif(st_60.get()==st_61.get() or st_60.get()==st_62.get() or st_60.get()==st_70.get() or st_60.get()==st_71.get() or st_60.get()==st_72.get() or st_60.get()==st_80.get() or st_60.get()==st_81.get() or st_60.get()==st_82.get() or st_60.get()==st_63.get() or st_60.get()==st_64.get() or st_60.get()==st_65.get() or st_60.get()==st_66.get() or st_60.get()==st_67.get() or st_60.get()==st_68.get()):
        popupmsg()
    
    elif(st_61.get()==st_62.get() or st_61.get()==st_70.get() or st_61.get()==st_71.get() or st_61.get()==st_72.get() or st_61.get()==st_80.get() or st_61.get()==st_81.get() or st_61.get()==st_82.get() or st_61.get()==st_63.get() or st_61.get()==st_64.get() or st_61.get()==st_65.get() or st_61.get()==st_66.get() or st_61.get()==st_67.get() or st_61.get()==st_68.get()):
        popupmsg()

    elif(st_62.get()==st_70.get() or st_62.get()==st_71.get() or st_62.get()==st_72.get() or st_62.get()==st_80.get() or st_62.get()==st_81.get() or st_62.get()==st_82.get() or st_62.get()==st_63.get() or st_62.get()==st_64.get() or st_62.get()==st_65.get() or st_62.get()==st_66.get() or st_62.get()==st_67.get() or st_62.get()==st_68.get()):
        popupmsg()
    
    elif(st_70.get()==st_71.get() or st_70.get()==st_72.get() or st_70.get()==st_80.get() or st_70.get()==st_81.get() or st_70.get()==st_82.get() or st_70.get()==st_73.get() or st_70.get()==st_74.get() or st_70.get()==st_75.get() or st_70.get()==st_76.get() or st_70.get()==st_77.get() or st_70.get()==st_78.get()):
        popupmsg()
    
    elif(st_71.get()==st_72.get() or st_71.get()==st_80.get() or st_71.get()==st_81.get() or st_71.get()==st_82.get() or st_71.get()==st_73.get() or st_71.get()==st_74.get() or st_71.get()==st_75.get() or st_71.get()==st_76.get() or st_71.get()==st_77.get() or st_71.get()==st_78.get()):
        popupmsg()

    elif(st_72.get()==st_80.get() or st_72.get()==st_81.get() or st_72.get()==st_82.get() or st_72.get()==st_73.get() or st_72.get()==st_74.get() or st_72.get()==st_75.get() or st_72.get()==st_76.get() or st_72.get()==st_77.get() or st_72.get()==st_78.get()):
        popupmsg()

    elif(st_80.get()==st_81.get() or st_80.get()==st_82.get() or st_80.get()==st_83.get() or st_80.get()==st_84.get() or st_80.get()==st_85.get() or st_80.get()==st_86.get() or st_80.get()==st_87.get() or st_80.get()==st_88.get()):
        popupmsg()

    elif(st_81.get()==st_82.get() or st_81.get()==st_83.get() or st_81.get()==st_84.get() or st_81.get()==st_85.get() or st_81.get()==st_86.get() or st_81.get()==st_87.get() or st_81.get()==st_88.get()):
        popupmsg()

    elif(st_82.get()==st_83.get() or st_82.get()==st_84.get() or st_82.get()==st_85.get() or st_82.get()==st_86.get() or st_82.get()==st_87.get() or st_82.get()==st_88.get()):
        popupmsg()

    # Frame 2,1
    elif(st_63.get()==st_64.get() or st_63.get()==st_65.get() or st_63.get()==st_73.get() or st_63.get()==st_74.get() or st_63.get()==st_75.get() or st_63.get()==st_83.get() or st_63.get()==st_84.get() or st_63.get()==st_85.get() or st_63.get()==st_66.get() or st_63.get()==st_67.get() or st_63.get()==st_68.get()):
        popupmsg()
    
    elif(st_64.get()==st_65.get() or st_64.get()==st_73.get() or st_64.get()==st_74.get() or st_64.get()==st_75.get() or st_64.get()==st_83.get() or st_64.get()==st_84.get() or st_64.get()==st_85.get() or st_64.get()==st_66.get() or st_64.get()==st_67.get() or st_64.get()==st_68.get()):
        popupmsg()

    elif(st_65.get()==st_73.get() or st_65.get()==st_74.get() or st_65.get()==st_75.get() or st_65.get()==st_83.get() or st_65.get()==st_84.get() or st_65.get()==st_85.get() or st_65.get()==st_66.get() or st_65.get()==st_67.get() or st_65.get()==st_68.get()):
        popupmsg()

    elif(st_73.get()==st_74.get() or st_73.get()==st_75.get() or st_73.get()==st_83.get() or st_73.get()==st_84.get() or st_73.get()==st_85.get() or st_73.get()==st_76.get() or st_73.get()==st_77.get() or st_73.get()==st_78.get()):
        popupmsg()
    
    elif(st_74.get()==st_75.get() or st_74.get()==st_83.get() or st_74.get()==st_84.get() or st_74.get()==st_85.get() or st_74.get()==st_76.get() or st_74.get()==st_77.get() or st_74.get()==st_78.get()):
        popupmsg()
    
    elif(st_75.get==st_83.get() or st_75.get==st_84.get() or st_75.get==st_85.get() or st_75.get()==st_76.get() or st_75.get()==st_77.get() or st_75.get()==st_78.get()):
        popupmsg()
    
    elif(st_83.get()==st_84.get() or st_83.get()==st_85.get() or st_83.get()==st_86.get() or st_83.get()==st_87.get() or st_83.get()==st_88.get()):
        popupmsg()
    
    elif(st_84.get()==st_85.get() or st_84.get()==st_86.get() or st_84.get()==st_87.get() or st_84.get()==st_88.get()):
        popupmsg()

    elif(st_85.get()==st_86.get() or st_85.get()==st_87.get() or st_85.get()==st_88.get()):
        popupmsg()

     # Frame 2,2
    elif(st_66.get()==st_67.get() or st_66.get()==st_68.get() or st_66.get()==st_76.get() or st_66.get()==st_77.get() or st_66.get()==st_78.get() or st_66.get()==st_86.get() or st_66.get()==st_87.get() or st_66.get()==st_88.get()):
        popupmsg()
    
    elif(st_67.get()==st_68.get() or st_67.get()==st_76.get() or st_67.get()==st_77.get() or st_67.get()==st_78.get() or st_67.get()==st_86.get() or st_77.get()==st_87.get() or st_77.get()==st_88.get()):                                 
        popupmsg()

    elif(st_68.get()==st_76.get() or st_68.get()==st_77.get() or st_68.get()==st_78.get() or st_68.get()==st_86.get() or st_68.get()==st_87.get() or st_68.get()==st_88.get()):
        popupmsg()
    
    elif(st_76.get()==st_77.get() or st_76.get()==st_78.get() or st_76.get()==st_86.get() or st_76.get()==st_87.get() or st_76.get()==st_88.get()):
        popupmsg()

    elif(st_77.get()==st_78.get() or st_77.get()==st_86.get() or st_77.get()==st_87.get() or st_77.get()==st_88.get()):
        popupmsg()
    
    elif(st_78.get()==st_86.get() or st_78.get()==st_87.get() or st_78.get()==st_88.get()):
        popupmsg()

    elif(st_86.get()==st_87.get() or st_86.get()==st_88.get()):
        popupmsg()

    elif(st_87.get()==st_88.get()):
        popupmsg()

    else:
        popupmsg_win()


def popupmsg():
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text='You Lose')
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B2 = tk.Button(popup, text="Exit", command = lambda: pop_exit())
    B1.pack()
    B2.pack()
    def pop_exit():
        quit()
    

def popupmsg_win():
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text='You Win')
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B2 = tk.Button(popup, text="Exit", command = lambda : exit())
    B1.pack()
    B2.pack()


def exit_1():
    root.destroy


def re_blank():
    # global cell1
    for i in cell1:
        i.delete(0,'end')


# def gui():

root = tk.Tk()
root.title('Sudoko')
root.geometry('443x550+923+0')
root.withdraw()

numbers = [1,2,3,4,5,6,7,8,9]

# global root

cell1 = []

# Frame 0,0
st_00 = tk.StringVar()
st_01 = tk.StringVar()
st_02 = tk.StringVar()

st_10 = tk.StringVar()
st_11 = tk.StringVar()
st_12 = tk.StringVar()

st_20 = tk.StringVar()
st_21 = tk.StringVar()
st_22 = tk.StringVar()


# Frame 0,1
st_03 = tk.StringVar()
st_04 = tk.StringVar()
st_05 = tk.StringVar()

st_13 = tk.StringVar()
st_14 = tk.StringVar()
st_15 = tk.StringVar()

st_23 = tk.StringVar()
st_24 = tk.StringVar()
st_25 = tk.StringVar()


# Frame 0,2
st_06 = tk.StringVar()
st_07 = tk.StringVar()
st_08 = tk.StringVar()

st_16 = tk.StringVar()
st_17 = tk.StringVar()
st_18 = tk.StringVar()

st_26 = tk.StringVar()
st_27 = tk.StringVar()
st_28 = tk.StringVar()


# Frame 1,0
st_30 = tk.StringVar()
st_31 = tk.StringVar()
st_32 = tk.StringVar()

st_40 = tk.StringVar()
st_41 = tk.StringVar()
st_42 = tk.StringVar()

st_50 = tk.StringVar()
st_51 = tk.StringVar()
st_52 = tk.StringVar()


# Frame 1,1
st_33 = tk.StringVar()
st_34 = tk.StringVar()
st_35 = tk.StringVar()

st_43 = tk.StringVar()
st_44 = tk.StringVar()
st_45 = tk.StringVar()

st_53 = tk.StringVar()
st_54 = tk.StringVar()
st_55 = tk.StringVar()


# Frame 1,2
st_36 = tk.StringVar()
st_37 = tk.StringVar()
st_38 = tk.StringVar()

st_46 = tk.StringVar()
st_47 = tk.StringVar()
st_48 = tk.StringVar()

st_56 = tk.StringVar()
st_57 = tk.StringVar()
st_58 = tk.StringVar()


# Frame 2,0
st_60 = tk.StringVar()
st_61 = tk.StringVar()
st_62 = tk.StringVar()

st_70 = tk.StringVar()
st_71 = tk.StringVar()
st_72 = tk.StringVar()

st_80 = tk.StringVar()
st_81 = tk.StringVar()
st_82 = tk.StringVar()


# Frame 2,1
st_63 = tk.StringVar()
st_64 = tk.StringVar()
st_65 = tk.StringVar()

st_73 = tk.StringVar()
st_74 = tk.StringVar()
st_75 = tk.StringVar()

st_83 = tk.StringVar()
st_84 = tk.StringVar()
st_85 = tk.StringVar()


# Frame 2,2
st_66 = tk.StringVar()
st_67 = tk.StringVar()
st_68 = tk.StringVar()

st_76 = tk.StringVar()
st_77 = tk.StringVar()
st_78 = tk.StringVar()

st_86 = tk.StringVar()
st_87 = tk.StringVar()
st_88 = tk.StringVar()


#GUI
# Frame 0, 0
fr_00 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_00.grid(row = 0, column = 0)

f_00 = tk.Entry(master = fr_00, textvariable = st_00, font = ('arial 30 bold'), width = 2)
f_00.grid(row = 0, column = 0)

f_01 = tk.Entry(master = fr_00, textvariable = st_01, font = ('arial 30 bold'), width = 2)
f_01.grid(row = 0, column = 1)

f_02 = tk.Entry(master = fr_00, textvariable = st_02, font = ('arial 30 bold'), width = 2)
f_02.grid(row = 0, column = 2)

f_10 = tk.Entry(master = fr_00, textvariable = st_10, font = ('arial 30 bold'), width = 2)
f_10.grid(row = 1, column = 0)

f_11 = tk.Entry(master = fr_00, textvariable = st_11, font = ('arial 30 bold'), width = 2)
f_11.grid(row = 1, column = 1)

f_12 = tk.Entry(master = fr_00, textvariable = st_12, font = ('arial 30 bold'), width = 2)
f_12.grid(row = 1, column = 2)

f_20 = tk.Entry(master = fr_00, textvariable = st_20, font = ('arial 30 bold'), width = 2)
f_20.grid(row = 2, column = 0)

f_21 = tk.Entry(master = fr_00, textvariable = st_21, font = ('arial 30 bold'), width = 2)
f_21.grid(row = 2, column = 1)

f_22 = tk.Entry(master = fr_00, textvariable = st_22, font = ('arial 30 bold'), width = 2)
f_22.grid(row = 2, column = 2)


# Frame 0, 1
fr_01 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_01.grid(row = 0, column = 1)

f_03 = tk.Entry(master = fr_01, textvariable = st_03, font = ('arial 30 bold'), width = 2)
f_03.grid(row = 0, column = 3)

f_04 = tk.Entry(master = fr_01, textvariable = st_04, font = ('arial 30 bold'), width = 2)
f_04.grid(row = 0, column = 4)

f_05 = tk.Entry(master = fr_01, textvariable = st_05, font = ('arial 30 bold'), width = 2)
f_05.grid(row = 0, column = 5)

f_13 = tk.Entry(master = fr_01, textvariable = st_13, font = ('arial 30 bold'), width = 2)
f_13.grid(row = 1, column = 3)

f_14 = tk.Entry(master = fr_01, textvariable = st_14, font = ('arial 30 bold'), width = 2)
f_14.grid(row = 1, column = 4)

f_15 = tk.Entry(master = fr_01, textvariable = st_15, font = ('arial 30 bold'), width = 2)
f_15.grid(row = 1, column = 5)

f_23 = tk.Entry(master = fr_01, textvariable = st_23, font = ('arial 30 bold'), width = 2)
f_23.grid(row = 2, column = 3)

f_24 = tk.Entry(master = fr_01, textvariable = st_24, font = ('arial 30 bold'), width = 2)
f_24.grid(row = 2, column = 4)

f_25 = tk.Entry(master = fr_01, textvariable = st_25, font = ('arial 30 bold'), width = 2)
f_25.grid(row = 2, column = 5)


# Frame = 0, 2
fr_02 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_02.grid(row = 0, column = 2)

f_06 = tk.Entry(master = fr_02, textvariable = st_06, font = ('arial 30 bold'), width = 2)
f_06.grid(row = 0, column = 6)

f_07 = tk.Entry(master = fr_02, textvariable = st_07, font = ('arial 30 bold'), width = 2)
f_07.grid(row = 0, column = 7)

f_08 = tk.Entry(master = fr_02, textvariable = st_08, font = ('arial 30 bold'), width = 2)
f_08.grid(row = 0, column = 8)

f_16 = tk.Entry(master = fr_02, textvariable = st_16, font = ('arial 30 bold'), width = 2)
f_16.grid(row = 1, column = 6)

f_17 = tk.Entry(master = fr_02, textvariable = st_17, font = ('arial 30 bold'), width = 2)
f_17.grid(row = 1, column = 7)

f_18 = tk.Entry(master = fr_02, textvariable = st_18, font = ('arial 30 bold'), width = 2)
f_18.grid(row = 1, column = 8)

f_26 = tk.Entry(master = fr_02, textvariable = st_26, font = ('arial 30 bold'), width = 2)
f_26.grid(row = 2, column = 6)

f_27 = tk.Entry(master = fr_02, textvariable = st_27, font = ('arial 30 bold'), width = 2)
f_27.grid(row = 2, column = 7)

f_28 = tk.Entry(master = fr_02, textvariable = st_28, font = ('arial 30 bold'), width = 2)
f_28.grid(row = 2, column = 8)


# Frame 1, 0
fr_10 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_10.grid(row = 1, column = 0)

f_30 = tk.Entry(master = fr_10, textvariable = st_30, font = ('arial 30 bold'), width = 2)
f_30.grid(row = 3, column = 0)

f_31 = tk.Entry(master = fr_10, textvariable = st_31, font = ('arial 30 bold'), width = 2)
f_31.grid(row = 3, column = 1)

f_32 = tk.Entry(master = fr_10, textvariable = st_32, font = ('arial 30 bold'), width = 2)
f_32.grid(row = 3, column = 2)

f_40 = tk.Entry(master = fr_10, textvariable = st_40, font = ('arial 30 bold'), width = 2)
f_40.grid(row = 4, column = 0)

f_41 = tk.Entry(master = fr_10, textvariable = st_41, font = ('arial 30 bold'), width = 2)
f_41.grid(row = 4, column = 1)

f_42 = tk.Entry(master = fr_10, textvariable = st_42, font = ('arial 30 bold'), width = 2)
f_42.grid(row = 4, column = 2)

f_50 = tk.Entry(master = fr_10, textvariable = st_50, font = ('arial 30 bold'), width = 2)
f_50.grid(row = 5, column = 0)

f_51 = tk.Entry(master = fr_10, textvariable = st_51, font = ('arial 30 bold'), width = 2)
f_51.grid(row = 5, column = 1)

f_52 = tk.Entry(master = fr_10, textvariable = st_52, font = ('arial 30 bold'), width = 2)
f_52.grid(row = 5, column = 2)


# Frame 1, 1
fr_11 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_11.grid(row = 1, column = 1)

f_33 = tk.Entry(master = fr_11, textvariable = st_33, font = ('arial 30 bold'), width = 2)
f_33.grid(row = 3, column = 3)

f_34 = tk.Entry(master = fr_11, textvariable = st_34, font = ('arial 30 bold'), width = 2)
f_34.grid(row = 3, column = 4)

f_35 = tk.Entry(master = fr_11, textvariable = st_35, font = ('arial 30 bold'), width = 2)
f_35.grid(row = 3, column = 5)

f_43 = tk.Entry(master = fr_11, textvariable = st_43, font = ('arial 30 bold'), width = 2)
f_43.grid(row = 4, column = 3)

f_44 = tk.Entry(master = fr_11, textvariable = st_44, font = ('arial 30 bold'), width = 2)
f_44.grid(row = 4, column = 4)

f_45 = tk.Entry(master = fr_11, textvariable = st_45, font = ('arial 30 bold'), width = 2)
f_45.grid(row = 4, column = 5)

f_53 = tk.Entry(master = fr_11, textvariable = st_53, font = ('arial 30 bold'), width = 2)
f_53.grid(row = 5, column = 3)

f_54 = tk.Entry(master = fr_11, textvariable = st_54, font = ('arial 30 bold'), width = 2)
f_54.grid(row = 5, column = 4)

f_55 = tk.Entry(master = fr_11, textvariable = st_55, font = ('arial 30 bold'), width = 2)
f_55.grid(row = 5, column = 5)


# Frame 1, 2
fr_12 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_12.grid(row = 1, column = 2)

f_36 = tk.Entry(master = fr_12, textvariable = st_36, font = ('arial 30 bold'), width = 2)
f_36.grid(row = 3, column = 6)

f_37 = tk.Entry(master = fr_12, textvariable = st_37, font = ('arial 30 bold'), width = 2)
f_37.grid(row = 3, column = 7)

f_38 = tk.Entry(master = fr_12, textvariable = st_38, font = ('arial 30 bold'), width = 2)
f_38.grid(row = 3, column = 8)

f_46 = tk.Entry(master = fr_12, textvariable = st_46, font = ('arial 30 bold'), width = 2)
f_46.grid(row = 4, column = 6)

f_47 = tk.Entry(master = fr_12, textvariable = st_47, font = ('arial 30 bold'), width = 2)
f_47.grid(row = 4, column = 7)

f_48 = tk.Entry(master = fr_12, textvariable = st_48, font = ('arial 30 bold'), width = 2)
f_48.grid(row = 4, column = 8)


f_56 = tk.Entry(master = fr_12, textvariable = st_56, font = ('arial 30 bold'), width = 2)
f_56.grid(row = 5, column = 6)

f_57 = tk.Entry(master = fr_12, textvariable = st_57, font = ('arial 30 bold'), width = 2)
f_57.grid(row = 5, column = 7)


f_58 = tk.Entry(master = fr_12, textvariable = st_58, font = ('arial 30 bold'), width = 2)
f_58.grid(row = 5, column = 8)


# Frame 2, 0
fr_20 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_20.grid(row = 2, column = 0)

f_60 = tk.Entry(master = fr_20, textvariable = st_60, font = ('arial 30 bold'), width = 2)
f_60.grid(row = 6, column = 0)

f_61 = tk.Entry(master = fr_20, textvariable = st_61, font = ('arial 30 bold'), width = 2)
f_61.grid(row = 6, column = 1)

f_62 = tk.Entry(master = fr_20, textvariable = st_62, font = ('arial 30 bold'), width = 2)
f_62.grid(row = 6, column = 2)

f_70 = tk.Entry(master = fr_20, textvariable = st_70, font = ('arial 30 bold'), width = 2)
f_70.grid(row = 7, column = 0)

f_71 = tk.Entry(master = fr_20, textvariable = st_71, font = ('arial 30 bold'), width = 2)
f_71.grid(row = 7, column = 1)

f_72 = tk.Entry(master = fr_20, textvariable = st_72, font = ('arial 30 bold'), width = 2)
f_72.grid(row = 7, column = 2)

f_80 = tk.Entry(master = fr_20, textvariable = st_80, font = ('arial 30 bold'), width = 2)
f_80.grid(row = 8, column = 0)

f_81 = tk.Entry(master = fr_20, textvariable = st_81, font = ('arial 30 bold'), width = 2)
f_81.grid(row = 8, column = 1)

f_82 = tk.Entry(master = fr_20, textvariable = st_82, font = ('arial 30 bold'), width = 2)
f_82.grid(row = 8, column = 2)


# Frame 2, 1
fr_21 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_21.grid(row = 2, column = 1)

f_63 = tk.Entry(master = fr_21, textvariable = st_63, font = ('arial 30 bold'), width = 2)
f_63.grid(row = 6, column = 3)


f_64 = tk.Entry(master = fr_21, textvariable = st_64, font = ('arial 30 bold'), width = 2)
f_64.grid(row = 6, column = 4)


f_65 = tk.Entry(master = fr_21, textvariable = st_65, font = ('arial 30 bold'), width = 2)
f_65.grid(row = 6, column = 5)

f_73 = tk.Entry(master = fr_21, textvariable = st_73, font = ('arial 30 bold'), width = 2)
f_73.grid(row = 7, column = 3)

f_74 = tk.Entry(master = fr_21, textvariable = st_74, font = ('arial 30 bold'), width = 2)
f_74.grid(row = 7, column = 4)

f_75 = tk.Entry(master = fr_21, textvariable = st_75, font = ('arial 30 bold'), width = 2)
f_75.grid(row = 7, column = 5)

f_83 = tk.Entry(master = fr_21, textvariable = st_83, font = ('arial 30 bold'), width = 2)
f_83.grid(row = 8, column = 3)

f_84 = tk.Entry(master = fr_21, textvariable = st_84, font = ('arial 30 bold'), width = 2)
f_84.grid(row = 8, column = 4)

f_85 = tk.Entry(master = fr_21, textvariable = st_85, font = ('arial 30 bold'), width = 2)
f_85.grid(row = 8, column = 5)


# Frame 2, 1
fr_22 = tk.Frame(root, height = 250, width = 250, bg = 'Black', bd = 2)
fr_22.grid(row = 2, column = 2)

f_66 = tk.Entry(master = fr_22, textvariable = st_66, font = ('arial 30 bold'), width = 2)
f_66.grid(row = 6, column = 6)

f_67 = tk.Entry(master = fr_22, textvariable = st_67, font = ('arial 30 bold'), width = 2)
f_67.grid(row = 6, column = 7)


f_68 = tk.Entry(master = fr_22, textvariable = st_68, font = ('arial 30 bold'), width = 2)
f_68.grid(row = 6, column = 8)

f_76 = tk.Entry(master = fr_22, textvariable = st_76, font = ('arial 30 bold'), width = 2)
f_76.grid(row = 7, column = 6)


f_77 = tk.Entry(master = fr_22, textvariable = st_77, font = ('arial 30 bold'), width = 2)
f_77.grid(row = 7, column = 7)

f_78 = tk.Entry(master = fr_22, textvariable = st_78, font = ('arial 30 bold'), width = 2)
f_78.grid(row = 7, column = 8)


f_86 = tk.Entry(master = fr_22, textvariable = st_86, font = ('arial 30 bold'), width = 2)
f_86.grid(row = 8, column = 6)


f_87 = tk.Entry(master = fr_22, textvariable = st_87, font = ('arial 30 bold'), width = 2)
f_87.grid(row = 8, column = 7)

f_88 = tk.Entry(master = fr_22, textvariable = st_88, font = ('arial 30 bold'), width = 2)
f_88.grid(row = 8, column = 8)


# Buttons
but_1 = tk.Button(text = 'Submit', font = ('arial 10 bold'), height = 2, width = 54, command = lambda: check())
but_1.grid(row = 9, column = 0, columnspan = 5,padx=0)

but_2 = tk.Button(text = 'Clear', font = ('arial 10 bold'), height = 2, width = 54, command = lambda: re_blank())
but_2.grid(row = 10, column = 0, columnspan = 5,padx=0)


# cell list
cell = [f_00,f_01,f_02,f_03,f_04,f_05,f_06,f_07,f_08,f_10,f_11,f_12,f_13,f_14,f_15,f_16,f_17,f_18,f_20,f_21,f_22,f_23,f_24,f_25,f_26,f_27,f_28,f_30,f_31,f_32,f_33,f_34,f_35,f_36,f_37,f_38,f_40,f_41,f_42,f_43,f_44,f_45,f_46,f_47,f_48,f_50,f_51,f_52,f_53,f_54,f_55,f_56,f_57,f_58,f_60,f_61,f_62,f_63,f_64,f_65,f_66,f_67,f_68,f_70,f_71,f_72,f_73,f_74,f_75,f_76,f_77,f_78,f_80,f_81,f_82,f_83,f_84,f_85,f_86,f_87,f_88]




# create()
# blank()
main_window()

root.mainloop()