import yaml

with open('config.yml') as f:
    config_file = yaml.load(f, Loader=yaml.FullLoader)