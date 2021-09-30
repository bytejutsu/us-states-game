import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
right_guesses = []

while len(right_guesses) < len(all_states):
    answer_state = screen.textinput(title=f"{len(right_guesses)}/{len(all_states)}", prompt="Give a state\'s name").title()

    if answer_state == "Exit":
        diff = [item for item in all_states if item not in right_guesses]
        new_data = pandas.DataFrame(diff)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in right_guesses:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state)
        right_guesses.append(answer_state)

screen.textinput(title="Good job!", prompt="you guessed all the states right")


