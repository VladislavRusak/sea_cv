import json
import os

def load_config(config_file='config.json'):
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    return config