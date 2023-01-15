import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

# Title
st.title("Iris' Ohm's Law Simulator!")

# Prompt user for voltage input
voltage_input = int(st.text_input("Total Voltage input: ", 0))

# Prompt user for number of resistors
number_of_resistors = st.number_input("Enter the number of resistors in the circuit: ", 
                                      min_value=None,
                                      max_value=15,
                                      step=1)

# Prompt user for resistance of each resistors and store in a list
i = 0
resistance_list = []                                   
  
while i < number_of_resistors:

    resistance = st.number_input("Resistance of resistor " + str(i+1))
    resistance_list.append(int(resistance))
    i += 1


# Calculate total resistance and voltage
total_resistance = 0
for r in range(len(resistance_list)):
    total_resistance = total_resistance + resistance_list[r]



# Calculate total current
I = 0
if total_resistance == 0:
    pass
else:
    I = int(voltage_input) / total_resistance



# Graph funsies

# get x coordinates
n = len(resistance_list) + 1
x = list(np.array(range(1,n)))
x.insert(0,0)

# get y coordinates

v = voltage_input
y = []

for r in range(len(resistance_list)):
    v = v - I * resistance_list[r]
    y.append(v)

y.insert(0,voltage_input)

# graph title, axis, etc.
plt.title("Voltage Drop Throughout the Circuit")
plt.xlabel("Resistor #")
plt.ylabel("Voltage")

plt.xlim([0, max(x)+0.5])
plt.ylim([0, max(y)+0.5])


# press the button i dare you
if st.button("Graph Voltage Drop!"):
    if number_of_resistors == 0:
        st.text("no resistors inputted... you just made a short circuit and your cat is on fire now")
    else:
        st.balloons()
        fig = plt.step(x,y, where='post')
        plots = plt.scatter(x,y)
        st.pyplot(fig=plt)
        
        st.text("hi")
        
        i = 0
        while i > number_of_resistors:
            st.text("The voltage drop in resistor ", str(x[i]+1), "is", str(y[i]), "volts" )
            i += 1
            
        


else:
    pass