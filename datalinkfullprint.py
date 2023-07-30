import random
from numpy.random import choice
import numpy as np

def divisibility(ndata):
    print(ndata)
    data_str=str(ndata)
    print(data_str)
    bit_list=[]
    byte_list=[]
    number_byte=len(data_str)//8
    fcount=0
    lcount=0
#    code_chksm=0
    for index in range(len(data_str)):
        bit_list.append(data_str[index])
        
    lendata=len(data_str)
    remind=lendata%8
    if(remind!=0):
        numberzero=8-remind
        for zro in range(numberzero):
            bit_list.insert(0,'0')


    for bit in bit_list:
        bit_list[lcount]=str(bit_list[lcount])
        lcount+=1
    
    out_data="".join(bit_list)
    print("out data",out_data)    
    return out_data


def checksum_sender(data):
    print(data)
    data_str=str(data)
    print(data_str)
    bit_list=[]
    byte_list=[]
    number_byte=len(data_str)//8
    fcount=0
#    lcount=0
#    code_chksm=0
    for index in range(len(data_str)):
        bit_list.append(data_str[index])
        
    while(number_byte):
        anybyte=[]
#        lcount=fcount+8
        for bit in range(8):
            if(fcount<len(bit_list)):
                anybyte.append(bit_list[fcount])
                fcount+=1
        anybyte.reverse()    
        byte_list.append(anybyte)    
        number_byte-=1
        
    sum_bytes=[0,0,0,0,0,0,0,0]  
    carry=0
    for bite in range(8):
        for index in range(len(byte_list)):
            sum_bytes[bite]+= int(byte_list[index][bite])
        sum_bytes[bite]+=carry
        carry=sum_bytes[bite]//2
        sum_bytes[bite]=sum_bytes[bite]%2
    sum_bytes.reverse()    
    for i in range(8):
        if (sum_bytes[i]==0):
            sum_bytes[i]=1
        else:
            sum_bytes[i]=0
            
#    for j in range(len(byte_list)):
#        byte_list[j].reverse()
#    byte_list.append(sum_bytes)    
#    for i in range(len(byte_list)):
#        byte_list[i]="".join(byte_list[i])
    stchang=0
    for bte in sum_bytes:
         sum_bytes[stchang]=str(sum_bytes[stchang])
         stchang+=1
    EDC="".join(sum_bytes)    
    return EDC

def error_probable(earlydata,edc):
    data_str=str(earlydata)
    print("data_str",data_str)
    bit_list=[]
    byte_list=[]
    list_index=[]
    probability=[]
    number_byte=len(data_str)/8
    fcount=0
    lcount=0
#    code_chksm=0
    for index in range(len(data_str)):
#        print(index)
        bit_list.append(data_str[index])
        list_index.append(index)
    print("bit_list",bit_list)
    noise=random.randrange(len(list_index))
    probability=random.randrange(0,100)
    print("probability",probability)
    if(probability<20):
        print("probability",probability)
        if(bit_list[noise]=='1'):
           bit_list[noise]='0' 
        else:
            bit_list[noise]='1'
    else:
        pass

    print("bit_list2",bit_list)    
    for bit in bit_list:
        bit_list[lcount]=str(bit_list[lcount])
        lcount+=1
    
    bit_list.append(edc)
    out_data="".join(bit_list)
    print("out data",out_data)    
    return out_data



def flagbyte_sender(fdata):
    data_str=str(fdata)
    print("fdata")
    print(fdata)
    bit_list=[]
    byte_list=[]
    number_byte=len(data_str)//8
    fcount=0
#    lcount=0
#    code_chksm=0
    for index in range(len(data_str)):
        bit_list.append(data_str[index])    

    while(number_byte):
        anybyte=[]
#        lcount=fcount+8
        for bit in range(8):
            if(fcount<len(bit_list)):
                anybyte.append(bit_list[fcount])
                fcount+=1    
        byte_list.append(anybyte)    
        number_byte-=1
#    escape_byte=False
    print("byte_list")
    print(byte_list)
    cunter_ones=0 
    cunter_zeros=0
#    esc_cunt=0
#    flag_cunt=0
    index_flaesc=0
    zero=False
    one=False
    list_index=[]
    ESC=['0','0','0','0','0','0','0','0']
    FLAG=['1','1','1','1','1','1','1','1']
    for byte in byte_list:
        if(byte==FLAG):
            cunter_ones=8
        if(byte==ESC):
            cunter_zeros=8

        print("byte",byte)       
        if(cunter_ones==8):
            list_index.append(index_flaesc)
            print("list_index",list_index)
        
        if(cunter_zeros==8):
           list_index.append(index_flaesc) 
           print("list_index",list_index) 
           
        index_flaesc+=1
        cunter_ones=0
        cunter_zeros=0
    count=0 
    print("index_flaesc",index_flaesc)
