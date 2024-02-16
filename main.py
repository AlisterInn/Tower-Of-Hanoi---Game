from flask import Flask, request, render_template, flash
import secrets
from stack import Stack

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='/')
app.config['SECRET_KEY'] = secrets.token_hex(16)

def reset(number_of_disks=3, number_of_towers=3, max_disk_size=90):
    '''Game [re]initializer
    - Resets the game counter to 0 steps
    - Resets gameActive flag to True
    - Initializes and returns a stack for each tower 
    '''
    counter = 0
    gameActive = True

    stacks = [Stack() for i in range (number_of_towers)]

    for i in range(number_of_disks):
        disk_size = max_disk_size-15*i
        stacks[0].push(disk_size)

    return stacks, counter, gameActive, number_of_disks

stacks, counter, gameActive, number_of_disks = reset()

@app.route('/', methods=['GET', 'POST'])
def main():
    global stacks, counter, gameActive, number_of_disks

    if request.method == 'POST':
        if 'reset' in request.form:
            number_of_disks = int(request.form.get('disks'))
            number_of_towers = int(request.form.get('towers'))
            stacks, counter, gameActive, number_of_disks = reset(number_of_disks, number_of_towers)
            
        elif 'move' in request.form and gameActive:
            # Step 2: Get the source and destination tower IDs from the form
            src = int(request.form.get('from'))
            dst = int(request.form.get('to'))
            # Remove pass after you are done with step 2

            # Step 3: Move the disk from the source tower to the destination tower if it is possible. 
            if not stacks[src].isEmpty() and (stacks[dst].isEmpty() or stacks[src].peek() < stacks[dst].peek()):
                disk = stacks[src].pop()
                stacks[dst].push(disk)
            # Increase the counter by one if the move was successful
                counter += 1
            # Otherwise, use flash('message') to print a relevant message on the screen
                flash('Successful move! 💫💫💫💫💫💫💫')
            else:
                flash('Illegal move! Try again. ˙◠˙ ˙◠˙')

            # Step 4. Check if the user has won after each move. 
            # If it is true, print a relevant message using flash('...') function 
            # and set gameActive flag to False.
            if len(stacks[-1]) == number_of_disks:
                flash('Congratulations, You won! 🌟🌟🌟🌟🌟🌟🌟')
                gameActive = False


    return render_template("game_template.html", stacks=stacks, towers=len(stacks), counter=counter, gameActive=gameActive)


app.run()