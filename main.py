import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"Guess the State {len(guessed_states)}/50",
                                   prompt="What's another state's name?").title()

    if user_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        break

    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = df[df.state == user_answer]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(f"{state_row.state.item()}", align="center", font=("Arial", 8, "normal"))

# states to learn csv
x = []
y = []
for state in missing_states:
    x.append(df[df.state == state].x.item())
    y.append(df[df.state == state].y.item())
unknown_states_dict = {
    "state": missing_states,
    "x": x,
    "y": y
}
states_to_learn_df = pd.DataFrame(unknown_states_dict)
states_to_learn_csv = states_to_learn_df.to_csv("states_to_learn.csv")
screen.exitonclick()
