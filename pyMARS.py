import tkinter as tk
raiz = tk.Tk()

raiz.title("Ventana de pruebas")

#---------frameTitulo de saludo-------------

frameTitulo = tk.Frame(raiz)
frameTitulo.pack()
frameTitulo.config(bg="white")

lableInicio = tk.Label(frameTitulo,text="pyMARS :D")
lableInicio.grid(row=0,column=0,pady=10,padx=10)
lableInicio.config(font=('times',40))

buttonStart = tk.Button(frameTitulo,text="START")
buttonStart.grid(row=0,column=1,pady=10,padx=10)
buttonStart.config(font=('times',40))

#---------frameTitulo de proceso-------------

valorHexa = tk.StringVar()




def funcion():
# ciclo para contruir primer vector 
  funciones=[["add","R",0,32],["addi","I",8],["addiu","I",9],["addu","R",0,33],["and","R",0,36],["andi","I",12],["beq","I",4],["blez","I",6],["bne","I",5],["bgtz","I",7],["div","R",0,26],
                ["divu","R",0,27],["j","J",2],["jal","J",3],["jr","R",0,8],["lb","I",32],["lbu","I",36],["lhu","I",37],["lui","I",15],["lw","I",35],["mfhi","R",0,16],["mthi","R",0,17],
                ["mflo","R",0,18],["mtlo","R",0,19],["mfc0","I",16],["mult","R",0,24],["multu","R",0,25],["nor","R",0,39],["xor","R",0,38],["or","R",0,37],["ori","I",13],["sb","I",40],["sh","I",41],
                ["slt","R",0,42],["slti","I",10],["sltiu","I",11],["sltu","R",0,43],["sll","R",0,0],["srl","R",0,2],["sra","R",0,3],["sub","R",0,34],["subu","R",0,35],["sw","I",43],["add.s","F",0],
                ["add.d","F",0],["sub.s","F",1],["sub.d","F",1],["mul.s","F",2],["mul.d","F",2],["div.s","F",3],["div.d","F",3],["abs.s","F",5],["abs.d","F",5],["neg.s","F",7],["neg.d","F",7],["c.seq.s","F",58],
                ["c.seq.d","F",58],["c.lt.s","F",60],["c.lt.d","F",60],["c.le.s","F",62],["c.le.d","F",62]]
                
  variables=[["$0",0],["$at",1],["$v0",2],["$v1",3],["$a0",4],["$a1",5],["$a2",6],["$a3",7],["$t0",8],["$t1",9],["$t2",10],["$t3",11],["$t4",12],["$t5",13],["$t6",14],["$t7",15],["$s0",16],
            ["$s1",17],["$s2",18],["$s3",19],["$s4",20],["$s5",21],["$s6",22],["$s7",23],["$t8",24],["$t9",25],["$k0",26],["$k1",27],["$gp",28],["$sp",29],["$fp",30],["$ra",31]]
  variables_f= [["$fv0",0],["$fv1",2],["$ft0",4],["$ft1",6],["$ft2",8],["$ft3",10],["$fa0",12],["$fa1",14],["$ft4",16],["$ft5",18],["$fs0",20],["$fs1",22],["$fs2",24],["$fs3",26],["$fs4",28],["$fs5",30]]
  b=[]
  decimal=[]
  for i in range(len(textoAssembly.get('1.0', 'end').split("\n"))-1):
    b.append(textoAssembly.get('1.0', 'end').split("\n")[i])
  for j in range(len(b)):
    matrix=[]
    for z in range(len(b[j].split())):
      matrix.append(b[j].split()[z])
    m=0
    t=0
    for m in range(len(funciones)-1):
      if matrix[0]==funciones[m][0]:
        t=1
        break
    if t==0:
      tk.Label(textoHexa, text="Error en la función de la linea"+str(j+1)).pack()
      
      break
    else:


