# 🍼 Baby Cry Sound Classification

A deep learning project to classify baby crying sounds into different emotional or situational categories using spectrograms of audio data. The models are trained to detect the reason for a baby's cry — like hunger, discomfort, tiredness, or pain — and are aimed to be part of an intelligent baby monitoring system.

---

## 📂 Dataset

- **Format**: `.npy` files representing mel-spectrograms of baby crying audio clips.
- **Preprocessing**: Normalized and converted to RGB images.
- **Classes**: (examples)
  - `belly_pain`, `burping`, `discomfort`, `hungry`, `noise`, `tired`, `laugh`, `cold_hot`, `silence`

- **Structure**:
  ```
  baby_cry_split/
  ├── train/
  ├── val/
  └── test/
  ```

---

## 🧠 Models Compared

### ✅ 1. YAMNet + Feedforward Classifier [🏆 Best Accuracy: 65% on Test Set]

- Based on Google’s YAMNet model (trained on AudioSet)
- Extracts 1024-dimensional embeddings from audio
- Feed-forward classifier head with:
  - Dropout
  - BatchNorm
  - Fully Connected layers
- **Test Accuracy**: 0.65
- **Best generalization performance**

### 2. Base CNN

- 3 Convolutional layers + MaxPooling
- Dropout + BatchNorm
- Custom classifier with 256 hidden units
- Input: 128×128 RGB images

### 3. ResNet-18

- Pretrained backbone (frozen)
- Custom head with dropout
- Strong data augmentation + label smoothing
- Used `class_weight` for imbalanced data
- Input: 224×224

### 4. ResNet-50

- Pretrained ResNet-50 with fine-tuning on deeper layers
- Added dropout and weight decay
- Best deep model after YAMNet

### 5. EfficientNet-B0

- Pretrained EfficientNet with fine-tuned blocks 4–7
- Used Mixup data augmentation
- Optimized with `AdamW` + scheduler
- Input: 224×224

### 6. MobileNetV3-Large

- Lightweight CNN for fast inference
- Strong augmentations and dropout
- Works well on smaller datasets
- Input: 224×224

---

## 🏋️‍♂️ Training Setup

| Setting                | Value              |
|------------------------|--------------------|
| Optimizer              | Adam / AdamW       |
| Loss Function          | CrossEntropyLoss (with optional label smoothing and class weights) |
| Learning Rate          | 1e-3 to 3e-5        |
| Regularization         | Dropout (0.3–0.6), Weight Decay |
| Batch Size             | 16 / 32 / 64       |
| Scheduler              | ReduceLROnPlateau  |
| Early Stopping         | Patience = 5–7     |

---

## 📈 Evaluation Metrics

All models were evaluated on a separate **test set** using:

- **Accuracy**
- **Precision, Recall, F1-Score**
- **Confusion Matrix**
- **Loss / Accuracy Curves**

Example:

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Assume y_true and y_pred are populated from model predictions
print(classification_report(y_true, y_pred, target_names=class_names))

cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=True, xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix")
plt.show()
```

---

## 📊 Results Summary

| Model              | Val Acc (%) | Test Acc (%) | Best Feature               |
|-------------------|-------------|--------------|----------------------------|
| **YAMNet + FC**    | 64.2        | **65.0**     | Pretrained embeddings      |
| ResNet-50          | 43–44       | 40.0         | Deeper layers, fine-tuned  |
| EfficientNet-B0    | 41.2        | 40.5         | Mixup + lightweight        |
| MobileNetV3-Large  | 40.6        | 40.0         | Fast inference             |
| ResNet-18          | 43.8        | 43.0         | Label smoothing + dropout  |
| Base CNN           | 40.5        | 40.0         | Basic CNN with dropout     |

---

## 🗃️ Output Files

- `best_model.pth` – Best model weights
- `confusion_matrix.png`
- `train_val_accuracy_loss.png`
- `classification_report.txt`

---

## 📦 Requirements

```bash
pip install torch torchvision torchaudio numpy matplotlib seaborn scikit-learn
```

YAMNet requires:
```bash
pip install tensorflow tensorflow_hub
```

---

## 🚀 Running the Code

Each model is implemented in its own notebook or script:
- `baby_classification_cnn.ipynb`
- `baby_classification_yammnet.ipynb`

Make sure your data is structured under `/content/baby_cry_split/` as described earlier.

---

## 📌 Notes

- Early stopping helps prevent overfitting
- Mixup worked well with EfficientNet
- Pretrained audio embeddings (YAMNet) clearly outperformed image-only methods