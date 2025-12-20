import os
import torch
import argparse
import data_setup, model_builder, engine, utils
from torchvision import transforms

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Train a TinyVGG model.")
    parser.add_argument("--num_epochs", type=int, default=5, help="Number of epochs to train for (default: 5)")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training (default: 32)")
    parser.add_argument("--hidden_units", type=int, default=10, help="Number of hidden units in TinyVGG (default: 10)")
    parser.add_argument("--learning_rate", type=float, default=0.001, help="Learning rate for optimizer (default: 0.001)")
    parser.add_argument("--train_dir", type=str, default="../data/pizza_steak_sushi/train", help="Path to training data")
    parser.add_argument("--test_dir", type=str, default="../data/pizza_steak_sushi/test", help="Path to testing data")
    parser.add_argument("--num_workers", type=int, default=0, help="Number of workers for DataLoader (default: 0)")
    args = parser.parse_args()

    # Setup device
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"[INFO] Using device: {device}")

    # Dynamically set pin_memory
    pin_memory = True if device == "cuda" else False

    # Create transforms
    data_transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor()
    ])

    # Create DataLoaders with help from data_setup.py
    train_dataloader, test_dataloader, class_names = data_setup.create_dataloaders(
        train_dir=args.train_dir,
        test_dir=args.test_dir,
        transform=data_transform,
        batch_size=args.batch_size,
        num_workers=args.num_workers,
    )

    # Create model with help from model_builder.py
    model = model_builder.TinyVGG(
        input_shape=3,
        hidden_units=args.hidden_units,
        output_shape=len(class_names)
    ).to(device)

    # Set loss and optimizer
    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.learning_rate)

    # Start training with help from engine.py
    engine.train(
        model=model,
        train_dataloader=train_dataloader,
        test_dataloader=test_dataloader,
        loss_fn=loss_fn,
        optimizer=optimizer,
        epochs=args.num_epochs,
        device=device
    )

    # Save the model with help from utils.py
    utils.save_model(
        model=model,
        target_dir="../models",
        model_name="05_going_modular_script_mode_tinyvgg_model.pth"
    )

if __name__ == "__main__":
    main()