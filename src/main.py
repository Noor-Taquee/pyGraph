from tkinter import Tk, Frame, Canvas, Label, Entry, Button
from turtle import TurtleScreen, RawTurtle
from math import sin, cos, tan, log, pi


# VARIABLES
wHeight = None
wWidth = None
cOrientation = None
aOrientation = ""

# yCorrection = None
# xCorrection = None


screenColor = "white"
functionColor = "blue"
pathWidth = 3

axisColor = "black"
axisLength = 1000

systemFont = "arial"
fontSize = 6
buttonFont = "Sans-serif"
createBg = "green"
clearBg = "orange"

defaultPrecision = 0.1
defaultScale = 50
defaultiValue = -12
defaultfValue = 12
maxLimit = 20

expression = ""
# function = None
precision = defaultPrecision
scale = defaultScale
iValue = defaultiValue
fValue = defaultfValue

lastY = 0
nextY = None
cleared = True


# FUNCTIONS
def createWindow():
  global window
  window = Tk()


def createScreen():
  global screen, pointer
  screen = TurtleScreen(graphArea)
  screen.bgcolor(screenColor)
  pointer = RawTurtle(screen)
  setTurtle()
  drawAxes()


def setTurtle():
  pointer.color(functionColor)
  pointer.speed(0)
  pointer.width(pathWidth)
  pointer.up()
  pointer.goto(0 + xCorrection, 0 + yCorrection)


def checkOrientation(event=None):
  global cOrientation, wHeight, wWidth
  window.update_idletasks()
  wHeight = window.winfo_height()
  wWidth = window.winfo_width()
  if wHeight > wWidth:
    cOrientation = "portrait"
  else:
    cOrientation = "landscape"
  if cOrientation != aOrientation:
    changeLayout()