#--------------------------------------Tipo I-----------------------------------------------
      if funciones[m][1]=="I":
        if len(matrix)!=4:
          if len(matrix)!=3:
           tk.Label(textoHexa, text="El número de argumentos no es adecuado en la linea"+str(j+1)).pack()
          else:
            linea=[funciones[m][2],0,0,0]
            test1=0
            test2=0
            test3=0
            y=0
            k=0
            for y in range(len(variables)):
              if matrix[1]==variables[y][0]:
                test1=1
                linea[2]=variables[y][1]
              if matrix[2].split("(")[1]==variables[y][0]:
                linea[1]=variables[y][1]
                test2=1
              if matrix[2].split("(")[0]==variables[y][0]:
                linea[3]=variables[y][1]
                test3=1
              try:
                if y==len(variables)-1 and test3==0:
                  if type(int(matrix[2].split("(")[0]))== int:
                    linea[3]=int(matrix[2].split("(")[0]) 
                    test3=1
              except (ValueError):
                tk.Label(textoHexa, text="Error en la linea  "+str(j+1)).pack()
               
                k=1
                break
              if test1==1 and test2==1 and test3==1:
                decimal.append(linea)
                break            
            if test1==0 or test2==0 or test3==0:
              if k==0:
                tk.Label(textoHexa, text="Error de sintaxys o escritura en los argumentos en la linea "+str(j+1)).pack()
                
        else:
          linea=[funciones[m][2],0,0,0]
          test1=0
          test2=0
          test3=0
          y=0
          k=0
          for y in range(len(variables)):
            if matrix[1]==variables[y][0]:
              test1=1
              linea[2]=variables[y][1]
            if matrix[2]==variables[y][0]:
              linea[1]=variables[y][1]
              test2=1
            if matrix[3]==variables[y][0]:
              linea[3]=variables[y][1]
              test3=1
            try:
              if y==len(variables)-1 and test3==0:
                if type(int(matrix[3]))== int:
                  linea[3]=int(matrix[3]) 
                  test3=1
            except (ValueError):
              tk.Label(textoHexa, text="Error en la linea  "+str(j+1)).pack()
              
              k=1
              break
            if test1==1 and test2==1 and test3==1:
              decimal.append(linea)
              break            
          if test1==0 or test2==0 or test3==0:
            if k==0:
              tk.Label(textoHexa, text="Error de sintaxys o escritura en los argumentos en la linea "+str(j+1)).pack()


# ------------------------------Tipo F----------------------------------------------------------
      if funciones[m][1]=="F":
        if len(matrix)!=4:
          lableInicio.pack()
          lableInicio.config(frameTitulo, text="El número de argumentos no es adecuado en la linea" + str(j+1)+" no es correcto")
          break
        else:
          linea=[17,0,0,0,0,funciones[m][2]]
          test1=0
          test2=0
          test3=0
          y=0
        
          if matrix[0].find(".s")!=-1:
            linea[1]=16
          if matrix[0].find(".d")!=-1:
            linea[1]=17
          for y in range(len(variables_f)):
            if matrix[1]==variables_f[y][0]:
              test1=1
              linea[4]=variables_f[y][1]
            if matrix[2]==variables_f[y][0]:
              linea[2]=variables_f[y][1]
              test2=1
            if matrix[3]==variables_f[y][0]:
              linea[3]=variables_f[y][1]
              test3=1
                       
            if test1==1 and test2==1 and test3==1:
                decimal.append(linea)
                break            
          if test1==0 or test2==0 or test3==0:
              tk.Label(textoHexa, text="Error de sintaxys o escritura en los argumentos en la linea "+str(j+1)).pack()


        
#--------------------------------------------------------Tipo J-------------------------
      if funciones[m][1]=="J":
        if len(matrix)!=2:
          tk.Label(textoHexa, text="El número de argumentos no es adecuado en la linea "+str(j+1)).pack()
          

        else:
          linea=[funciones[m][2],0]
          test1=0
          y=0
          k=0
          for y in range(len(variables)):
            if matrix[1]==variables[y][0]:
              linea[1]=variables[y][1]
              test1=1
            try:
              if y==len(variables)-1 and test1==0:
                if type(int(matrix[1]))== int:
                  linea[1]=int(matrix[1]) 
                  test1=1
            except (ValueError):
              tk.Label(textoHexa, text="Error en la linea  "+str(j+1)).pack()
              
              k=1
              break
            if test1==1:
              decimal.append(linea)
              break
            print(linea)
          if test1==0:
              print("entre")
              tk.Label(textoHexa, text="Error de sintaxys o escritura en los argumentos en la linea"+str(j+1)).pack() 
              
               



