import turtle
import pandas

screen = turtle.Screen()
screen.title('USA States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

# While loop that keeps the game going until you have guessed all 50 states
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt='Enter a state\'s name').title()
    # Create an exit keyword to exit the game when you are finished
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv('states_to_learn.csv')
        break
    # Write state over correct state if guessed
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data['state'] == answer_state]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(state_info.state.item())


# Create csv file that contains missing states that weren't guessed
missing_states = pandas.DataFrame(all_states)
missing_states.to_csv('states_to_learn.csv')
