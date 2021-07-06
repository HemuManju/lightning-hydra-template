from hydra.experimental import compose, initialize
from utils import skip_run

# Initialize the config directory
initialize(config_path="configs", job_name="learning")

with skip_run('skip', 'split_image_folder') as check, check():
    hparams = compose(config_name="config")
    raise NotImplementedError
