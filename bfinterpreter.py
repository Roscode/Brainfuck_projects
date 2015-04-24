"""brainfuck to text"""

bfinput = "+++[->+++<]>[->++++++++<]>.\
>++++[->+++++<]>[->+++++<]>+.\
>+++[->+++++<]>[->++++++++<]>+.\
>++[->+++++<]>+[->++++<]>.\
>++++[->++++++++<]>.\
>+++[->++++++<]>[->++++++<]>.\
>++++++[->++++++<]>+[->+++<]>.\
>++++++[->++++++<]>+[->+++<]>.\
>++[->++++++<]>+[->++++<]>+[->++<]>+.\
>++++[->++++++++<]>.\
>++[->++++++++<]>+[->+++++++<]>.\
>++[->++++++<]>+[->++++++++<]>.\
>++[->++++++<]>[->++++++++<]>+.\
>++++[->+++++++<]>+[->++++<]>.\
>++++[->++++++++<]>.\
>+++[->+++<]>[->++++++++<]>+.\
>++++[->++++++++<]>.\
>++++[->+++++<]>[->+++++<]>.\
>+++[->+++++<]>[->+++++++<]>.\
>++++[->+++++<]>[->+++++<]>.\
>++[->+++++<]>+[->+++<]>.\
>"
class bfbits:
    def __init__ (self):
        self.mempoint = 0
        self.instructpoint = 0
        self.byteline = [0]*500
        self.loopspot = []
        self.loopdepth = 0
        self.on = True
        self.offdepth = 0
        self.outputstring =''
    def moveright(self):
        if(self.on):
            self.mempoint += 1
    def moveleft(self):
        if(self.on):
            self.mempoint -= 1
    def increment(self):
        if(self.on):
            self.byteline[self.mempoint] += 1
    def decrement(self):
        if(self.on):
            self.byteline[self.mempoint] -= 1
    def takeinput(self):
        if(self.on):
            inpt = raw_input()
            self.byteline[self.mempoint] = inpt
    def giveoutput(self):
        if(self.on):
            print(chr(self.byteline[self.mempoint]))
            self.outputstring += chr(self.byteline[self.mempoint])
    def beginloop(self):
        if(self.byteline[self.mempoint]!=0 and self.on):
            self.loopspot.append(self.instructpoint)
            self.on = True
            self.loopdepth += 1
        elif(self.btyeline[selt.mempoint] == 0 and self.on):
            self.on = False
            self.offdepth = self.loopdepth
    def endloop(self):
        if(self.byteline[self.mempoint]!=0 and self.on):
            self.instructpoint =self.loopspot[self.loopdepth-1]
        elif(self.byteline[self.mempoint]==0 and self.on):
            self.loopspot.pop()
            self.loopdepth -= 1
        if(self.loopdepth == self.offdepth):
            self.on = True
    def contread(self):
        self.instructpoint += 1

reader = bfbits()

commands = {'+' : reader.increment, '-' : reader.decrement,
            '>' : reader.moveright, '<' : reader.moveleft,
            '.' : reader.giveoutput, ',' : reader.takeinput,
            '[' : reader.beginloop, ']' : reader.endloop, }

while(reader.instructpoint<len(bfinput)):
    commands[bfinput[reader.instructpoint]]()
    reader.contread()
print(reader.outputstring)
