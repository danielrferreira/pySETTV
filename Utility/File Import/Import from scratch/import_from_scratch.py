def import_file(input_file,header,delimiter=','):
  #This function transform a txt file to a dictionary, given a header, a file and a delimiter(optional)  
  with open(input_file,'r') as clash:
        #gets the first line to check how many commas
        temp=clash.readline() 
        #creates a list with the same number of columns as squential elements
        n_col=1
        for c in temp: 
            if c==',':
                n_col+=1
        clash.seek(0)
        i=1
        l=[0]
        while i<n_col:
            l.append(i)
            i+=1
        result={1:1}
        for g in l:
            result[header[g]]=[]
        n_rows=len(clash.readlines())
        
        #Comeback the pointer to the begining of the file 
        clash.seek(0)
        #Line loop
        count_row=1
        for row in clash.readlines():
            #Collumn gathering
            pos,start,end,count_var=0,0,0,0
            for k in row: 
                if k==delimiter:
                    end=pos
                    result[header[count_var]].append(row[start:end])
                    start=pos+1 
                    count_var+=1
                    if count_var==n_col-1:
                        if count_row==n_rows:
                            result[header[count_var]].append(row[start:len(row)])
                        else: 
                            result[header[count_var]].append(row[start:len(row)-1])      
                pos+=1
            count_row+=1
    result.pop(1)
    return result

#%%
#Function call example
header = ('artist','album','country','region','year_artist','label','year_album')                    
input_file='input2.txt'
db = import_file(input_file,header) 

#%%
def retrieve(i):
    print(db['album'][i],'by',db['artist'][i],'. Year of Release:', db['year_album'][i])

#%%
retrieve(38)     
