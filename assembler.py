import re
import sys



def binary_string(number):                 #converting decimal to binary string
    return bin(number)[2:]   




def decimal_to_binary_twos_complement(decimal_number):
    if decimal_number < 0:
        binary_string = bin(decimal_number & int("1" * (decimal_number.bit_length() + 1), 2))[2:]   #decimal to 2s complement 
    else:
        binary_string = bin(decimal_number)[2:]

    return binary_string



    return result_bin
def fill(binary_string, num_bits,s):
    if len(binary_string) < num_bits:
        binary_string = s * (num_bits - len(binary_string)) + binary_string   #filling
    
    elif len(binary_string) > num_bits:
        binary_string = binary_string[-num_bits:]
    
    return binary_string






    


r_type_instructions = {
    "add": {"opcode": "0110011", "rd": "", "funct3": "000", "rs1": "", "rs2": "", "funct7": "0000000"},
    "sub": {"opcode": "0110011", "rd": "", "funct3": "000", "rs1": "", "rs2": "", "funct7": "0100000"},
    "sll": {"opcode": "0110011", "rd": "", "funct3": "001", "rs1": "", "rs2": "", "funct7": "0000000"},
    "slt": {"opcode": "0110011", "rd": "", "funct3": "010", "rs1": "", "rs2": "", "funct7": "0000000"},
    "sltu": {"opcode": "0110011", "rd": "", "funct3": "011", "rs1": "", "rs2": "", "funct7": "0000000"},
    "xor": {"opcode": "0110011", "rd": "", "funct3": "100", "rs1": "", "rs2": "", "funct7": "0000000"},
    "srl": {"opcode": "0110011", "rd": "", "funct3": "101", "rs1": "", "rs2": "", "funct7": "0000000"},
    "or": {"opcode": "0110011", "rd": "", "funct3": "110", "rs1": "", "rs2": "", "funct7": "0000000"},
    "and": {"opcode": "0110011", "rd": "", "funct3": "111", "rs1": "", "rs2": "", "funct7": "0000000"}
}

i_type_instructions = {
    "lw": {"opcode": "0000011","rd": "", "funct3": "010", "rs1": "",  "imm": ""},
    "addi": {"opcode": "0010011","rd": "", "funct3": "000", "rs1": "",  "imm": ""},
    "sltiu": {"opcode": "0010011","rd": "", "funct3": "011", "rs1": "", "imm": ""},
    "jalr": {"opcode": "1100111","rd": "", "funct3": "000", "rs1": "",  "imm": ""}
}

s_type_instructions = {
    "sw": {"opcode": "0100011","imm":"", "funct3": "010","rs1":"","rs2":""},
}
b_type_instructions = {
    "beq": {"opcode": "1100011", "imm1": "", "funct3": "000", "rs1": "", "rs2": "", "imm2": ""},
    "bne": {"opcode": "1100011", "imm1": "", "funct3": "001", "rs1": "", "rs2": "", "imm2": ""},
    "blt": {"opcode": "1100011", "imm1": "", "funct3": "100", "rs1": "", "rs2": "", "imm2": ""},
    "bge": {"opcode": "1100011", "imm1": "", "funct3": "101", "rs1": "", "rs2": "", "imm2": ""},
    "bltu": {"opcode": "1100011", "imm1": "", "funct3": "110", "rs1": "", "rs2": "", "imm2": ""},
    "bgeu": {"opcode": "1100011", "imm1": "", "funct3": "111", "rs1": "", "rs2": "", "imm2": ""}
}

u_type_instructions = {
    "lui": {"opcode": "0110111","rd":"","imm":""},
    "auipc": {"opcode": "0010111","rd":"","imm":""},
}
j_type_instructions = {
    "jal": {"opcode": "1101111","rd":"","imm":""},
}




instruction_types=[r_type_instructions,i_type_instructions,s_type_instructions,b_type_instructions,u_type_instructions,j_type_instructions]








