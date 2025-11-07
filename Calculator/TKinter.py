#*******************************************************************
# Course:      CSCI 201
#Assignment: Classwork 03-24-2024
# Programmer: Jerard Austin
# Instructor: Dr. Mirek Mystkowski
# Date: March 24th 2024
# Synopsis: This program displays a window from tkinter that displays a calculator
# Test case 1:
# input: 3 + 6 =
# expected output: 9
# actual output: 9
# Test case 2:
# input:
# expected output:
# actual output:
# Test case 3:
# …………….
#*******************************************************************


from tkinter import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, levels):
        self.levels = levels
        self.root = None

    def add(self, value):
       self.root = self._add(self.root,value)

    def _add(self, node:Node, value):

        if node is None:
            return Node(value)
        else:
            levels = self.levels

            if levels.get(value, 0) >= levels.get(node.value, 0):

                newNode = Node(value)
                newNode.left = node

                return newNode
            else:
                 node.right = self._add(node.right, value)
                 return node


    def calc(self):
        return self._calc(self.root)


    def _calc(self, node):
        if node.left is None and node.right is None:
            return int(node.value)
        else:

            result = 0

            if node.value == '/':
                result = self._calc(node.left) / self._calc(node.right)
            elif node.value == 'x':
                result = self._calc(node.left) * self._calc(node.right)
            elif node.value == '+':
                result = self._calc(node.left) + self._calc(node.right)
            elif node.value == '-':
                result = self._calc(node.left) - self._calc(node.right)

            return result



class Calculator:

    def __init__(self):
        # Configuartions:
        min_width = 300
        min_height = 400

        top_ratio = 1
        mid_ratio = 7
        bottom_ratio = 2

        # min_width + 30% of min_width
        max_width = int(min_width * 1.3)
        max_height = int(min_height  * 1.3)

        top_height = int(min_height * top_ratio/10)
        middle_height = int(min_height * mid_ratio/10)
        bottom_height = int(min_height * bottom_ratio/10)

        top_frame_font = 'Courier 22 bold'

        bottom_frame_font = 'Courier 22 bold'

        middle_frame_font = 'Courier 20 bold'

        self.currentNumber = "0"
        self.OPERATOR_LEVEL = {
            "x": 1,
            "/": 1,
            "+": 2,
            "-": 2,


        }

        # Window
        self.window = Tk()

        root = self.window
        root.title('My Calculator')


        root.minsize(width=min_width,height=min_height )
        root.maxsize(width=max_width,height=max_height)

        # Frames: Top, Middle, Bottom
        topFrame = Frame(

            root,
            width=min_width,
            height=top_height ,
            bg= 'red'

        )

        midFrame = Frame(

            root,
            width=min_width,
            height=middle_height,
            #bg='green'

        )

        bottomFrame = Frame(

            root,
            width=min_width,
            height=bottom_height,
            bg='blue'

        )


        # NEWS - North -> top, East -> right, West -> left, South -> bottom


        topFrame.grid(row=0, column=0 , sticky= 'news')
        midFrame.grid(row=1,column=0, sticky= 'news')
        bottomFrame.grid(row=2, column=0, sticky= 'news')

        root.columnconfigure(0, weight=1) # weight = growth ratio
        root.rowconfigure(0,weight=1)
        root.rowconfigure(1, weight=7)
        root.rowconfigure(2, weight=2)

        # Build frame contents:

        self._BuildTopFrameContent(topFrame, top_frame_font)
        self._BuildMiddleFrameContent(midFrame, middle_frame_font)
        self._BuildBottomFrameContent(bottomFrame,bottom_frame_font)


        self.currentNumber = '0'


        self.window.mainloop()

    def _BuildTopFrameContent(self, frame:Frame, fontConfig):

        self.lbl_display = Label(

            frame,
            text= '0',
            anchor= 'e', # anchor to the east
            font =  fontConfig
        )
        self.lbl_display.grid(row=0,column=0, sticky='news')

        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0, weight=1)

    def _BuildMiddleFrameContent(self, frame: Frame, fontConfig):
       buttons = [
           ['7','8','9','/'],
           ['4', '5', '6', 'x'],
           ['1', '2', '3', '-'],
           [' ', '0', ' ', '+'],

       ]
       for ridx,row in enumerate (buttons):

           frame.rowconfigure(ridx,weight=1)

           for cidx,col in enumerate(row):

               frame.columnconfigure(cidx,weight=1)

               if col != ' ':

                   btn = Button(

                        frame,
                        text=col,
                        font=fontConfig,
                       #command= self._ifNoLambdaWasAvailableInPython(col)
                        command=lambda x = col:self._btn_NoOp_action(x)
                    )
                   btn.grid(row= ridx,column=cidx,sticky="news")



    def _btn_NoOp_action(self, value): #number
        if value.isdigit():

            if self.currentNumber.startswith('0'):
                self.currentNumber = value
                self.lbl_display['text'] = self.lbl_display['text'][:-1]
            else:
                self.currentNumber += value

        else: #operator

            if not self.lbl_display['text'][-1].isdigit():
                self.lbl_display['text'] = self.lbl_display['text'][:-1]


        self.lbl_display['text'] += value
        print(self.currentNumber )



    def _BuildBottomFrameContent(self, frame:Frame, fontConfig):
        btn_clr = Button(
            frame,
            text= 'clear',
            font= fontConfig,
            command= self._btn_clr_action
        )

        btn_eq = Button(
            frame,
            text='=',
            font=fontConfig,
            command=self._btn_eq_action
        )

        btn_clr.grid(row=0, column=0, sticky="news")
        btn_eq.grid(row=0, column=1, sticky="news")

        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(1,weight=1)
        frame.rowconfigure(0,weight=1)



    def _btn_clr_action(self):
        self.lbl_display['text'] = '0'
        self.currentNumber = '0'

    def _btn_eq_action(self):
       expTree = self._BuildExpressionTree()
       result = expTree.calc()
       self.lbl_display["text"] = result
       self.currentNumber = result

    def _BuildExpressionTree(self):
        expTree = ExpressionTree(self.OPERATOR_LEVEL)
        displayExp = self.lbl_display["text"]

        if not displayExp[-1].isdigit():
            displayExp = displayExp[:-1]


        numberStr = ""
        for char in displayExp:
            if char.isdigit():
                numberStr += char
            else:
                expTree.add(numberStr)
                numberStr = ""

                expTree.add(char)
        expTree.add(numberStr)

        return expTree

Calculator()