# ------------------------------------------Tipo R--------------------------------------------
      
      if funciones[m][1]=="R":
        if len(matrix)!=4:
          tk.Label(textoHexa, text="existe un error en la funcion de la linea "+str(j+1)).pack()

          break
        else:
          linea=[0,0,0,0,0,funciones[m][3]]
          test1=0
          test2=0
          test3=0
          y=0
          k=0
          for y in range(len(variables)):
            if matrix[1]==variables[y][0]:
              test1=1
              linea[3]=variables[y][1]
            if matrix[2]==variables[y][0]:
              if matrix[0]=="sll" or matrix[0]=="srl" or matrix[0]=="sra":
                linea[2]=variables[y][1]
                test2=1
              else:  
                linea[1]=variables[y][1]
                test2=1
            if matrix[3]==variables[y][0]:
              if matrix[0]=="sll" or matrix[0]=="srl" or matrix[0]=="sra":
                linea[1]=variables[y][1]
                test3=1
              else:
                linea[2]=variables[y][1]
                test3=1
            try:
              if matrix[0]=="sll" or matrix[0]=="srl" or matrix[0]=="sra":
                if type(int(matrix[3]))== int:
                  linea[4]=int(matrix[3]) 
                  test3=1
            except (ValueError):
              tk.Label(textoHexa, text="Error en la linea "+str(j+1)).pack()
              k=1
              break
           
            if test1==1 and test2==1 and test3==1:
                decimal.append(linea)
                break            
          if test1==0 or test2==0 or test3==0:
            if k==0:
              tk.Label(textoHexa, text="Error de sintaxys o escritura en los argumentos en la linea"+str(j+1)).pack()
          
              

  
