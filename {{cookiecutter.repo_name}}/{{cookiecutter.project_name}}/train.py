import numpy as np

import torch
import pytorch_lightning as pl

import hydra

from src.models.dqn import DQNModel


@hydra.main(config_path='configs', config_name='config')
def main(hparams):
    torch.manual_seed(hparams.pytorch_seed)
    model = DQNModel(hparams)
    trainer = pl.Trainer(max_epochs=10000, val_check_interval=100)
    trainer.fit(model)


if __name__ == '__main__':
    torch.manual_seed(0)
    np.random.seed(0)
    main()
