from torch.utils.data import DataLoader
import pytorch_lightning as pl
from torch.utils.data import random_split
from torchvision import transforms

pl.seed_everything(1234)


def get_data_loaders(batch_size=32):
    from torchvision.datasets.mnist import MNIST
    dataset = MNIST('', train=True, download=True, transform=transforms.ToTensor())
    mnist_test = MNIST('', train=False, download=True, transform=transforms.ToTensor())
    mnist_train, mnist_val = random_split(dataset, [55000, 5000])
    train_loader = DataLoader(mnist_train, batch_size=batch_size)
    val_loader = DataLoader(mnist_val, batch_size=batch_size)
    test_loader = DataLoader(mnist_test, batch_size=batch_size)
    return train_loader, val_loader, test_loader