#    print("list_index",list_index)
    for flaesc in list_index:
        byte_list.insert(flaesc,['0','0','0','0','0','0','0','0'])
        count+=1
        if(count<len(list_index)):
            list_index[count]=list_index[count]+count
            print("list_count",list_index[count])
            
    byte_list.insert(0, FLAG) 
    byte_list.append(FLAG)
    print("byte_listt",byte_list)
    for i in range(len(byte_list)):
        byte_list[i]="".join(byte_list[i]) 
        
    data_out="".join(byte_list)    
    return data_out
    
def flagbyte_reciver(redata):
    print(redata)
    data_str=str(redata)
    print("flag iish",data_str)
    bit_list=[]
    byte_list=[]
    number_byte=len(data_str)//8
    fcount=0
#    lcount=0
#    code_chksm=0
    for index in range(len(data_str)):
        bit_list.append(data_str[index])  
  

    while(number_byte):
        anybyte=[]
#        lcount=fcount+8
        for bit in range(8):
            if(fcount<len(bit_list)):
                anybyte.append(bit_list[fcount])
                fcount+=1    
        byte_list.append(anybyte)    
        number_byte-=1
        
        
    
    start_byte=False
    indx_byte=0
    cunter_ones=0 
    cunter_zeros=0 
    escape_sign=False
    lisindx=[]           
#    del byte_list[0]
#    del byte_list[-1]
    ESC=['0','0','0','0','0','0','0','0']
    FLAG=['1','1','1','1','1','1','1','1']
    if(len(byte_list)%2==1):
        if(byte_list[-1]==ESC and byte_list[-2]==ESC and byte_list[-3]==ESC):
            del byte_list[-1]
            del byte_list[-2]
    print("zombi",byte_list)    
    for byte in byte_list:
        print("hi")
        if(byte==FLAG):
            cunter_ones=8
            
        if(byte==ESC):
            cunter_zeros=8
            print("hehe",cunter_zeros)
         
        print("byteee",byte)
         
        if(cunter_ones==8 and indx_byte==0):
            start_byte=True
            lisindx.append(indx_byte)
            
        elif(cunter_zeros==8 and escape_sign==False ):
            lisindx.append(indx_byte)
            escape_sign=True            
                
        elif(cunter_zeros==8 or cunter_ones==8):
            if(escape_sign==True):
                escape_sign=False
        
        if(cunter_ones==8 and start_byte==True and indx_byte==len(byte_list)-1 ):
            start_byte=False
            del byte_list[-1]
            break
                    
        indx_byte+=1
        cunter_ones=0
        cunter_zeros=0                        
    print("lisindx", lisindx)
    print("indx_byte", indx_byte)
    print("len( byte_list)", len( byte_list)) 
    x=np.array(byte_list)
    print("nekbat",x)
    index_decrease=0
    print(lisindx)

    for i in lisindx:
        byte_list[i] = '!'
        
    for i in range(0, byte_list.count('!')):
        byte_list.remove('!') # remove        

    x=np.array(byte_list)    
    print("nekbat",x)
    for i in range(len(byte_list)):
        byte_list[i]="".join(byte_list[i]) 
        
    data_out="".join(byte_list)  
    print("not flag",data_out)
    return data_out    

def checksum_reciver(rechdata):
    data_str=str(rechdata)
    bit_list=[]
    byte_list=[]
    number_byte=len(data_str)//8
    fcount=0
#    lcount=0
#    code_chksm=0
    for index in range(len(data_str)):
        bit_list.append(data_str[index])
        
    while(number_byte):
        anybyte=[]
#        lcount=fcount+8
        for bit in range(8):
            if(fcount<len(bit_list)):
                anybyte.append(bit_list[fcount])
                fcount+=1
        anybyte.reverse()    
        byte_list.append(anybyte)    
        number_byte-=1   
        
    sum_bytes=[0,0,0,0,0,0,0,0] 
    no_error=[1,1,1,1,1,1,1,1]
    carry=0
    value_error=False
    for bite in range(8):
        for index in range(len(byte_list)):
            sum_bytes[bite]+= int(byte_list[index][bite])
        sum_bytes[bite]+=carry
        carry=sum_bytes[bite]//2
        sum_bytes[bite]=sum_bytes[bite]%2
    sum_bytes.reverse() 
    if (sum_bytes==no_error):
        value_error=False
        
    else:
        value_error=True
    
    print("this data is recive",rechdata)    
    return  value_error   


#lendata=int(input())
    
original_data=input("enter original binery data")
inputdata=divisibility(original_data)
noisedc=error_probable(inputdata,checksum_sender(inputdata))
frame=flagbyte_sender(noisedc)
edc_checker=flagbyte_reciver(frame)
result=checksum_reciver(edc_checker)
if(result==True):
    print("this media is a noisy pipline canal//some error is happen")
    
else:
    print("no error happen in this pipeline canal")
    

