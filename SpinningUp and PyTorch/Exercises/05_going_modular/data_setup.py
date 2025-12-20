import os
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def create_dataloaders(
        train_dir:str,
        test_dir:str,
        transform:transforms.Compose,
        batch_size:int,
        num_workers:int=0
):
    
    train_data = datasets.ImageFolder(root=train_dir,
                                  transform=transform)

    test_data = datasets.ImageFolder(root=test_dir,
                                  transform=transform)
    
    class_names = train_data.classes

  # Turn images into data loaders
    train_dataloader = DataLoader(
        train_data,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=False,
    )
    test_dataloader = DataLoader(
        test_data,
        batch_size=batch_size,
        shuffle=False, # don't need to shuffle test data
        num_workers=num_workers,
        pin_memory=False,
    )

    return train_dataloader, test_dataloader, class_names