def get_get(line):
    s = ''
    for i in range(len(line)):
        if i == 0:
            if line[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_":
                s += line[i]
            else:
                return None
                break
        else:
            if line[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz_":
                s += line[i]
                continue
            elif line[i] == ':':
                return s
                break
            else:
                return None
                break
    return None



register_encoding = {
    "x0": "00000",
    "zero": "00000",
    "r0": "00000",
    "x1": "00001",
    "ra": "00001",
    "r1": "00001",
    "x2": "00010",
    "sp": "00010",
    "r2": "00010",
    "x3": "00011",
    "gp": "00011",
    "r3": "00011",
    "x4": "00100",
    "tp": "00100",
    "r4": "00100",
    "x5": "00101",
    "t0": "00101",
    "r5": "00101",
    "x6": "00110",
    "t1": "00110",
    "r6": "00110",
    "x7": "00111",
    "t2": "00111",
    "r6": "00111",
    "r10": "01010",
    "x11": "01011",
    "a1": "01011",
    "r11": "01011",
    "x12": "01100",
    "a2": "01100",
    "r12": "01100",
    "x13": "01101",
    "a3": "01101",
    "r13": "01101",
    "x14": "01110",
    "a4": "01110",
    "r14": "01110",
    "x15": "01111",
    "a5": "01111",
    "r15": "01111",
    "x16": "10000",
    "a6": "10000",
    "r16": "10000",
    "x17": "10001",
    "a7": "10001",
    "x17": "10001",
    "x18": "10010",
    "s2": "10010",
    "r18": "10010",
    "x19": "10011",
    "s3": "10011",
    "r19": "10011",
    "x20": "10100",
    "s4": "10100",
    "r20": "10100",
    "x21": "10101",
    "s5": "10101",
    "r21": "10101",
    "x22": "10110",
    "s6": "10110",
    "r22": "10110",
    "x23": "10111",
    "s7": "10111",
    "r23": "10111",
    "x24": "11000",
    "s8": "11000",
    "r24": "11000",
    "x25": "11001",
    "s9": "11001",
    "r25": "11001",
    "x26": "11010",
    "s10": "11010",
    "r26": "11010",
    "x27": "11011",
    "s11": "11011",
    "r27": "11011",
    "x28": "11100",
    "t3": "11100",
    "r28": "11100",
    "x29": "11101",
    "t4": "11101",
    "r29": "11101",
    "x30": "11110",
    "t5": "11110",
    "r30": "11110",
    "x31": "11111",
    "t6": "11111",
    "r31": "11111"
}



ip=[]
with open("input.txt", 'r') as file:
    ip = [line.strip() for line in file]


ip = [line.split('#')[0].strip() for line in ip]
                        
    
def Ibinaryrep(decimal,totalbits):
    if decimal== 0:
        return '0'.zfill(totalbits)
    if decimal<0:
        decimal = abs(decimal)
        sign= '1'
    else:
        sign= '0'
    binary=''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    binary = sign + binary.zfill(totalbits - 1)
    return (binary)



def instruction(l,line_no,label,line):
    if l[0] in r_type_instructions.keys():
        temp = l[0]+" "
        op_lenght = len(temp)
        lin=line[op_lenght:]
        fun = lin.split(',')
        space_check=lin.split()
        if len(fun)== 3 and len(space_check) == 1:
            try:
                bintemp=""
                registers=[reg.strip(",") for reg in l[1:]]
                bintemp+=r_type_instructions[l[0]]["funct7"]
                bintemp+=register_encoding[registers[0].split(",")[2]]                         
                bintemp+=register_encoding[registers[0].split(",")[1]]
                bintemp+=r_type_instructions[l[0]]["funct3"]
                bintemp+=register_encoding[registers[0].split(",")[0]] 
                bintemp+=r_type_instructions[l[0]]["opcode"]
            except:
                f=open("output.txt","w")
                f.write(f"Invalid register call for {temp} at line {line_no}")
                f.close()
                sys.exit()

        else:
            f=open("output.txt","w")
            f.write(f"Invalid syntax for {temp} at line {line_no}")
            f.close()
            sys.exit()
    
    elif l[0] in i_type_instructions.keys():
        bintemp=""
        if l[0]==("lw" or "lh" or "lb" or "ld"):
            bintemp +=Ibinaryrep(l[1].split(",")[1].split("(")[0],12)
            bintemp +=register_encoding[l[1].split(",")[1].split("(")[1].strip(")")]   #inside bracket
            bintemp +=i_type_instructions[l[0]]["funct3"]
            bintemp +=register_encoding[l[1].split(",")[0]]   # 2nd reg
            bintemp +=i_type_instructions[l[0]]["opcode"]
        else:
            registers=[reg.strip(",") for reg in l[1:]]
            bintemp +=Ibinaryrep(registers[0].split(",")[2],12)
            bintemp +=register_encoding[registers[0].split(",")[1]]
            bintemp +=i_type_instructions[l[0]]["funct3"]
            bintemp +=register_encoding[registers[0].split(",")[0]]
            bintemp +=i_type_instructions[l[0]]["opcode"]
        
    elif l[0] in s_type_instructions.keys():
        bintemp=""
        x=Ibinaryrep(l[1].split(",")[1].split("(")[0],12)
        bintemp +=x[11:5]
        bintemp +=register_encoding[l[1].split(",")[0]]
        bintemp +=register_encoding[l[1].split(",")[1].split("(")[1].strip(")")]
        bintemp +=i_type_instructions[l[0]]["funct3"]
        bintemp +=x[4:0]
        bintemp +=i_type_instructions[l[0]]["opcode"]




    elif l[0] in u_type_instructions.keys():
        bintemp=""
        registers=[operand.strip(",")for operand in l[1:]]
        
        bintemp +=Ibinaryrep(registers[0].split(",")[2],20)
        
        bintemp+=register_encoding[registers[0].split(",")[0]] 
        bintemp +=u_type_instructions[l[0]]["opcode"]

    elif l[0] in j_type_instructions.keys():
        bintemp=""
        registers=[operand.strip(",")for operand in l[1:]]
        x +=Ibinaryrep(registers[0].split(",")[2],20)
        bintemp +=x[20]
        bintemp +=x[10:1]
        bintemp +=x[11]
        bintemp +=x[19:12]  
        bintemp+=register_encoding[registers[0].split(",")[0]] 
        bintemp +=j_type_instructions[l[0]]["opcode"]
        
    elif list[0] in s_type_instructions.keys():
        bintemp=""




    else:
        f=open("output.txt","w")
        f.write(f"Error:Invalid Syntax after label at line no:{line_no}")
        f.close()
        sys.exit()

        




    
 
label=dict() #to store appropriate pointers to respective labels
v_halt="beq zero,zero,0" #to check for virtual halt
count_halt=0 #To check the count for virtual halt

line_no=0
pointer=0
for line in ip:
    line_no = line_no+1 
    if len(line)==0:
        continue
    else:
        pointer = pointer + 1
        l=line.split()
        m=l[0]
        for i in instruction_types:
            if m in i:
                if line==v_halt:
                    count_halt=count_halt+1
                continue
        else:
            d = get_get(line)
            if d in label:
                g=open("output.txt","w")
                g.write(f"Error in Line {line_no} ,Duplicate Label" )#mere lode pe
                g.close()
                sys.exit()
                break
            elif d == None:
                g=open("output.txt","w")
                g.write(f"Error in Line {line_no} ,Invalid Syntax" )#mere lode pe
                g.close()
                sys.exit()
                break
            else:
                gray = len(d) + 1
                ld = line[gray:]
                if len(ld) == 0:
                    label[d] = (pointer)*4
                    continue
                else:
                    ld = ld.strip()
                    if ld==v_halt:
                        count_halt=count_halt+1
                    label[d] = (pointer-1)*4
                    continue

if count_halt==0:
    f=open("output.txt","w") 
    f.write("Error:No Virtual Halt in Program")
    f.close()
    sys.exit()

       
line_no=0
for line in ip:
    line_no = line_no+1 
    if len(line)==0:
        continue
    else:
        l=line.split()
        m=l[0]
        for i in instruction_types:
            if m in i:
                instruction(l,line_no,label,line)
                break
        else:
            d = get_get(line)
            if d == None:
                continue
            else:
                gray = len(d) + 1
                line = line[gray:]
                if len(line) == 0:
                    continue
                else:
                    line = line.strip()
                    l=line.split()
                    instruction(l,line_no,label,line)
                    continue