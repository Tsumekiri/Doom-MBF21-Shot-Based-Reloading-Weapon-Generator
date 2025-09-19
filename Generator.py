# Read the number of shots from user input
print('How many shots do you want your weapon to have before reloading?')
numShots = int(input())

# Initialize empty string
readyState = ''
fireState = ''

# Read the contents of the ready and fire state files
with open('ready_state.txt', 'r') as f:
    readyState = f.read()

with open('fire_state.txt', 'r') as f:
    fireState = f.read()


# Beautify it slightly, feel free to add or remove tabs (they're the \t) as well as end of lines (that's \n)
readyState = readyState.replace('\n', '\n\t\t')
fireState = fireState.replace('\n', '\n\t\t')

result = ''

# For each shot write fire and ready states
for i in range(1, numShots):
    # Skip writing the first fire state, the user should already have one
    if (i != 1):
        result += '\tfire' + str(i) + ':\n'
        result += '\t\t' + fireState + '\n'
    
    # Write the ready state with a loop at the end
    result += '\tready' + str(i) + ':\n'
    result += '\t\tTNT1 A 0 A_RefireTo("fire' + str(i + 1) + '")\n'
    result += '\t\t' + readyState + '\n'
    result += '\t\tloop\n'

# Write the last fire state
if (numShots == 1):
    result += '\tfire' + ':\n'
else:
    result += '\tfire' + str(numShots) + ':\n'

result += '\t\t' + fireState + '\n'

# Show result on console
print(result)

# Write result to a file
with open('weapon_result.txt', 'w') as f:
    f.write(result)