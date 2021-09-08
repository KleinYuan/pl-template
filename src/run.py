import subprocess
import fire


def create_starter(model_name):
    print("Creating starter according to model name ....")
    command = '''sed "s|STUB_MODEL_NAME|{}|g" train_template.py>train.py'''.format(model_name)
    subprocess.call(command, shell=True)
    print("Starter created!")


def clean_up(model_name):
    print("Clean up!")
    command = '''rm -rf train.py '''.format(model_name)
    subprocess.call(command, shell=True)


def run_training(model_name):
    print("Run the training!")
    command = '''python train.py '''.format(model_name)
    subprocess.call(command, shell=True)


def run(model_name):
    create_starter(model_name)
    run_training(model_name)
    clean_up(model_name)


if __name__ == '__main__':
    fire.Fire()
