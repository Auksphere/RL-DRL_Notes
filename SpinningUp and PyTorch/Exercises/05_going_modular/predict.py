import argparse
import torch
from torchvision import transforms
from PIL import Image
import model_builder
import os

def load_model(model_path, input_shape, hidden_units, output_shape, device):
    """Load a trained model from a file."""
    model = model_builder.TinyVGG(
        input_shape=input_shape,
        hidden_units=hidden_units,
        output_shape=output_shape
    ).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    return model

def predict_image(image_path, model, class_names, transform, device):
    """Predict the class of an image using a trained model."""
    # Load the image
    image = Image.open(image_path).convert("RGB")
    
    # Apply the transformations
    transformed_image = transform(image).unsqueeze(0).to(device)  # Add batch dimension
    
    # Set the model to evaluation mode
    model.eval()
    
    # Perform inference
    with torch.inference_mode():
        outputs = model(transformed_image)
        predicted_class = torch.argmax(outputs, dim=1).item()
    
    return class_names[predicted_class]

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Predict the class of an image using a trained TinyVGG model.")
    parser.add_argument("--image", type=str, required=True, help="Path to the image to predict.")
    parser.add_argument("--model_path", type=str, default="../models/05_going_modular_script_mode_tinyvgg_model.pth", help="Path to the trained model.")
    parser.add_argument("--class_names", type=str, nargs="+", default=["pizza", "steak", "sushi"], help="List of class names.")
   
    args = parser.parse_args()

    # Setup device
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"[INFO] Using device: {device}")

    # Define image transformations
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor()
    ])

    hidden_units = 128
    # Load the model
    model = load_model(
        model_path=args.model_path,
        input_shape=3,
        hidden_units=hidden_units,
        output_shape=len(args.class_names),
        device=device
    )

    # Predict the class of the image
    predicted_class = predict_image(
        image_path=args.image,
        model=model,
        class_names=args.class_names,
        transform=transform,
        device=device
    )

    print(f"[INFO] Predicted class: {predicted_class}")

if __name__ == "__main__":
    main()