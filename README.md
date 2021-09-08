# Summary
This is a project to illustrate how to pytorch-lightening to architecture a training pipeline for multiple projects.

# Pre-requisites

1. A machine with NVIDIA GPU
2. The below is only tested on an Ubuntu machine. Not sure whether it works for Windows/MacOS
3. Install [NVIDIA docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

# Run Examples

1. Build the docker images: `make build`
2. Run the container: `make run`
3. Run the training: `python run.py run --model_name=example`

Then you shall see the data downloading is automatically happening and the training is going on:
```
Creating starter according to model name ....
Starter created!
Run the training!
Global seed set to 1234
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to MNIST/raw/train-images-idx3-ubyte.gz
9913344it [00:01, 8681839.59it/s]                                                                                                                                               
Extracting MNIST/raw/train-images-idx3-ubyte.gz to MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to MNIST/raw/train-labels-idx1-ubyte.gz
29696it [00:00, 9765115.77it/s]                                                                                                                                                 
Extracting MNIST/raw/train-labels-idx1-ubyte.gz to MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to MNIST/raw/t10k-images-idx3-ubyte.gz
1649664it [00:00, 8366687.88it/s]                                                                                                                                               
Extracting MNIST/raw/t10k-images-idx3-ubyte.gz to MNIST/raw

......

GPU available: True, used: False
TPU available: False, using: 0 TPU cores
IPU available: False, using: 0 IPUs
/usr/local/lib/python3.6/dist-packages/pytorch_lightning/trainer/trainer.py:1293: UserWarning: GPU available but not used. Set the gpus flag in your trainer `Trainer(gpus=1)` or script `--gpus=1`.
  "GPU available but not used. Set the gpus flag in your trainer"
/usr/local/lib/python3.6/dist-packages/pytorch_lightning/trainer/configuration_validator.py:99: UserWarning: you passed in a val_dataloader but have no validation_step. Skipping val loop
  rank_zero_warn(f"you passed in a {loader_name} but have no {step_name}. Skipping {stage} loop")
  | Name    | Type       | Params
---------------------------------------
0 | encoder | Sequential | 50.4 K
1 | decoder | Sequential | 51.2 K
---------------------------------------
101 K     Trainable params
0         Non-trainable params
101 K     Total params
0.407     Total estimated model params size (MB)
/usr/local/lib/python3.6/dist-packages/pytorch_lightning/trainer/data_loading.py:106: UserWarning: The dataloader, train dataloader, does not have many workers which may be a bottleneck. Consider increasing the value of the `num_workers` argument` (try 16 which is the number of cpus on this machine) in the `DataLoader` init to improve performance.
  f"The dataloader, {name}, does not have many workers which may be a bottleneck."
Epoch 57:  97%|##################################################################################################7   | 1665/1719 [00:07<00:00, 224.37it/s, loss=0.0375, v_num=0]

```

# Write Another Model Training Pipeline

1. Come up with a proper name, denoting as `${model_name}`, such as `${task}_${version}`...
2. Create an `${model_name}_data.py` under [src/data_loaders](src/data_loaders)
3. Create an `${model_name}_model.py` under [src/models](src/models)
4. Work on those two modules
5. Test the training: `python run.py run --model_name=${model_name}`

# TODOs

- [ ] Add customized configs
- [ ] Add large scale data management
- [ ] Add support for unit-tests
- [ ] Add support for Horovod distributed training
- [ ] Add support for cloud training platform integrations