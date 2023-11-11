from graphics import * 

def FinalDigitPatch7(window, primarycolor,alternatecolor,outlinecolor,TLXcoordinate, TLYcoordinate):

    
    incrementor = 5 
    TopLeftPoint = Point(TLXcoordinate, TLYcoordinate)
    BottomRightPointXCoordinate = TLXcoordinate + 100 # Bottomright coordinate was just 100 bigger than the TopLeft
    BottomRightPointYCoordinate = TLYcoordinate + 100
    BottomRightPoint = Point(BottomRightPointXCoordinate,BottomRightPointYCoordinate)

    for i in range(0, 50, 5):
        squareColor = ""
        
        if i == 5 or i == 15 or i == 25 or i == 35 or i == 45:
            squareColor = alternatecolor #Each of the white square TL x coordinate was 10 bigger starting at 5
        

        if i == 0 or i == 10 or i == 20 or i == 30 or i == 40: 
            squareColor = primarycolor  #each of the coloured squares was TL X coordinate was 10 bigger starting at 0
                
        patch = drawRectangle(window, TopLeftPoint, BottomRightPoint,squareColor,outlinecolor)

        TopLeftPoint.x = TopLeftPoint.x + incrementor #as the inside squares got smaller it increased by 5
        TopLeftPoint.y = TopLeftPoint.y + incrementor

        BottomRightPoint.x = BottomRightPoint.x - incrementor # as the squares on the inside got smaller it decreased by 5
        BottomRightPoint.y = BottomRightPoint.y - incrementor

        #return patch


       
    window.getMouse()
    window.Close() 

def drawTwoRectangles(window,RectOneTL,RectOneBR, RectTwoTL,RectTwoBR, color, outline): 
    rectangleOne = Rectangle(RectOneTL, RectOneBR)
    rectangleTwo = Rectangle(RectTwoTL, RectTwoBR) 
    rectangleOne.setFill(color)
    rectangleTwo.setFill(color)
    rectangleOne.setOutline(outline)
    rectangleTwo.setOutline(outline)

    rectangleOne.draw(window)
    rectangleTwo.draw(window) 

    return rectangleOne,rectangleTwo

def PenUltimatePatch8(win, color, outline,TLXcoor,TLYcoor): #TLXCoor and TlYcoor handle the topleft point for the patch design allowing it to be moved around depending on the topleft coordinate it's been fed

    #background 

    drawRectangle(win,Point(TLXcoor,TLYcoor),Point(TLXcoor+100,TLYcoor+100),"white",outline)

    for i in range(20,90,20):
        drawRectangle(win,Point(TLXcoor,i+TLYcoor),Point(TLXcoor+100,i+TLYcoor),"white",outline)
        print(i)
    
    #pattern

    for y in range(0, 90, 40):
        for x in range(0, 90, 20):
            if x == 20 or x == 60:
                drawTwoRectangles(win, Point(x+TLXcoor,y+TLYcoor),Point(x+20+TLXcoor,y+5+TLYcoor),Point(x+TLXcoor,y+10+TLYcoor),Point(x+20+TLXcoor,y+15+TLYcoor),color,outline) #used RectOneTl and RectOneBr as the reference point to increase or decrease values
            if x== 0 or x == 40 or x == 80:
                drawTwoRectangles(win, Point(x+TLXcoor,y+TLYcoor),Point(x+5+TLXcoor,y+20+TLYcoor),Point(x+10+TLXcoor,y+TLYcoor),Point(x+15+TLXcoor,y+20+TLYcoor),color,outline)
    
    for y2 in range(00, 90, 40):
        for x2 in range(20, 110, 20):
            secondRectBR = Point(x2,y2)
            if secondRectBR.x == 40 or secondRectBR.x == 80:
                drawTwoRectangles(win, Point(secondRectBR.x-15+TLXcoor,secondRectBR.y-20+TLYcoor),Point(secondRectBR.x-10+TLXcoor,secondRectBR.y+TLYcoor),Point(secondRectBR.x-5+TLXcoor,secondRectBR.y-20+TLYcoor),Point(secondRectBR.x+TLXcoor,secondRectBR.y+TLYcoor),color,outline) #SecondBr was used as the referencePoint for the mathsnn

            if secondRectBR.x == 20 or secondRectBR.x == 60 or secondRectBR.x == 100:
                drawTwoRectangles(win,Point(secondRectBR.x-20 + TLXcoor ,secondRectBR.y-15 +TLYcoor),Point(secondRectBR.x +TLXcoor ,secondRectBR.y-10 +TLYcoor),Point(secondRectBR.x-20+TLXcoor,secondRectBR.y-5+TLYcoor),Point(secondRectBR.x+TLXcoor,secondRectBR.y+TLYcoor),color,outline)
    
   
    win.getMouse()
    win.Close() 

