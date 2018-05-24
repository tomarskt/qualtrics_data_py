from variables import *
from add_several_strs import *

def tofloat(string):
    try:
        number=float(string)
        return number
    except ValueError as e:
        return 0



def allocatelist(var,times):  #this just allocates the list
    var=[]
    for k in range(times):
        var.append(' ')
    return var

def get_num_of_schools_row(fullstring):#this figures out how many schools are in a row by scanning until it finds a blank where a school name should be.
    try:
        if fullstring[SCHname[0]] != '':
            num=1
        else:
            num=0
            #separation distance between schools is 230 cells
    except IndexError:
        num=0
        run=0
    sep=23
    run=1
    while run != 0:
        try:
            if (fullstring[(SCHname[0]+run*sep)] !='') or (fullstring[(SCHname[0]+run*sep)] !='Agreed'):
                run=run+1
                num=run
            else:
                run=0
        except IndexError:
            num=1
            run=0
    return num



def generate_cost(fullstring,ODS): # (UNUSED) this tells us the total per student cost, and works for any school in a row
    perSTtotal= fullstring[ODS]+fullstring[ODS+1]+fullstring[ODS+2]+fullstring[ODS+3]
    return perSTtotal


def scrape_data_into_list(fullstring,schnum): #this function scrapes all the data for a given school in a list

    diff=(schnum-1)*23#this line allows this function to work for any school in a row
    var=[]
    line=allocatelist(var,20)
    line[0]=fullstring[ESDname[0]] #one ESD per line so this shouldn't change
    line[1]= fullstring[ESD_NUM_OF_SCHOOLS[0]]
    line[2]=fullstring[(SCHname[0]+diff)] #school name
    line[3]=fullstring[ODS_provider_name[0]+diff] #ods name
    if fullstring[ODSotheroption[0]+diff] == '':
        line[4]=''
    else:
        line[4]=fullstring[ODSotheroption[0]+diff] #ods other option name,
    line[5]=fullstring[per_student_SCH_EST_cost[0]+diff] #school estimated cost per student
    line[6]=fullstring[grade5_attending[0]+diff] # of studens
    line[7]=fullstring[grade6_attending[0]+diff] # of studens
    line[8]=fullstring[program_days_nights[0]+diff] #length of program
    #line[8]=''#fullstring[]#default $$ per student given length in number form for math
    #totalperstudent=tofloat(fullstring[ODS_provider_fees[0]+diff])+tofloat(fullstring[transport[0]+diff])+tofloat(fullstring[personnel_stipends[0]+diff])+tofloat(fullstring[programcosts_no_admin_costs[0]+diff])+tofloat(fullstring[details_text_box[0]+diff])    #money math
    #print(str(totalperstudent))  #testing line
    line[10]=fullstring[SCH_is_money_enough[0]+diff]
    line[11]=fullstring[SCH_if_threshhold_enough_what_is_needed[0]+diff]
    for k in list(range(4)):
        line[12+k]=fullstring[ODS_provider_fees[0]+diff+k] #cost per student estimated using the cost breakdown
    line[9]=addthemup(line[6],line[7],line[12],line[3],line[14],line[15],0)

    line[16]=multiplythethree(line[6],line[7],line[9],line[11],line[2])
    return line