def changeLayout():
  global \
    aOrientation, \
    screenFrame, \
    topPanel, \
    entryPanel, \
    buttonPanel, \
    graphPanel, \
    fontSize
  for widget in window.winfo_children():
    widget.destroy()
  if cOrientation == "portrait":
    # FRAMES
    screenFrame = Frame(window)
    screenFrame.columnconfigure(0, weight=1)
    screenFrame.rowconfigure(0, weight=3)
    screenFrame.rowconfigure(1, weight=20)
    screenFrame.rowconfigure(2, weight=1)

    entryPanel = Frame(screenFrame)
    entryPanel.columnconfigure(0, weight=1)
    entryPanel.columnconfigure(1, weight=1)
    entryPanel.columnconfigure(2, weight=1)
    entryPanel.columnconfigure(3, weight=1)
    entryPanel.rowconfigure(0, weight=1)
    entryPanel.rowconfigure(1, weight=1)
    entryPanel.rowconfigure(2, weight=1)

    graphPanel = Frame(screenFrame)
    graphPanel.columnconfigure(0, weight=1)
    graphPanel.rowconfigure(0, weight=1)

    buttonPanel = Frame(screenFrame)
    buttonPanel.columnconfigure(0, weight=1)
    buttonPanel.columnconfigure(1, weight=1)
    buttonPanel.rowconfigure(0, weight=1)

    # CANVAS
    global graphArea
    graphArea = Canvas(graphPanel)
    # MESSAGES
    global functionMessage, iValueMessage, fValueMessage, precisionMessage, scaleMessage
    functionMessage = Label(entryPanel, text="fx:", font=(systemFont, fontSize))
    iValueMessage = Label(entryPanel, text="start:", font=(systemFont, fontSize))
    fValueMessage = Label(entryPanel, text="end:", font=(systemFont, fontSize))
    precisionMessage = Label(entryPanel, text="precision:", font=(systemFont, fontSize))
    scaleMessage = Label(entryPanel, text="scale:", font=(systemFont, fontSize))
    # ENTRY
    global functionEntry, iValueEntry, fValueEntry, scaleEntry, precisionEntry
    functionEntry = Entry(entryPanel, font=(systemFont, fontSize))
    iValueEntry = Entry(entryPanel, font=(systemFont, fontSize))
    fValueEntry = Entry(entryPanel, font=(systemFont, fontSize))
    precisionEntry = Entry(entryPanel, font=(systemFont, fontSize))
    scaleEntry = Entry(entryPanel, font=(systemFont, fontSize))
    # BUTTONS
    global bnCreate, bnClear
    bnCreate = Button(
      buttonPanel,
      text="CREATE",
      font=(systemFont, fontSize),
      bg=createBg,
      command=f_create,
    )
    bnClear = Button(
      buttonPanel,
      text="CLEAR",
      font=(systemFont, fontSize),
      bg=clearBg,
      command=f_clear,
    )
    # PLACEMENT==================
    screenFrame.pack(fill="both", expand=True)
    entryPanel.grid(column=0, row=0, sticky="nsew")
    graphPanel.grid(column=0, row=1, sticky="nsew")
    buttonPanel.grid(column=0, row=2, sticky="nsew")

    bnCreate.grid(column=1, row=0, sticky="nsew")
    bnClear.grid(column=0, row=0, sticky="nsew")
  else:
    # FRAMES
    screenFrame = Frame(window)
    screenFrame.columnconfigure(0, weight=1)
    screenFrame.rowconfigure(0, weight=1)
    screenFrame.rowconfigure(1, weight=20)

    topPanel = Frame(screenFrame)
    topPanel.columnconfigure(0, weight=4)
    topPanel.columnconfigure(1, weight=1)
    topPanel.rowconfigure(0, weight=1)

    entryPanel = Frame(topPanel)
    entryPanel.columnconfigure(0, weight=1)
    entryPanel.columnconfigure(1, weight=1)
    entryPanel.columnconfigure(2, weight=1)
    entryPanel.columnconfigure(3, weight=1)
    entryPanel.rowconfigure(0, weight=1)
    entryPanel.rowconfigure(1, weight=1)
    entryPanel.rowconfigure(2, weight=1)

    buttonPanel = Frame(topPanel)
    buttonPanel.columnconfigure(0, weight=1)
    buttonPanel.rowconfigure(0, weight=1)
    buttonPanel.rowconfigure(1, weight=1)

    graphPanel = Frame(screenFrame)
    graphPanel.columnconfigure(0, weight=1)
    graphPanel.rowconfigure(0, weight=1)
    # CANVAS
    graphArea = Canvas(graphPanel)
    # MESSAGES
    functionMessage = Label(entryPanel, text="fx:", font=(systemFont, fontSize))
    iValueMessage = Label(entryPanel, text="start:", font=(systemFont, fontSize))
    fValueMessage = Label(entryPanel, text="end:", font=(systemFont, fontSize))
    precisionMessage = Label(entryPanel, text="precision:", font=(systemFont, fontSize))
    scaleMessage = Label(entryPanel, text="scale:", font=(systemFont, fontSize))
    # ENTRY
    functionEntry = Entry(entryPanel, font=(systemFont, fontSize))
    iValueEntry = Entry(entryPanel, font=(systemFont, fontSize))
    fValueEntry = Entry(entryPanel, font=(systemFont, fontSize))
    precisionEntry = Entry(entryPanel, font=(systemFont, fontSize))
    scaleEntry = Entry(entryPanel, font=(systemFont, fontSize))
    # BUTTONS
    bnCreate = Button(
      buttonPanel,
      text="CREATE",
      font=(systemFont, fontSize),
      bg=createBg,
      command=f_create,
    )
    bnClear = Button(
      buttonPanel,
      text="CLEAR",
      font=(systemFont, fontSize),
      bg=clearBg,
      command=f_clear,
    )
    # PLACEMENT=================
    screenFrame.pack(fill="both", expand=True)
    topPanel.grid(column=0, row=0, sticky="nsew")
    entryPanel.grid(column=0, row=0, sticky="nsew")
    buttonPanel.grid(column=1, row=0, sticky="nsew")
    graphPanel.grid(column=0, row=1, sticky="nsew")

    bnCreate.grid(column=0, row=1, sticky="nsew")
    bnClear.grid(column=0, row=0, sticky="nsew")

  graphArea.grid(column=0, row=0, sticky="nsew")

  functionMessage.grid(column=0, row=0, sticky="nsew")
  iValueMessage.grid(column=0, row=1, sticky="nsew")
  fValueMessage.grid(column=0, row=2, sticky="nsew")
  precisionMessage.grid(column=2, row=1, sticky="nsew")
  scaleMessage.grid(column=2, row=2, sticky="nsew")

  functionEntry.grid(column=1, row=0, columnspan=3, sticky="nsew")
  iValueEntry.grid(column=1, row=1, sticky="nsew")
  fValueEntry.grid(column=1, row=2, sticky="nsew")
  precisionEntry.grid(column=3, row=1, sticky="nsew")
  scaleEntry.grid(column=3, row=2, sticky="nsew")

  aOrientation = cOrientation
  updateCorrection()
  createScreen()
  f_clear()


