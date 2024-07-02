'''
def write_data_to_txt(file_name, data):
    if isinstance(data, str):
        with open(file_name + '.txt', 'w') as f:
            f.write(data)
    else:
        with open(file_name + '.txt', 'a+') as f:
            if f.tell() != 0:
                f.write('\n')
            f.write(str(data))
'''

def write_data_to_txt(file_name, data):
    with open(file_name + '.txt', 'w') as f:
        if isinstance(data, str):
            f.write(data)
        else:
            f.write(str(data))



def read_data_from_txt(file_name):
    with open(file_name + '.txt', 'r') as file:
        content = file.read()
        if len(content) >= 4300:
            return content
        else:
            cleaned_content = content.replace('[', '').replace(']', '').replace(',', '').split()
            data = [int(number) for number in cleaned_content]
            return data



