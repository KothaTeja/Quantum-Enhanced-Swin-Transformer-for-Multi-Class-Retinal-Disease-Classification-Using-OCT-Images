from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import io
import timm

app = Flask(__name__)
CORS(app)

# ================= CONFIG =================
MODEL_PATH = "final_model (1).pth"
CLASSES = ['AMD','CNV','CSR','DME','DR','DRUSEN','MH','NORMAL']
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ================= QUANTUM SETTINGS =================
n_qubits = 4

# ================= QUANTUM LAYER =================
class QuantumLayer(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(n_qubits))

    def forward(self, x):
        return torch.tanh(x + self.weights)

# ================= MODEL =================
class QuantumSwinTransformer(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.swin = timm.create_model(
            'swin_tiny_patch4_window7_224',
            pretrained=False,
            num_classes=0
        )

        self.fc1 = nn.Linear(self.swin.num_features, n_qubits)
        self.quantum = QuantumLayer()
        self.fc_final = nn.Linear(self.swin.num_features + n_qubits, num_classes)

    def forward(self, x):
        features = self.swin(x)
        q_in = torch.tanh(self.fc1(features))
        q_out = self.quantum(q_in)
        combined = torch.cat((features, q_out), dim=1)
        return self.fc_final(combined)

# ================= LOAD MODEL =================
model = QuantumSwinTransformer(num_classes=8)
state_dict = torch.load(MODEL_PATH, map_location=device)
model.load_state_dict(state_dict)

model.to(device)
model.eval()

# ================= TRANSFORM (IMPROVED 🔥) =================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])   # ⚠️ IMPORTANT FIX
])

# ================= ROUTES =================
@app.route('/')
def home():
    return "Backend Running ✅"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files['file']

    try:
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
    except:
        return jsonify({"error": "Invalid image"})

    img = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img)
        probs = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probs, 1)

    confidence_score = round(confidence.item() * 100, 2)
    predicted_class = CLASSES[predicted.item()]

    # 🔥 Optional threshold (keep or remove)
    if confidence.item() < 0.6:
        predicted_class = "Uncertain"

    return jsonify({
        "class": predicted_class,
        "confidence": confidence_score
    })
# ================= MAIN =================
if __name__ == '__main__':
    app.run(debug=True)