def updateCorrection():
  global xCorrection, yCorrection
  if aOrientation == "portrait":
    xCorrection = 280
    yCorrection = -350
  else:
    xCorrection = 320
    yCorrection = -100


def drawAxes():
  axesPlotter = RawTurtle(screen)
  axesPlotter.color(axisColor)
  axesPlotter.speed(0)
  axesPlotter.hideturtle()
  axesPlotter.up()
  axesPlotter.goto(0 + xCorrection, 0 + yCorrection)
  axesPlotter.down()
  for i in range(-axisLength, axisLength + 1, 2 * axisLength):
    axesPlotter.goto(0 + xCorrection, 0 + yCorrection)
    axesPlotter.goto(i + xCorrection, 0 + yCorrection)
    axesPlotter.goto(0 + xCorrection, 0 + yCorrection)
    axesPlotter.goto(0 + xCorrection, i + yCorrection)


def getValues():
  global function, precision, scale, iValue, fValue
  function = functionEntry.get()
  try:
    precision = eval(precisionEntry.get())
  except SyntaxError:
    precision = defaultPrecision
  try:
    scale = eval(scaleEntry.get())
  except SyntaxError:
    scale = defaultScale
  try:
    iValue = eval(iValueEntry.get())
  except SyntaxError:
    iValue = defaultiValue
  try:
    fValue = eval(fValueEntry.get())
  except SyntaxError:
    fValue = defaultfValue
  return function


def findExpression():
  global expression
  expression = ""
  i = 0
  while i < len(function):
    char = function[i]
    try:
      nchar = function[i + 1]
    except IndexError:
      nchar = "$"
    if char.isdigit():
      expression += char
      if nchar.isalpha() or nchar in "[{(":
        expression += "*"
    elif char.lower() == "x":
      expression += char
      if nchar.isalnum() or nchar in "[{(":
        expression += "*"
    elif char in "sct":
      try:
        if function[i : i + 3] in "cosintan":
          expression += function[i : i + 3]
          i += 2
      except IndexError:
        pass
    elif char == "p":
      if nchar == "i":
        expression += "pi"
    elif char in "[{(":
      expression += "("
    elif char in ")}]":
      expression += ")"
      if nchar.isalnum():
        expression += "*"
    elif char in "*/+-":
      expression += char
    elif char == "^":
      expression += "**"
    i += 1


def createCordinates(i, f, step):
  cordinates = []
  while i < f:
    cordinates.append(i)
    i += step
  return cordinates


def find(x, org):
  global lastY
  try:
    y = eval(expression.replace("x", str(x)))
  except SyntaxError or ZeroDivisionError:
    y = lastY
  if org:
    lastY = y
  return y


def plotGraph():
  pointer.up()
  for x in createCordinates(iValue, fValue, precision):
    if not cleared:
      currentY = find(x, True)
      nextY = find(x + precision, False)
      if x != iValue:
        if (nextY - currentY) > maxLimit or (nextY - currentY) < -maxLimit:
          pointer.up()
        else:
          pointer.down()
      pointer.goto(x * scale + xCorrection, currentY * scale + yCorrection)


# BUTTON FUNCTION
def f_create():
  global cleared
  if cleared:
    if getValues():
      cleared = False
      findExpression()
      plotGraph()


def f_clear():
  global cleared, lastY
  pointer.reset()
  setTurtle()
  cleared = True
  lastY = 0


createWindow()
checkOrientation()
window.bind("<Configure>", checkOrientation)
window.mainloop()