def drawRectangle(win, tlpoint, brpoint, color, outlinecolor):
    rectangle = Rectangle(tlpoint, brpoint)

    if color == "none" and outlinecolor == "none":
        rectangle.draw(win)
        rectangle.setFill("white")
        rectangle.setWidth(0) 
    
    elif outlinecolor == "none":
        rectangle.draw(win)
        rectangle.setFill(color) 
        rectangle.setWidth(0)

    elif color == "none":
        rectangle.draw(win)
        rectangle.setFill("white") 
        rectangle.setOutline(outlinecolor)

    else:
        rectangle.draw(win) 
        rectangle.setFill(color)
        rectangle.setOutline(outlinecolor)
        rectangle.setWidth(0.2) 
        
    return rectangle 


colours = ["red", "green", "purple", "orange", "cyan"]
window_size_list = [500, 700]

screensize = 0
while screensize != window_size_list[0] or screensize != window_size_list[1]: #Runs the loop while the variable screensize(user input) does not equal any of the window sizes stored in the list 

    screensize = input(("Enter the size of the window you would like, 5 = 500x500 or 7= 700x700: ")) 
    screensize = int(screensize)
    
    if screensize == 5:
        screensize = window_size_list[0]
        break #Ends the while loop

    if screensize == 7:
        screensize = window_size_list[1]
        break

    else:
        print("") #Empty string to create space and allow the user to read prompts more clearly.
        print("Sorry, the data you enter is invalid, please re-enter your screensize.")
        print("") 

firstColorInput = ""
while firstColorInput != colours[0] or firstColorInput != colours[1] or firstColorInput != colours[2] or firstColorInput != colours[3] or firstColorInput != colours[4]: #While the user input does not equal any of the colours stored in the list the loop runs
    firstColorInput = input("Please enter your first colour of choice: ")
    firstColorInput = firstColorInput.lower() 

    if firstColorInput == colours[0]:
        firstColorInput = colours[0]
        break

    elif firstColorInput == colours[1]:
        firstColorInput = colours[1]
        break

    elif firstColorInput == colours[2]:
        firstColorInput = colours[2]
        break

    elif firstColorInput == colours[3]:
        firstColorInput = colours[3]
        break

    elif firstColorInput == colours[4]:
        firstColorInput = colours[4]
        break
    else:
        print("") #Empty string to create space and allow the user to read prompts more clearly.
        print("Sorry, this data is invalid, please re-enter your first color choice")
        print("") #Empty string to create space and allow the user to read prompts more clearly.

secondColorInput = ""
while secondColorInput != colours[0] or secondColorInput != colours[1] or secondColorInput != colours[2] or secondColorInput != colours[3] or secondColorInput != colours[4]:
    secondColorInput = input("Please enter your second colour of choice: ")
    secondColorInput = secondColorInput.lower() 

    if secondColorInput == colours[0]:
        secondColorInput = colours[0]
        break

    elif secondColorInput == colours[1]:
        secondColorInput = colours[1]
        break

    elif secondColorInput == colours[2]:
        secondColorInput = colours[2]
        break

    elif secondColorInput == colours[3]:
        secondColorInput = colours[3]
        break

    elif secondColorInput == colours[4]:
        secondColorInput = colours[4]
        break
    else:
        print("") #Empty string to create space and allow the user to read prompts more clearly.
        print("Sorry, this data is invalid, please re-enter your second colour choice.")
        print("") #Empty string to create space and allow the user to read prompts more clearly.

