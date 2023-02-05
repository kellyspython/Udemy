import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)





data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # dit is nodig om te controleren of het antwoord in de lijst staat.
guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's an nother state's name?: ").title()

    if answer_state == "Exit":

        missing_states = [state for state in all_states if state not in guessed_states]

                                           # missing_states = []
        # bovenstaande                     # for state in all_states:
        # regel vervangt                   # if state not in guessed_states:
        # deze vier regels                 # missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in all_states: # "in" kan je alleen gebruiken voor een lijst!
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        check_answer = data[data.state == answer_state]
        t.goto(int(check_answer.x), int(check_answer.y))
        #t.write(answer_state)# Op deze manier kun je de staat die je al hebt opgeslage gebruiken.
        t.write(check_answer.state.item())# item haalt het antwoord uit alle rotzooi data die meegeleverd wordt.









#screen.exitonclick()