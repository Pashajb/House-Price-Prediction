
from pathlib import Path
from huggingface_hub import hf_hub_download

# Directory where the raw dataset will be stored
data_dir = Path("data/raw")
data_dir.mkdir(parents=True, exist_ok=True)

# Download the dataset from Hugging Face
file_path = hf_hub_download(
    repo_id="divarofficial/real_estate_ads",
    filename="real_estate_ads.csv",
    repo_type="dataset",
    local_dir=data_dir
)

print("\nDownload completed successfully!")
print(f"File location: {file_path}")
