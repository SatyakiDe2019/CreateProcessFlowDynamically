#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 15-Jul-2024                     ####
#### Modified On 20-Jul-2024                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### clsGenFlowLLM class to initiate the         ####
#### data flow capability in real-time.          ####
####                                             ####
#####################################################

# Sample Q1: "Create a flowchart for the process of making a cup of coffee using a drip coffee maker."
# Sample Q2: "Generate a diagram showing the steps in a basic CI/CD pipeline."
# Sample Q3: "Create a flowchart for the process of handling a user login in a web application."

# We keep the setup code in a different class as shown below.
import clsGenFlowLLM as gfl

from clsConfigClient import clsConfigClient as cf

import datetime
import logging

def main():
    try:
        # Other useful variables
        debugInd = 'Y'

        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('Start Time: ', str(var))

        # Initiating Log Class
        general_log_path = str(cf.conf['LOG_PATH'])

        # Enabling Logging Info
        logging.basicConfig(filename=general_log_path + 'genFLDLog.log', level=logging.INFO)

        print('Started predicting best bodyline deliveries from the Cricket Streaming!')

        # Passing source data csv file
        x1 = gfl.clsGenFlowLLM()

        while True:
            desc = input("Enter the subject to generate the flow diagram (or 'quit' to exit): ")

            var1 = datetime.datetime.now()

            if desc.lower() == 'quit':
                break

            # Execute all the pass
            r1 = x1.generateFlowchart(desc, debugInd, var1)

            if (r1 == 0):
                print('Successfully generated Flow Diagram based on the content!')
            else:
                print('Failed to generate Flow Diagram!')

            r1 = 0

            var2 = datetime.datetime.now()

            c = var2 - var1
            minutes = c.total_seconds() / 60
            print('Total difference in minutes: ', str(minutes))

        var3 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        print('End Time: ', str(var3))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
