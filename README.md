# Elden Ring Batch Downloader

<p align="center">
  <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/header.jpg" alt="Elden Ring Banner" width="700" />
</p>

<p align="center">
  <b><i>"Arise, Tarnished, and automate your journey to the Lands Between!"</i></b>
</p>

---

<details>
<summary><strong>🛡️ About This Project</strong></summary>

Automate the download of all Elden Ring: Shadow of the Erdtree repack files (FitGirl release) with a single script! This tool uses Selenium and Firefox to batch-download every part from a curated list of URLs, handling popups and ads automatically with uBlock Origin. Perfect for fans who want a hands-off, reliable way to fetch all required files for installation.

</details>

---

## 🎮 Elden Ring Context

Elden Ring is a critically acclaimed action RPG by FromSoftware. The Shadow of the Erdtree expansion is a massive DLC, distributed in large multi-part archives (e.g., FitGirl repack). Downloading all parts manually is tedious and error-prone—this script automates the process, ensuring you get every file needed for extraction and installation.

**Total download size:** ~49GB (102 files)

---

<details>
<summary><strong>🚀 Features (Blessings of Grace)</strong></summary>

- ⚔️ Automated batch downloads from a list of URLs (102 files: 97 main parts + 5 bonus content)
- 🦾 Selenium + Firefox automation (headless or visible)
- 🛡️ uBlock Origin adblocker integration
- 🧙 Handles popups/overlays

</details>

---

<details>
<summary><strong>📦 Download Your Arsenal</strong></summary>

- [Download ZIP of this script and dependencies](https://github.com/briviamoon/Elden-Ring/archive/refs/heads/main.zip)
</details>

---

<details>
<summary><strong>📝 Requirements (Sacred Relics)</strong></summary>

- 🐍 Python 3.8+
- 🐲 [Selenium](https://pypi.org/project/selenium/)
- 🦎 [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (see setup instructions below)
- 🦊 [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)
- 🧩 `ublock_origin.xpi` (uBlock Origin extension, already included in this folder—see notes below)

</details>

---

<details>
<summary><strong>🦎 GeckoDriver Setup Example (Smithing Table)</strong></summary>

1. Go to the [GeckoDriver releases page](https://github.com/mozilla/geckodriver/releases).
2. Download the version matching your OS (e.g., `geckodriver-v0.34.0-win64.zip` for Windows 64-bit).
3. Extract the ZIP file. You will get a file named `geckodriver.exe`.
4. **Add GeckoDriver to your PATH:**
   - Move `geckodriver.exe` to a folder already in your system PATH (e.g., `C:\Windows`), **or**
   - Add the folder containing `geckodriver.exe` to your PATH environment variable:
     - Press `Win + S`, search for "Environment Variables", and open it.
     - Edit the `Path` variable and add the folder path (e.g., `C:\tools\geckodriver`).
   - Open a new terminal and run `geckodriver --version` to confirm it works.

</details>

---

<details>
<summary><strong>🧩 uBlock Origin Extension (Talisman)</strong></summary>

- The required `ublock_origin.xpi` file is already included in this folder. **You do not need to download it again.**
- If you want to update uBlock Origin in the future:
  1. Download the latest `.xpi` from [here](https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi).
  2. Replace the existing `ublock_origin.xpi` in this folder with the new one.
  3. **The file must be named exactly `ublock_origin.xpi` and placed in the same folder as the script.**

</details>

---

## 📂 Files

- `Elden-Ring-Batch.py` — Main script
- `ublock_origin.xpi` — uBlock Origin extension (download manually)
- `Elden-Ring-links.txt` — List of 102 URLs (97 main + 5 bonus)
- `downloads/` — Downloaded files (auto-created)

---

## ⚙️ Setup & Usage

1. **Install Python dependencies:**

   ```sh
   pip install selenium
   ```

2. **Download GeckoDriver:**
   - [Get GeckoDriver here](https://github.com/mozilla/geckodriver/releases)
   - Extract and add to your system PATH.

3. **Download uBlock Origin .xpi:**
   - [Get uBlock Origin .xpi](https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi)
   - Place it in the same folder as the script and rename to `ublock_origin.xpi`.

4. **Edit the URL list:**
   - Edit the `URLS` list in `Elden-Ring-Batch.py` or use your own `.txt` file (default: `Elden-Ring-links.txt` with 103 links).

5. **Run the script:**

   ```sh
   python Elden-Ring-Batch.py
   ```
   - Firefox will open and trigger downloads for each file.
   - The browser will remain open so downloads can finish. Close it manually when all downloads are done.

---

## 🛑 Manual Fallback Instructions

If only a few files are missing or failed to download:

1. Open `Elden-Ring-links.txt` and locate the URLs for the missing parts.
2. Open each link in Firefox (with uBlock Origin or another adblocker enabled).
3. Click the download button manually and save the file to your `downloads/` folder.
4. Ensure the file size matches expectations (most are ~500MB, part098 is ~41MB, bonus part4 is ~427MB).

This is useful if you want to avoid re-running the full batch script for just a few missing files.

---

## ⚠️ Limitations & Flaws

- **Partial file handling:** The script will delete any `.part` file or final file less than 500MB (except for `part098`, which uses a 41MB threshold, and `fg-optional-bonus-content.part4`, which uses a 427MB threshold) before starting a new download for that URL. This ensures only complete files are kept and avoids stuck/incomplete downloads.
- **Special case for part098:** The script treats `part098` as complete if it is at least 41MB. All other parts require at least 500MB to be considered complete, except `fg-optional-bonus-content.part4`, which requires 427MB.
- **No download resumption:** If a download is interrupted or a file is incomplete/corrupted, the script will delete the partial/incomplete file and start a new download for that part on the next run. There is no resume support for partial files.
- **No integrity verification:** The script does not verify if a downloaded file is valid or uncorrupted. It only checks file size.
- **Browser must remain open:** Closing Firefox before downloads finish will interrupt all downloads.

---

## 🛠 Troubleshooting

- If downloads do not start, check that GeckoDriver and Firefox are installed and in your PATH.
- If you see popups or ads, ensure `ublock_origin.xpi` is present.
- If a file is stuck or incomplete, delete it and re-run the script.

---

## 💡 Tips

- You can safely close the terminal after the script finishes; downloads will continue in Firefox.
- To restart failed downloads, delete the incomplete files and run the script again.

---

## 📜 License

This script is provided for educational purposes only. Use responsibly and respect copyright laws.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

---

## 🙏 Acknowledgements

- **FitGirl Repacks** — This script is designed to automate downloads for the Elden Ring: Shadow of the Erdtree repack as distributed by FitGirl Repacks. All credit for the repack, file structure, and distribution goes to FitGirl and their team. Please support original creators and the FitGirl community for their dedication to high-quality, accessible game repacks.

---

## ⭐️ Enjoy your journey in the Lands Between!