thirdColorInput = ""
while thirdColorInput != colours[0] or thirdColorInput != colours[1] or thirdColorInput != colours[2] or thirdColorInput != colours[3] or thirdColorInput != colours[4]:
    thirdColorInput = input("Please enter your third colour of choice: ")
    thirdColorInput = thirdColorInput.lower() 

    if thirdColorInput == colours[0]:
        thirdColorInput = colours[0]
        break

    elif thirdColorInput == colours[1]:
        thirdColorInput = colours[1]
        break

    elif thirdColorInput == colours[2]:
        thirdInput = colours[2]
        break

    elif thirdColorInput == colours[3]:
        thirdColorInput = colours[3]
        break

    elif thirdColorInput == colours[4]:
        thirdColorInput = colours[4]
        break
    else:
        print("") #Empty string to create space and allow the user to read prompts more clearly.
        print("Sorry, this data is invalid, please re-enter your third colour choice.")
        print("") #Empty string to create space and allow the user to read prompts more clearly. 

def main(window, color,outline):

    for x in range(0, screensize, 100): #creates the background of the patch using the first color input
        for y in range(0, screensize, 100): #first loop is the x coordinate then for every x coordinate a y coordinate is provided the number the loop ends on is based on the screensize 
            TopLeft = Point(x, y)
            bottomRight = Point(x+100, y+100) #bottomright point is always 100 more than both the x and y coordinate
            drawRectangle(window,TopLeft, bottomRight, color, outline)
                

    for x1 in range(100, screensize-(+100),100):
        for y1 in range(100,screensize-(+100),100):
            TopLeft1 = Point(x1, y1)
            bottomRight1 = Point(x1+100, y1+100)
            drawRectangle(window, TopLeft1,bottomRight1, secondColorInput, outline)
    
    if screensize == 500:
        drawRectangle(window,Point(300,200),Point(400,300),thirdColorInput,outline)
        drawRectangle(window,Point(300,300),Point(400,400),thirdColorInput,outline)
        drawRectangle(window,Point(200,300),Point(300,400),thirdColorInput,outline) 

        #drawing patches
    
        for i in range(0, screensize, 200):
            for i2 in range(0,screensize,100):
                if (i == 100 and i2 ==200) or (i == 200 and i2 == 200):
                    FinalDigitPatch7(window,secondColorInput,"white","black",i,i2)
                if (i== 300 and i2==200):
                    FinalDigitPatch7(window,thirdColorInput,"white","black",i,i2)
                else:
                    FinalDigitPatch7(window,firstColorInput,"white","black",i,i2)



    if screensize == 700:
        drawRectangle(window,Point(200,500),Point(300,600),thirdColorInput,outline)
        drawRectangle(window,Point(300,500),Point(400,600),thirdColorInput,outline)
        drawRectangle(window,Point(400,500),Point(500,600),thirdColorInput,outline)
        drawRectangle(window,Point(500,500),Point(600,600),thirdColorInput,outline)
        drawRectangle(window,Point(300,400),Point(400,500),thirdColorInput,outline)
        drawRectangle(window,Point(400,400),Point(500,500),thirdColorInput,outline)
        drawRectangle(window,Point(500,400),Point(600,500),thirdColorInput,outline)
        drawRectangle(window,Point(400,300),Point(500,400),thirdColorInput,outline)
        drawRectangle(window,Point(500,300),Point(600,400),thirdColorInput,outline)
        drawRectangle(window,Point(500,200),Point(600,300),thirdColorInput,outline)
       
        PenUltimatePatch8(window,secondColorInput,"black",100,300)

    
            

    window.getMouse()
    window.Close() 

   
main(GraphWin("...",screensize, screensize), firstColorInput, "black")

