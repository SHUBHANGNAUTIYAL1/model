import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template, request
import numpy as np
import datetime
import pandas_datareader as web
now=datetime.datetime.now()
List=['WIPRO.NS','RELIANCE.NS','TATAMOTORS.NS','HCLTECH.NS','M&M.NS','KOTAKBANK.NS','BAJAJ-AUTO.NS','NTPC.NS','ITC.NS','INFY.NS']
List1=[]

length=len(List)
for i in range(length):
   List2=[]
   df=web.DataReader(List[i],data_source='yahoo',start='2021-01-01',end=now.strftime("20%y-%m-%d"))
   
   df['MA50']=df['Adj Close'].rolling(50).mean()
   df['MA100']=df['Adj Close'].rolling(100).mean()
   df['MA200']=df['Adj Close'].rolling(200).mean()

   rows=df.shape[0]

   diff=0
   if df.values[rows-2][3]>df.values[rows-1][3] :
      diff=df.values[rows-2][3]-df.values[rows-1][3]
   if  df.values[rows-2][3]<df.values[rows-1][3] : 
      diff=df.values[rows-1][3]-df.values[rows-2][3]
   a=df.values[rows-1][2]-df.values[rows-1][3]
   
   NEW={
      'OPEN':[round(df.values[rows-1][2],2)],
      'CLOSES':[round(df.values[rows-1][3],2)],
      'DIFFERENCE':[round(diff,2)],     
      'MA_50':[round(df.values[rows-1][6],2)],
      'MA_100 ':[round(df.values[rows-1][7],2)],
      'MA_200 ':[round(df.values[rows-1][8],2)],
      'CHANGE':[round(a % diff,2)]
      }
   
   df1=pd.DataFrame(NEW)
   #print(df1)
   
   for j in range(7):
      List2.append(df1.values[0][j])
   List2.append('WIPRO')
   List1.append(List2)   
#print(List1)
List1[0][7]='WIPRO'
List1[1][7]='RELIANCE'
List1[2][7]='TATA' 
List1[3][7]='HCL'
List1[4][7]='MAHINDRA'
List1[5][7]='KOTAK'
List1[6][7]='BAJAJ'
List1[7][7]='NTPC' 
List1[8][7]='ITC'
List1[9][7]='INFOSYS'
#print(df1.shape)

List1=sorted(List1,key=lambda x:int(x[2]))
#print(List1)

na1=List1[0][7]
na2=List1[1][7]
na3=List1[2][7]
na4=List1[3][7]
na5=List1[4][7]
na6=List1[5][7]
na7=List1[6][7]
na8=List1[7][7]
na9=List1[8][7]
na10=List1[9][7]

h2=List1[1][2]
h1=List1[0][2]
h3=List1[2][2]
h4=List1[3][2]
h5=List1[4][2]
h6=List1[5][2]
h7=List1[6][2]
h8=List1[7][2]
h9=List1[8][2]
h10=List1[9][2]


a1=List1[0][3]
a2=List1[1][3]
a3=List1[2][3]
a4=List1[3][3]
a5=List1[4][3]
a6=List1[5][3]
a7=List1[6][3]
a8=List1[7][3]
a9=List1[8][3]
a10=List1[9][3]

b1=List1[0][4]
b2=List1[1][4]
b3=List1[2][4]
b4=List1[3][4]
b5=List1[4][4]
b6=List1[5][4]
b7=List1[6][4]
b8=List1[7][4]
b9=List1[8][4]
b10=List1[9][4]

c1=List1[0][5]
c2=List1[1][5]
c3=List1[2][5]
c4=List1[3][5]
c5=List1[4][5]
c6=List1[5][5]
c7=List1[6][5]
c8=List1[7][5]
c9=List1[8][5]
c10=List1[9][5]


f1=List1[0][0]
f2=List1[1][0]
f3=List1[2][0]
f4=List1[3][0]
f5=List1[4][0]
f6=List1[5][0]
f7=List1[6][0]
f8=List1[7][0]
f9=List1[8][0]
f10=List1[9][0]

g1=List1[0][1]
g2=List1[1][1]
g3=List1[2][1]
g4=List1[3][1]
g5=List1[4][1]
g6=List1[5][1]
g7=List1[6][1]
g8=List1[7][1]
g9=List1[8][1]
g10=List1[9][1]

l1=List1[0][6]
l2=List1[1][6]
l3=List1[2][6]
l4=List1[3][6]
l5=List1[4][6]
l6=List1[5][6]
l7=List1[6][6]
l8=List1[7][6]
l9=List1[8][6]
l10=List1[9][6]




app=Flask(__name__)

@app.route('/')
def web1():
   return render_template("web1.html")
@app.route('/',methods=['POST'])
def web2():
   ma1=0
   m=request.form['name']
  
   if m=="50" :
      ma1=a1
      ma2=a2
      ma3=a3
      ma4=a4
      ma5=a5
      ma6=a6
      ma7=a7
      ma8=a8
      ma9=a9
      ma10=a10
      
   if m=="100" :
      ma1=b1
      ma2=b2 
      ma3=b3
      ma4=b4
      ma5=b5
      ma6=b6
      ma7=b7
      ma8=b8
      ma9=b9
      ma10=b10
   if m=="200" :
      ma1=c1
      ma2=c2 
      ma3=c3 
      ma4=c4 
      ma5=c5 
      ma6=c6 
      ma7=c7 
      ma8=c8
      ma9=c9
      ma10=c10 
       
      
   
   return render_template("web2.html",name1=na1,a1=f1,b1=g1,d1=h1,c1=ma1,e1=m,k1=l1,name2=na2,a2=f2,b2=g2,d2=h2,c2=ma2,e2=m,k2=l2,name3=na3,a3=f3,b3=g3,d3=h3,c3=ma3,e3=m,k3=l3,
                          name4=na4,a4=f4,b4=g4,d4=h4,c4=ma4,k4=l4,name5=na5,a5=f5,b5=g5,d5=h5,c5=ma5,k5=l5,name6=na6,a6=f6,b6=g6,d6=h6,c6=ma6,k6=l6,name7=na7,a7=f7,b7=g7,d7=h7,c7=ma7,k7=l7,
                         name8=na8, a8=f8,b8=g8,d8=h8,c8=ma8,k8=l8,name9=na9,a9=f9,b9=g9,d9=h9,c9=ma9,k9=l9,name10=na10,a10=f10,b10=g10,d10=h10,c10=ma10,k10=l10)

   

if __name__ == '__main__':

   app.run(debug=True,port=5001)

