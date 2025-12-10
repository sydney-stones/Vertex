# Authentication Required - Final Setup Step

## 🚨 You're Almost There!

Everything is set up correctly, but you need to authenticate with Google Cloud to use the Vertex AI API.

## ✅ What's Already Done

- ✅ Project ID: renderedfitsnew
- ✅ Python environment and dependencies
- ✅ Your images are ready:
  - `input_images/person/model.png` (1.4 MB)
  - `input_images/clothing/outfit.png` (564 KB)
- ✅ Code is ready to run

## 🔐 What You Need to Do: Authenticate

### Option 1: Using Google Cloud CLI (Recommended)

#### Step 1: Install gcloud CLI

**macOS:**
```bash
# Using Homebrew (easiest)
brew install google-cloud-sdk

# OR download installer
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

**Download Link:**
https://cloud.google.com/sdk/docs/install

#### Step 2: Authenticate

After installing gcloud:

```bash
# Login to your Google account
gcloud auth login

# Set up application default credentials (THIS IS REQUIRED)
gcloud auth application-default login

# Set your project
gcloud config set project renderedfitsnew

# Enable the Vertex AI API
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

#### Step 3: Run Virtual Try-On!

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the script
python run_my_tryon.py
```

### Option 2: Using Service Account (Alternative)

If you can't install gcloud CLI, you can use a service account:

#### Step 1: Create Service Account
1. Go to: https://console.cloud.google.com/iam-admin/serviceaccounts?project=renderedfitsnew
2. Click "Create Service Account"
3. Name it: `virtual-tryon-sa`
4. Grant role: **Vertex AI User**
5. Click "Done"

#### Step 2: Create Key
1. Click on the service account you just created
2. Go to "Keys" tab
3. Click "Add Key" → "Create new key"
4. Choose JSON format
5. Save the file to this directory as `service-account-key.json`

#### Step 3: Set Environment Variable
```bash
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/service-account-key.json"
```

#### Step 4: Enable API
1. Go to: https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=renderedfitsnew
2. Click "Enable"

#### Step 5: Run Virtual Try-On
```bash
source venv/bin/activate
python run_my_tryon.py
```

## 🎯 Quick Commands Summary

**Recommended Method (gcloud CLI):**
```bash
# Install gcloud CLI first, then:
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew

# Then run:
source venv/bin/activate
python run_my_tryon.py
```

**Service Account Method:**
```bash
# After creating and downloading service account key:
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/service-account-key.json"
source venv/bin/activate
python run_my_tryon.py
```

## 📋 Verification

After authenticating, verify it worked:

```bash
source venv/bin/activate
python check_setup.py
```

You should see:
```
✅ Check 6: Authentication working!
   → Connected to Vertex AI
```

## 🎬 What Happens Next

Once authenticated, the script will:

1. ✅ Load your person image (`model.png`)
2. ✅ Load your outfit image (`outfit.png`)
3. 🔄 Send to Google's Virtual Try-On API (takes ~10-30 seconds)
4. 💾 Save result to `output_images/tryon_TIMESTAMP.jpeg`
5. ✅ Show success message with file path

## 💰 Billing Note

Make sure billing is enabled on your project:
https://console.cloud.google.com/billing/projects

Virtual Try-On costs a few cents per image generated.

## 🆘 Troubleshooting

### "gcloud: command not found"
- gcloud CLI is not installed
- Install from: https://cloud.google.com/sdk/docs/install

### "API not enabled"
```bash
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

### "Permission denied"
- Make sure you're logged into the correct Google account
- Verify you have Owner or Editor role on the project
- Check: https://console.cloud.google.com/iam-admin/iam?project=renderedfitsnew

### "Billing not enabled"
- Enable billing: https://console.cloud.google.com/billing

## 🔗 Useful Links

- **Install gcloud CLI:** https://cloud.google.com/sdk/docs/install
- **Set up ADC:** https://cloud.google.com/docs/authentication/provide-credentials-adc
- **Project Console:** https://console.cloud.google.com/home/dashboard?project=renderedfitsnew
- **Enable Vertex AI:** https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=renderedfitsnew
- **Billing:** https://console.cloud.google.com/billing

## ✅ Once You're Authenticated

You'll be able to:

1. Run `python run_my_tryon.py` to try on your outfit
2. Generate multiple variations with different settings
3. Try on multiple clothing items sequentially
4. Use any of the example scripts

---

**Choose your authentication method above and you'll be ready to go in 5 minutes!** 🚀
