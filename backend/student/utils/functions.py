def validate_image_file(filename: str) -> bool:
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    return any(filename.endswith(ext) for ext in allowed_extensions)
