# 🚀 Launch Virtual Try-On Web Interface

## Super Simple - Just One Command!

```bash
./launch_ui.sh
```

That's it! The web interface will open in your browser at:
**http://127.0.0.1:7860**

---

## 📸 What You'll See

A beautiful web interface with:
- **Drag & drop** for uploading images
- **Live preview** of your uploads
- **Click to generate** button
- **Real-time progress** bar
- **Instant results** displayed

No more typing commands! Just:
1. Upload person image
2. Upload clothing image
3. Click generate
4. Wait ~15 seconds
5. See result!

---

## 🎯 Quick Usage

### Single Item Try-On
```
1. Launch: ./launch_ui.sh
2. Upload person image (left side)
3. Upload clothing image (right side)
4. Click "✨ Generate Virtual Try-On"
5. View result!
```

### Multiple Items Try-On
```
1. Switch to "Multiple Items" tab
2. Upload person image
3. Upload 2-3 clothing items
4. Click "✨ Generate Sequential Try-On"
5. View complete outfit!
```

---

## ⚙️ Features

### 📤 Easy Uploads
- Drag & drop images
- Or click to browse
- Support for webcam (person images)
- Multiple file upload (for outfits)

### 🎨 Customizable
- Generate 1-4 variations
- Adjust safety filters
- See real-time progress
- Automatic saving

### 💾 Organized Output
- All results saved to `output_images/`
- Timestamped filenames
- Status shows save location

---

## 🔐 Authentication Status

**If you see "Authentication Required" warning:**

```bash
# Stop the app (Ctrl+C)
# Then run:
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew

# Restart:
./launch_ui.sh
```

**If you see "✅ Connected to Vertex AI":**
You're all set! Start uploading images.

---

## 🎬 Video Walkthrough

**Step 1: Launch**
```bash
./launch_ui.sh
```
Wait for "Running on http://127.0.0.1:7860"

**Step 2: Open Browser**
The interface opens automatically, or go to:
http://127.0.0.1:7860

**Step 3: Upload Images**
- Click or drag person image to left box
- Click or drag clothing image to right box

**Step 4: Generate**
Click the big "✨ Generate Virtual Try-On" button

**Step 5: Wait**
Watch the progress bar (~15 seconds)

**Step 6: View Result**
Your virtual try-on appears on the right!

**Step 7: Save (Automatic)**
Image is already saved in `output_images/`
Path shown in status box

---

## 📱 Interface Tabs

### Tab 1: Single Item Try-On
- Try on one clothing item
- Generate 1-4 variations
- Fastest option

### Tab 2: Multiple Items Try-On
- Complete outfits (shirt + pants + shoes)
- Sequential processing
- Takes longer but worth it!

### Tab 3: About & Help
- Supported clothing types
- Troubleshooting tips
- Cost information
- Project links

---

## 🛑 Stopping the Interface

Press **Ctrl+C** in the terminal where it's running.

---

## 🔄 Restarting

```bash
./launch_ui.sh
```

The launcher handles everything:
- ✅ Activates virtual environment
- ✅ Checks dependencies
- ✅ Verifies authentication
- ✅ Starts the server
- ✅ Opens your browser

---

## 💡 Pro Tips

### For Best Results
- Use high-res images (1024x1024+)
- Ensure good lighting
- Person facing forward
- Clear clothing images

### For Speed
- Generate 1 image first
- Use smaller images initially
- Test with samples first

### For Multiple Variations
- Set slider to 2, 3, or 4
- Pick the best result
- Each variation costs the same!

---

## 🆘 Common Issues

### "Port already in use"
```bash
# Kill existing process
lsof -i :7860
kill -9 <PID>

# Relaunch
./launch_ui.sh
```

### "Module not found"
```bash
source venv/bin/activate
pip install -r requirements.txt
./launch_ui.sh
```

### "Authentication failed"
```bash
gcloud auth application-default login
./launch_ui.sh
```

### Interface is slow
- This is normal! AI takes time
- Single item: 10-30 seconds
- Multiple items: 30-90 seconds
- Be patient ☺️

---

## 📂 Where Are My Images?

**Uploaded images:** Temporary (auto-deleted)

**Generated images:**
```
output_images/
├── tryon_20251210_120530_0.jpeg
├── tryon_20251210_121045_0.jpeg
└── ...
```

**Open folder:**
```bash
open output_images/
```

---

## 🌐 Access from Other Devices

**Want to use from phone or tablet?**

Edit [app.py](app.py), line 522:
```python
server_name="0.0.0.0",  # Change from 127.0.0.1
```

Then access from any device on your network:
```
http://YOUR_COMPUTER_IP:7860
```

---

## 💰 Cost Tracking

Each generation = 1 API call (even for 4 variations!)

Monitor usage:
https://console.cloud.google.com/billing

Typical cost: Few cents per generation

---

## 📖 More Help

- **Full UI Guide:** [UI_GUIDE.md](UI_GUIDE.md)
- **Setup Issues:** [AUTHENTICATION_REQUIRED.md](AUTHENTICATION_REQUIRED.md)
- **Complete Docs:** [README.md](README.md)

---

## ✨ Ready to Go!

Launch the interface:
```bash
./launch_ui.sh
```

Upload your images and create amazing virtual try-ons! 🎨👔

No coding required. No terminal commands. Just point, click, and generate! 🚀
