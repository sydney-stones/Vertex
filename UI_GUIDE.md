# 🎨 Virtual Try-On Web Interface Guide

## Easy-to-Use Visual Interface!

No more terminal commands! Use the beautiful web interface to upload images and generate virtual try-ons with just a few clicks.

---

## 🚀 Quick Start

### Step 1: Install Gradio (if needed)

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Launch the Web Interface

**Option A: Use the launcher script (easiest)**
```bash
./launch_ui.sh
```

**Option B: Run directly**
```bash
source venv/bin/activate
python app.py
```

### Step 3: Open in Browser

The interface will automatically open at:
```
http://127.0.0.1:7860
```

Or click the link in the terminal output.

---

## 🎯 How to Use the Interface

### Tab 1: Single Item Try-On

Perfect for trying on one clothing item at a time.

**Steps:**
1. **Upload Person Image** - Click or drag & drop your model image
2. **Upload Clothing Item** - Add the clothing you want to try on
3. **Adjust Settings** (optional):
   - Number of Variations: 1-4 images
   - Safety Filter Level: Content filtering
4. **Click "Generate Virtual Try-On"**
5. **Wait** ~10-30 seconds
6. **View Result** - The generated image appears on the right!

**Features:**
- 📷 Upload from computer or use webcam
- 🎲 Generate up to 4 variations at once
- ⚙️ Adjustable safety filters
- 📥 Results automatically saved to `output_images/`

### Tab 2: Multiple Items Try-On

Try on complete outfits (shirt + pants + shoes) sequentially.

**Steps:**
1. **Upload Person Image**
2. **Upload Multiple Clothing Items** - Select 2-3 items
   - They will be applied in the order you upload them
   - Example: shirt.jpg, then pants.jpg, then shoes.jpg
3. **Adjust Safety Filter** (optional)
4. **Click "Generate Sequential Try-On"**
5. **Wait** ~30-60 seconds (depends on number of items)
6. **View Final Result** - See the complete outfit!

**How it works:**
- Item 1 → Try on person → Result A
- Item 2 → Try on Result A → Result B
- Item 3 → Try on Result B → Final Result

### Tab 3: About & Help

Contains:
- Supported clothing types
- Cost information
- Troubleshooting guide
- Project info and links

---

## 🎨 Interface Features

### ✨ Beautiful Design
- Clean, modern interface
- Easy drag-and-drop uploads
- Real-time status updates
- Progress indicators

### 📱 User-Friendly
- No coding required
- No terminal commands
- Visual feedback
- Clear error messages

### 🎛️ Customizable Settings
- Number of variations (1-4)
- Safety filter levels
- Support for webcam input
- Multiple file uploads

### 💾 Automatic Saving
- All results saved to `output_images/`
- Timestamped filenames
- View status shows save location

---

## 📸 Screenshot Tour

**Main Interface:**
```
┌─────────────────────────────────────────────────────────────────┐
│  👔 Virtual Try-On with Google Vertex AI                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [Single Item] [Multiple Items] [About & Help]                 │
│                                                                 │
│  Person Image          │         Clothing Item                 │
│  ┌─────────────┐       │       ┌─────────────┐                │
│  │             │       │       │             │                 │
│  │  Upload or  │       │       │  Upload     │                 │
│  │  Drag Here  │       │       │  Image      │                 │
│  │             │       │       │             │                 │
│  └─────────────┘       │       └─────────────┘                │
│                                                                 │
│  Number of Variations: [▓▓▓░░░] 1-4                           │
│  Safety Level: [BLOCK_LOW_AND_ABOVE ▼]                        │
│                                                                 │
│         [✨ Generate Virtual Try-On]                           │
│                                                                 │
│  Result:                                                        │
│  ┌───────────────────────────────────────┐                    │
│  │                                       │                     │
│  │     Generated image appears here     │                     │
│  │                                       │                     │
│  └───────────────────────────────────────┘                    │
│                                                                 │
│  Status: ✅ Success! Generated 1 image(s).                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💡 Tips for Best Results

### Person Images
- ✅ Face forward, full body visible
- ✅ Good lighting, clear image
- ✅ Neutral pose works best
- ✅ High resolution (1024x1024+)
- ❌ Avoid dark or blurry images
- ❌ Avoid extreme angles

### Clothing Images
- ✅ Clear view of the item
- ✅ Well-lit, product photo quality
- ✅ Plain or simple background
- ✅ High resolution
- ❌ Avoid cluttered backgrounds
- ❌ Avoid partial views

### Sequential Try-On
- Try tops before bottoms
- Try larger items before accessories
- Limit to 2-3 items for best results
- Upload in the order you want them applied

---

## ⚙️ Settings Explained

### Number of Variations
- **1** - Single result (fastest, cheapest)
- **2-4** - Multiple variations (more options, costs more)

Use multiple variations when:
- You want different poses/angles
- You want to pick the best result
- You're testing the system

### Safety Filter Level

**BLOCK_LOW_AND_ABOVE** (Default - Most Restrictive)
- Blocks most potentially sensitive content
- Recommended for production/public use

**BLOCK_MEDIUM_AND_ABOVE**
- Blocks moderate and high-risk content
- Balanced filtering

**BLOCK_ONLY_HIGH**
- Only blocks high-risk content
- Less restrictive

**BLOCK_NONE**
- No content filtering
- Use with caution

---

## 🔧 Troubleshooting

### "Authentication Required" Warning

**Problem:** Red warning box appears at the top

**Solution:**
```bash
# In a terminal:
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew

# Then restart the app:
./launch_ui.sh
```

### "Error: Credentials not found"

**Problem:** Generation fails with authentication error

**Solution:** Same as above - authenticate first, then restart

### Interface Won't Load

**Problem:** Browser shows connection error

**Solution:**
```bash
# Check if port 7860 is in use
lsof -i :7860

# Kill any existing process
kill -9 <PID>

# Restart the app
./launch_ui.sh
```

### Slow Generation

**Problem:** Takes a long time to generate

**This is normal:**
- Single item: 10-30 seconds
- Multiple items: 30-60+ seconds
- Depends on API load and image size

**Tips:**
- Use smaller images (1024x1024 or 2048x2048)
- Be patient - quality takes time
- Check your internet connection

### Poor Quality Results

**Solutions:**
1. Use higher resolution images
2. Ensure good lighting in source images
3. Try different safety filter levels
4. Generate multiple variations and pick the best
5. Make sure person is facing forward

### "API not enabled" Error

**Solution:**
```bash
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

---

## 🌐 Accessing the Interface

### Local Access (Default)
```
http://127.0.0.1:7860
```
Only accessible from your computer.

### Network Access (Optional)

To allow access from other devices on your network:

Edit `app.py`, line ~522:
```python
app.launch(
    server_name="0.0.0.0",  # Change from 127.0.0.1
    server_port=7860,
    share=False
)
```

Then access from other devices using:
```
http://YOUR_COMPUTER_IP:7860
```

### Public Access (Optional)

For temporary public link:

Edit `app.py`, line ~522:
```python
app.launch(
    share=True,  # Creates a public gradio.live link
    server_port=7860
)
```

⚠️ **Warning:** Public links expire in 72 hours and share your interface with anyone who has the link.

---

## 📂 File Organization

The web interface automatically organizes files:

```
Vertex/
├── app.py                    # Web interface code
├── launch_ui.sh              # Launcher script
├── input_images/             # Your uploaded images
│   ├── person/
│   └── clothing/
├── output_images/            # Generated results
│   ├── tryon_20251210_120530_0.jpeg
│   ├── tryon_20251210_120645_0.jpeg
│   └── ...
└── temp_*.png                # Temporary files (auto-deleted)
```

---

## 🎬 Workflow Example

### Example 1: Single Item
1. Launch: `./launch_ui.sh`
2. Open: http://127.0.0.1:7860
3. Upload person image
4. Upload shirt image
5. Click "Generate"
6. Wait 15 seconds
7. View result!
8. Find saved file in `output_images/`

### Example 2: Complete Outfit
1. Launch interface
2. Switch to "Multiple Items" tab
3. Upload person image
4. Upload 3 items: shirt, pants, shoes
5. Click "Generate Sequential Try-On"
6. Wait 45 seconds
7. See complete outfit!

---

## 💰 Cost Tracking

Each generation uses the Vertex AI API:
- **Single item:** ~1 API call
- **Multiple items (3):** ~3 API calls
- **4 variations:** ~1 API call (generates 4 images)

Monitor costs at:
https://console.cloud.google.com/billing

---

## 🆘 Need Help?

### In the Interface
- Check the "About & Help" tab
- Read error messages carefully
- Try the tips section

### In Documentation
- [README.md](README.md) - Full documentation
- [FINAL_SUMMARY.md](FINAL_SUMMARY.md) - Complete overview
- [AUTHENTICATION_REQUIRED.md](AUTHENTICATION_REQUIRED.md) - Auth help

### Common Commands
```bash
# Check authentication
python check_setup.py

# View logs
tail -f output_images/*.log

# Restart interface
./launch_ui.sh
```

---

## 🎉 Advantages of the Web UI

### vs. Terminal Commands
- ✅ No typing commands
- ✅ Visual feedback
- ✅ Easier to use
- ✅ Better for non-technical users
- ✅ Real-time preview
- ✅ Drag-and-drop uploads

### vs. Python Scripts
- ✅ No coding required
- ✅ Instant results
- ✅ Easy to share with others
- ✅ Mobile-friendly
- ✅ Better error handling

---

## 📱 Sharing with Others

To let others use your interface:

### Option 1: Local Network
1. Edit `app.py` to use `server_name="0.0.0.0"`
2. Share your IP address
3. They access: `http://YOUR_IP:7860`

### Option 2: Public Link
1. Edit `app.py` to use `share=True`
2. Share the gradio.live link
3. Link expires in 72 hours

### Option 3: Deploy to Cloud
- Deploy to Google Cloud Run
- Deploy to Hugging Face Spaces
- Deploy to your own server

---

## 🎯 Quick Reference

| Action | Command |
|--------|---------|
| **Launch UI** | `./launch_ui.sh` |
| **Stop UI** | Press `Ctrl+C` in terminal |
| **Access** | http://127.0.0.1:7860 |
| **Check Status** | `python check_setup.py` |
| **View Output** | `open output_images/` |
| **Restart** | `Ctrl+C` then `./launch_ui.sh` |

---

## 🚀 You're Ready!

Start the interface and enjoy the visual experience:

```bash
./launch_ui.sh
```

Then open your browser and start trying on clothes! 👔✨

---

**Questions?** Check the other documentation files or the "About & Help" tab in the interface.

Happy try-on! 🎨
