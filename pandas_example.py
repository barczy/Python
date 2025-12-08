
import yaml
import pandas as pd

# Load YAML file
with open('data.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Convert to DataFrame (if the structure is tabular)
df = pd.DataFrame(yaml_data)

print(df)
