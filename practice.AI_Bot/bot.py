import json
## Choose the JSON File to Process
# File-1 :----> assignment_1_input_1.json
# File-2 :----> assignment_1_input_2.json
File = "assignment_1_input_2.json"

xrange=range ## For Backward Compatibility
## Opening the input json File
f = open(File,"r")
f_name = f.name
input_json = json.loads(f.read())
output_json = {}
var_dict = {} # Dictionary to store variables of json file
## Generating an output file
fo = open("assignment_"+ f_name[-14] + "output" + f_name[-6] + ".json", "w+")

## Function to generate the output dictionary

def generate_json (itr,input_list,user_input,qucik_rep_active,qucikrep,q_rep_mess_no,user_input_flag):
    output_json['stage' + str(itr)] = {'Bot Says': []}
    if(user_input_flag == True):
        output_json['stage' + str(itr)]['User Says'] = str(user_input)

    for message in input_list:
        output_json['stage' + str(itr)]['Bot Says'].append({'message': {"text": str(message)}})
    if(qucik_rep_active == True):
        for i in qucikrep:
            output_json['stage' + str(itr)]['Bot Says'][0]['message']['quick_replies'] = [{
              "content_type": "text",
              "title": str(i).capitalize(),
              "payload": str(i).lower()
              }]
def paramaeter_initializer():
    ##----------------Temporary Variable declaration with default values -----------------------
    input_list = []
    user_input = []
    user_input_flag = False
    qucik_rep_active = False
    q_rep_mess_no = 0
    qucikrep = []
    return (input_list,user_input,user_input_flag,qucik_rep_active,q_rep_mess_no,qucikrep)
    ##----------------Temporary Variable declaration -----------------------

def parse_json (input_json , stage_no,itr):
    ## initializing values
    (input_list ,user_input ,user_input_flag ,qucik_rep_active ,q_rep_mess_no ,qucikrep) = paramaeter_initializer()
    #Case-1
    if('instruction'  in input_json.keys() and 'instruction_var' not in input_json.keys()):
        input_list.append(input_json['instruction'])
        print(input_json['instruction']) ##------<<
        if(input_json['instruction'] == "Congratulations! Registration Successful."):
            user_input_flag = False
            qucik_rep_active = False
            generate_json(stage_no, input_list, user_input, qucik_rep_active, qucikrep, q_rep_mess_no, user_input_flag)
            return stage_no + 1
        user_input_flag = False
        qucik_rep_active = False
        generate_json(stage_no, input_list, user_input, qucik_rep_active, qucikrep, q_rep_mess_no, user_input_flag)
        return stage_no
    # Case-2
    elif(('text' and 'var') in input_json.keys() and (('conditions' and 'options' and 'calculated_variable') not in  input_json.keys()) ):
        input_list.append(input_json['text'])
        var_dict[input_json['var']] = input(str(input_json['text']) + "\n").split(" ")
        if(len(var_dict[input_json['var']]) <= 1):
            var_dict[input_json['var']] = str(var_dict[input_json['var']][0])
        else:
            var_dict['rows'].append(var_dict[input_json['var']])
        user_input_flag = True
        user_input = var_dict[input_json['var']]
        qucik_rep_active = False
        generate_json(stage_no,input_list,user_input,qucik_rep_active,qucikrep,q_rep_mess_no,user_input_flag)
        return stage_no + 1
    # Case-3
    elif (('text' and 'var' and 'options') in input_json.keys() and (('conditions') not in input_json.keys())):
        input_list.append(input_json['text'])
        print(input_json['options'][0])
        print(input_json['options'][1])
        if(input_json['var'] == 'age'):
            var_dict[input_json['var']] = int(input(str(input_json['text']) + "\n"))
        else:
            var_dict[input_json['var']] = input(str(input_json['text']) + "\n")
        user_input_flag = True
        user_input = var_dict[input_json['var']]
        qucik_rep_active = True
        qucikrep = input_json['options']
        q_rep_mess_no = itr - stage_no
        generate_json(stage_no, input_list, user_input, qucik_rep_active, qucikrep, q_rep_mess_no, user_input_flag)
        return stage_no + 1
    #Case-4
    elif (('text' and 'var' and 'conditions') in input_json.keys() and (('options') not in input_json.keys())):
        if(eval(input_json['conditions'][0][0])):
            input_list.append(input_json('text'))
            var_dict[input_json['var']] = input(str(input_json['text']) + "\n")
            user_input_flag = True
            user_input =  var_dict[input_json['var']]
            qucik_rep_active = False
            generate_json(stage_no, input_list, user_input, qucik_rep_active, qucikrep, q_rep_mess_no, user_input_flag)
            return stage_no + 1
        else:
            return stage_no
    #Case-5
    elif (('calculated_variable' and 'var' and 'formula') in input_json.keys()):
        globals().update(var_dict)
        var_dict[input_json['var']] = eval(input_json['formula'])
        return stage_no
    #Case-6
    elif (('instruction_var' and 'instruction') in input_json.keys()):
        if('list_var' in input_json.keys()):
            for i in range(int(input_json['list_length'])):
                input_list.append(input_json['instruction'] % (eval(input_json['instruction_var'][0]),var_dict['t_matrix'][i]))
                qucik_rep_active = False
                user_input_flag = False
                generate_json(stage_no, input_list, user_input, qucik_rep_active, qucikrep, q_rep_mess_no,
                              user_input_flag)
                print(input_json['instruction'] % (eval(input_json['instruction_var'][0]),var_dict['t_matrix'][i]))
            return stage_no
        else:
            input_list.append(input_json['instruction'] % (var_dict[input_json['instruction_var'][0]]))
            qucik_rep_active = False
            user_input_flag = False
            generate_json(stage_no, input_list, user_input, qucik_rep_active, qucikrep, q_rep_mess_no, user_input_flag)
            print(input_json['instruction'] % (var_dict[input_json['instruction_var'][0]]))
            return stage_no




## Iterating over the Questions to ask
stage_itr = 1
for i in range(len(input_json['questions'])):
    stage_itr = parse_json(input_json['questions'][i],stage_itr,i)

## Writing the output Json to File
fo.write(json.dumps(output_json, indent = 4, separators=(',',': ')))
print(fo.name + " is generated")
##Closing the Files before termination
fo.close()
f.close()