import importlib
MODEL_NAME = "STUB_MODEL_NAME"
data_loader = importlib.import_module("data_loaders.{}_data".format(MODEL_NAME))
model = importlib.import_module("models.{}_model".format(MODEL_NAME))
import pytorch_lightning as pl

if __name__ == '__main__':
    train_loader, val_loader, test_loader = data_loader.get_data_loaders()
    networks = model.Networks()
    trainer = pl.Trainer()
    trainer.fit(networks, train_loader, val_loader)
    result = trainer.test(test_dataloaders=test_loader)
