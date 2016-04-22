from turtle import *
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print ('Unrecognised command')
def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)
instructions = '''Enter a program for the turtle:
N = New drawing
U/D = Pen Up/Down
F = Forward
B = Backward
R = Turn right
L = Turn left
Write number of steps/degree after letter
Insert a hyphen between every movment command'''
screen = getscreen()
while True:
    t_program = screen.textinput('Drawing Machine', instructions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    string_artist(t_program)