# ------------------------- Transformar en hexadecimal-------------------------------------
  
  hexadecimal1=[]
  for ind in range(len(decimal)):
    bin_num=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ind1=0
    if len(decimal[ind])==6:
      for ind1 in range(len(decimal[ind])):
        num=decimal[ind][ind1]
        h=0
        while num>=1:
          if ind1==0:
            bin_num[5-h]=num%2
            num=num//2
          if ind1==1:
            bin_num[10-h]=num%2
            num=num//2
          if ind1==2:
            bin_num[15-h]=num%2
            num=num//2
          if ind1==3:
            bin_num[20-h]=num%2
            num=num//2
          if ind1==4:
            bin_num[25-h]=num%2
            num=num//2
          if ind1==5:
            bin_num[31-h]=num%2
            num=num//2
          h=h+1
      
      hexadecimal1.append(hex(int(str(bin_num[0])+str(bin_num[1])+str(bin_num[2])+str(bin_num[3])+str(bin_num[4])+str(bin_num[5])+str(bin_num[6])+str(bin_num[7])+str(bin_num[8])+
      str(bin_num[9])+str(bin_num[10])+str(bin_num[11])+str(bin_num[12])+str(bin_num[13])+str(bin_num[14])+str(bin_num[15])+str(bin_num[16])+str(bin_num[17])+str(bin_num[18])+
      str(bin_num[19])+str(bin_num[20])+str(bin_num[21])+str(bin_num[22])+str(bin_num[23])+str(bin_num[24])+str(bin_num[25])+str(bin_num[26])+str(bin_num[27])+str(bin_num[28])+
      str(bin_num[29])+str(bin_num[30])+str(bin_num[31]),2)))
        
    if len(decimal[ind])==4:
      for ind1 in range(len(decimal[ind])):
        num=decimal[ind][ind1]
        h=0
        while num>=1:
          if ind1==0:
            bin_num[5-h]=num%2
            num=num//2
          if ind1==1:
            bin_num[10-h]=num%2
            num=num//2
          if ind1==2:
            bin_num[15-h]=num%2
            num=num//2
          if ind1==3:
            bin_num[31-h]=num%2
            num=num//2
          h=h+1
            
        while num<0:
          tran=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
          tran1=[]
          x=-num
          while x>=1:
            if x%2==0:
              tran1.append(1)
              x=x//2
            else:
              tran1.append(0)
              x=x//2
          
          
          complemento=[]
          acarreo=0
          for p in range(len(tran1)):
            if p==0:
              if tran1[p]==1:
                complemento.append(0)
                acarreo=1
              else:
                complemento.append(1)
                acarreo=0
            else:
              if tran1[p]==1 and acarreo==0:
                complemento.append(1)
                acarreo=0
              if tran1[p]==1 and acarreo==1:
                complemento.append(0)
                acarreo=1
              if tran1[p]==0 and acarreo==0:
                complemento.append(0)
                acarreo=0
              if tran1[p]==0 and acarreo==1:
                complemento.append(1)
                acarreo=0

          if p==len(tran1)-1 and acarreo==1:
            complemento.append(1)

        
          for n1 in range(len(complemento)):
            tran[15-n1]=complemento[n1]
          for n2 in range(len(tran)):
            bin_num[31-n2]=tran[15-n2]
          
          num=0

      hexadecimal1.append(hex(int(str(bin_num[0])+str(bin_num[1])+str(bin_num[2])+str(bin_num[3])+str(bin_num[4])+str(bin_num[5])+str(bin_num[6])+str(bin_num[7])+str(bin_num[8])+
      str(bin_num[9])+str(bin_num[10])+str(bin_num[11])+str(bin_num[12])+str(bin_num[13])+str(bin_num[14])+str(bin_num[15])+str(bin_num[16])+str(bin_num[17])+str(bin_num[18])+
      str(bin_num[19])+str(bin_num[20])+str(bin_num[21])+str(bin_num[22])+str(bin_num[23])+str(bin_num[24])+str(bin_num[25])+str(bin_num[26])+str(bin_num[27])+str(bin_num[28])+
      str(bin_num[29])+str(bin_num[30])+str(bin_num[31]),2)))
      
    if len(decimal[ind])==2:
      for ind1 in range(len(decimal[ind])):
        num=decimal[ind][ind1]
        h=0
        while num>=1:
          if ind1==0:
            bin_num[5-h]=num%2
            num=num//2
          if ind1==1:
            bin_num[31-h]=num%2
            num=num//2
          h=h+1
      hexadecimal1.append(hex(int(str(bin_num[0])+str(bin_num[1])+str(bin_num[2])+str(bin_num[3])+str(bin_num[4])+str(bin_num[5])+str(bin_num[6])+str(bin_num[7])+str(bin_num[8])+
      str(bin_num[9])+str(bin_num[10])+str(bin_num[11])+str(bin_num[12])+str(bin_num[13])+str(bin_num[14])+str(bin_num[15])+str(bin_num[16])+str(bin_num[17])+str(bin_num[18])+
      str(bin_num[19])+str(bin_num[20])+str(bin_num[21])+str(bin_num[22])+str(bin_num[23])+str(bin_num[24])+str(bin_num[25])+str(bin_num[26])+str(bin_num[27])+str(bin_num[28])+
      str(bin_num[29])+str(bin_num[30])+str(bin_num[31]),2)))
  
  

  
  
  valorHexa.set(hexadecimal1)
  print(valorHexa)

  #---------Pantalla de texto-------------



frameTexto = tk.Frame()
frameTexto.pack()
frameTexto.config(bg="gray")


buttonStart = tk.Button(frameTitulo,text="START",command=funcion)
buttonStart.grid(row=0,column=1,pady=10,padx=10)
buttonStart.config(font=('times',40))


textoAssembly = tk.Text(frameTexto,height=10)
textoAssembly.grid(row=0,column=0,pady=10,padx=10)


textoHexa = tk.Label(frameTexto,height=10,width=80,textvariable=valorHexa)
textoHexa.grid(row=1,column=0,pady=10,padx=10)

raiz.mainloop()