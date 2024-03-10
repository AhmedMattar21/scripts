import yaml

def decode_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    decoded_data = decode_yaml_values(yaml_data)
    return decoded_data

def decode_yaml_values(data):
    if isinstance(data, dict):
        return {key: decode_yaml_values(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [decode_yaml_values(item) for item in data]
    elif isinstance(data, str):
        return data.encode('utf-8').decode('unicode_escape')
    else:
        return data

def encode_yaml_values(data):
    if isinstance(data, dict):
        return {key: encode_yaml_values(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [encode_yaml_values(item) for item in data]
    elif isinstance(data, str):
        return data.encode('unicode_escape').decode('utf-8')
    else:
        return data

def write_yaml_file(file_path, data):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

if __name__ == "__main__":
    yaml_file_path = "env-vpsie.yaml"
    
    # Decoding YAML file
    decoded_data = decode_yaml_file(yaml_file_path)
    print("Decoded YAML data:")
    print(decoded_data)
    
    # Encoding decoded data
    encoded_data = encode_yaml_values(decoded_data)
    print("\nEncoded YAML data:")
    print(encoded_data)
    
    # Writing encoded data back to YAML file
    write_yaml_file("encoded_example.yaml", encoded_data)
    print("\nEncoded YAML data written to encoded_example.yaml")
    
    # Writing decoded data back to another YAML file
    write_yaml_file("decoded_example.yaml", decoded_data)
    print(f"\nDecoded YAML data written to decoded_example.yaml")
