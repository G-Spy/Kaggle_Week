import random

### 1. Read and parse input file

# file_name = '0_example'
# file_name = '1_binary_landscapes'
file_name = '10_computable_moments'
# file_name = '11_randomizing_paintings'
# file_name = '110_oily_portraits'

file_path = './Data/'+ file_name +'.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

# Initialize storage for parsed data
parsed_data = []

painting_number = int(lines[0]);
new_lines = lines[1:];

# Process each line
for line in new_lines:
    # Clean up the line
    line = line.strip()
    if line:  # Skip empty lines
        # Split the line into components
        components = line.split()
        label = components[0]  # 'L' or 'P'
        number = int(components[1])  # The number after the label
        words = components[2:]  # Remaining words

        # Store parsed information
        parsed_data.append({
            'label': label,
            'numberOfTags': number,
            'tags': words
        })

# # Print the parsed data
# for entry in parsed_data:
#     print(entry)
#
# print(parsed_data['label'])
# print(parsed_data['tags'])

### 2. Generate output file

def generateOutputSameOrder(painting_number,parsed_data, output_file_path):
    # Open the file in write mode
    with open(output_file_path, 'w') as file:
        file.writelines(f"{painting_number} \n");
        for entry in parsed_data:
            # Format each entry as a line in the file
            line = f"{entry['label']} {entry['numberOfTags']} " + " ".join(entry['tags'])
            file.write(line + '\n')  # Write the line followed by a newline

    print(f"Parsed data saved to {output_file_path}")

def generateOutputReverseOrder(painting_number,parsed_data, output_file_path):
    parsed_data.reverse()

    # Open the file in write mode
    with open(output_file_path, 'w') as file:
        file.writelines(f"{painting_number} \n");
        for entry in parsed_data:
            # Format each entry as a line in the file
            line = f"{entry['label']} {entry['numberOfTags']} " + " ".join(entry['tags'])
            file.write(line + '\n')  # Write the line followed by a newline

    print(f"Parsed data saved to {output_file_path}")

def generateOutputRandomOrder(painting_number,parsed_data, output_file_path):
    random.shuffle(parsed_data)

    # Open the file in write mode
    with open(output_file_path, 'w') as file:
        file.writelines(f"{painting_number} \n");
        for entry in parsed_data:
            # Format each entry as a line in the file
            line = f"{entry['label']} {entry['numberOfTags']} " + " ".join(entry['tags'])
            file.write(line + '\n')  # Write the line followed by a newline

    print(f"Parsed data saved to {output_file_path}")

# same order
output_file_path = './OutputData/'+ file_name + '_output_same_order.txt'
generateOutputSameOrder(painting_number,parsed_data,output_file_path)

# reversed order
output_file_path = './OutputData/'+ file_name + '_output_reverse_order.txt'
generateOutputReverseOrder(painting_number,parsed_data,output_file_path)

# shuffle order
output_file_path = './OutputData/'+ file_name + 'output_random_order.txt'
generateOutputRandomOrder(painting_number,parsed_data,output_file_path)

# order by tags inside frameglasse

### 3. Write output file

# 4.



