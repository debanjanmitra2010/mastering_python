import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # Using List Comprehension
        missing_states = [state for state in all_states if state not in guessed_state]

        # states to learn.csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # If they got it right
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Create a turtle to write the name of the state at the state's x and y coordinate
        t.write(state_data.state.item())  # Or t.write(answer_state)


