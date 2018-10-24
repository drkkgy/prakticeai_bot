# prakticeai_bot
a simple response bot on the given input 

Created Using Python 3.6 

Code is in --> bot.py

Minor issues with the input2 Json Corrected 



{
            "calculated_variable":"True",
            "formula":"[map(int, i.split()) for i in row]",
            "var":"matrix"
        },
---------------------------changed to this-------------------------
{
            "calculated_variable":"True",
            "formula":"[map(int, i.split()) for i in rows]",
            "var":"matrix"
        },

Bot Works on both the input file which can be changed by chaning the file name in the top of the Code
# File-1 :----> assignment_1_input_1.json
# File-2 :----> assignment_1_input_2.json
File = "assignment_1_input_2.json"  <-------------

* Here the Files have been to be assumed to be in local directory and the output will be generated in the local directory it self 
assignment_1output1.json
assignment_1output2.json

Note[Please input a single word for age and not a string "currently it fails on doing so"]

for any issue in the code please let me know :)