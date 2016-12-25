import json
import glob
import sys

def load(config_file="config.json"):
    """
    :param config_file (str): name of configuration file
    :return:
      data ([str, str,,,]): list of law text data
      target ([int, int,,,]): list of class index
    """
    with open(config_file, 'r') as f:
        config = json.load(f)

    base_directory = config['base_directory']
    number_of_classes = config['number_of_classes']
    target_names = config['targets']

    data = []
    target = []
    class_id = 0
    for category in target_names:
        target_dir = base_directory + "/" + category
        target_files = target_dir + "/*.txt"
        filenames = glob.glob(target_files)
        for filename in filenames:
            with open(filename, 'r') as f:
                data.append(f.read())
                target.append(class_id)
        class_id = class_id + 1
    if number_of_classes != class_id:
        print("load() failed. config_file(" + config_file + ") had something wrong.")
        sys.exit(0)

    return data, target, target_names
