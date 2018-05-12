import json

data_path = r"/home/pooja/Downloads/NLPCode/event_detection.data.filter.json"  # event_detection.data.filter.json

with open(data_path,'r') as in_json_file:

    # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)

    length = len(json_obj_list)
    number_of_chunks = 4000
    count = 0
    for i in range(0, length, number_of_chunks):
        filename = r"/home/pooja/Downloads/NLPCode/Chunks/InputChunks/event_detection_chunk" + str(count)
        t = json_obj_list[i:i + number_of_chunks]
        with open(filename, 'w') as out_json_file:
            json.dump(t, out_json_file, indent=4)
        count = count + 1
