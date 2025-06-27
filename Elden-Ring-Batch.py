#!/usr/bin/env python3
"""
Automate downloading files by visiting URLs and clicking
the download button with Selenium and Firefox (GeckoDriver).

Requirements:
- selenium package
- GeckoDriver installed and in your PATH
- Firefox browser installed

This script:
- Reads URLs from a list
- Opens each URL in headless Firefox
- Waits for a button with id "downloadButton" (change if needed)
- Clicks the button to start the download
- Downloads files automatically into the specified folder
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")

URLS = [
    "https://fuckingfast.co/v8jb5nm593lc#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part000.rar",
    "https://fuckingfast.co/v8jb5nm593lc#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part001.rar",
    "https://fuckingfast.co/ghg83mmugqyv#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part002.rar",
    "https://fuckingfast.co/5tn6hnn3tfxu#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part003.rar",
    "https://fuckingfast.co/727ng7vftrmv#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part004.rar",
    "https://fuckingfast.co/hb06pol224b2#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part005.rar",
    "https://fuckingfast.co/nrydtm371iya#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part006.rar",
    "https://fuckingfast.co/ni5exqfgvvef#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part007.rar",
    "https://fuckingfast.co/z3ha8fixj94p#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part008.rar",
    "https://fuckingfast.co/9sw8qxi4nx44#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part009.rar",
    "https://fuckingfast.co/22m7qw5t9z4s#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part010.rar",
    "https://fuckingfast.co/u4kagwzo9xc4#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part011.rar",
    "https://fuckingfast.co/08vbghmmgzgo#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part012.rar",
    "https://fuckingfast.co/b2594pm3b6ox#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part013.rar",
    "https://fuckingfast.co/4vk1fd34ktbh#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part014.rar",
    "https://fuckingfast.co/1h286bmn3d78#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part015.rar",
    "https://fuckingfast.co/vfyfeipeexqa#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part016.rar",
    "https://fuckingfast.co/fx18d4gdnyl4#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part017.rar",
    "https://fuckingfast.co/j1tu7qfgbsje#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part018.rar",
    "https://fuckingfast.co/4vss56l5yh69#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part019.rar",
    "https://fuckingfast.co/c0zwqzvgdsli#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part020.rar",
    "https://fuckingfast.co/zk3ozovj7j3z#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part021.rar",
    "https://fuckingfast.co/p9043wt8nx9a#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part022.rar",
    "https://fuckingfast.co/cdvvjbp7q5yi#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part023.rar",
    "https://fuckingfast.co/afme8vlaajhe#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part024.rar",
    "https://fuckingfast.co/1yqpci07n6ci#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part025.rar",
    "https://fuckingfast.co/znsmcsqeotj8#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part026.rar",
    "https://fuckingfast.co/fxp1vhpn207y#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part027.rar",
    "https://fuckingfast.co/dlaftqx0jmdy#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part028.rar",
    "https://fuckingfast.co/q9uov7m09bmy#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part029.rar",
    "https://fuckingfast.co/4rbzvpb11184#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part030.rar",
    "https://fuckingfast.co/2q65actmvgl0#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part031.rar",
    "https://fuckingfast.co/cptsykps0nlt#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part032.rar",
    "https://fuckingfast.co/zyc9ixuvllml#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part033.rar",
    "https://fuckingfast.co/qdxpkofbnveu#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part034.rar",
    "https://fuckingfast.co/m4fl4w0eh5oh#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part035.rar",
    "https://fuckingfast.co/rya8s11k8l1h#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part036.rar",
    "https://fuckingfast.co/gotq1w44p1xl#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part037.rar",
    "https://fuckingfast.co/6mynsmjg2y9x#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part038.rar",
    "https://fuckingfast.co/l9a80kgnpvyc#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part039.rar",
    "https://fuckingfast.co/y8uoj3z2gw65#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part040.rar",
    "https://fuckingfast.co/1rbgz1u0ikdg#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part041.rar",
    "https://fuckingfast.co/efldv175di9z#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part042.rar",
    "https://fuckingfast.co/dng5mtpxz5e2#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part043.rar",
    "https://fuckingfast.co/8ikj3c6uooop#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part044.rar",
    "https://fuckingfast.co/gchifyhfzzfk#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part045.rar",
    "https://fuckingfast.co/n96k4s39e0pg#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part046.rar",
    "https://fuckingfast.co/26kz10txdmrg#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part047.rar",
    "https://fuckingfast.co/99w4gnespys4#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part048.rar",
    "https://fuckingfast.co/c0rlg43gnt31#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part049.rar",
    "https://fuckingfast.co/g65merhaq1sx#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part050.rar",
    "https://fuckingfast.co/c9ow2h12e2n8#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part051.rar",
    "https://fuckingfast.co/jzitwnp435y5#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part052.rar",
    "https://fuckingfast.co/f27xgcrik5oe#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part053.rar",
    "https://fuckingfast.co/u46cle8tbwwe#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part054.rar",
    "https://fuckingfast.co/yos1nw9t1ji9#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part055.rar",
    "https://fuckingfast.co/tohiijtgderp#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part056.rar",
    "https://fuckingfast.co/8fjlw85me7mc#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part057.rar",
    "https://fuckingfast.co/ymttd3c52li2#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part058.rar",
    "https://fuckingfast.co/aeyx7z22u1j4#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part059.rar",
    "https://fuckingfast.co/ccbh9gkmmt2w#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part060.rar",
    "https://fuckingfast.co/mufxdrze7eze#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part061.rar",
    "https://fuckingfast.co/i7x4styv0q6w#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part062.rar",
    "https://fuckingfast.co/dse0uu2qaea3#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part063.rar",
    "https://fuckingfast.co/51e2od9tdu5v#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part064.rar",
    "https://fuckingfast.co/vocyaadlqopr#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part065.rar",
    "https://fuckingfast.co/kjc3mi1r0ed0#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part066.rar",
    "https://fuckingfast.co/wr7yua488z07#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part067.rar",
    "https://fuckingfast.co/qmnafkxknxlr#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part068.rar",
    "https://fuckingfast.co/roc4w22lhwp5#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part069.rar",
    "https://fuckingfast.co/w550kz4ry2un#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part070.rar",
    "https://fuckingfast.co/l8thtpgmswkg#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part071.rar",
    "https://fuckingfast.co/osigrmjzszns#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part072.rar",
    "https://fuckingfast.co/9nnzzbvag5n7#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part073.rar",
    "https://fuckingfast.co/guy31q4wrnl0#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part074.rar",
    "https://fuckingfast.co/u7uw9ddz0yir#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part075.rar",
    "https://fuckingfast.co/rnj1xcogxak8#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part076.rar",
    "https://fuckingfast.co/bafwhe8cnciv#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part077.rar",
    "https://fuckingfast.co/1vafojydqzmd#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part078.rar",
    "https://fuckingfast.co/ntul05525f6s#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part079.rar",
    "https://fuckingfast.co/8rn3gfanvi4u#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part080.rar",
    "https://fuckingfast.co/fepolwkg8unj#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part081.rar",
    "https://fuckingfast.co/aidbtm82awap#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part082.rar",
    "https://fuckingfast.co/32wljppkp5r9#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part083.rar",
    "https://fuckingfast.co/yr8je0gm880w#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part084.rar",
    "https://fuckingfast.co/760nngqsodcp#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part085.rar",
    "https://fuckingfast.co/njbse7vkbcyr#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part086.rar",
    "https://fuckingfast.co/3xxuf81apmjw#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part087.rar",
    "https://fuckingfast.co/lhelyxrsb47q#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part088.rar",
    "https://fuckingfast.co/m3sy7uit2equ#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part089.rar",
    "https://fuckingfast.co/h5mia2dzx3lj#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part090.rar",
    "https://fuckingfast.co/giv3s3jgxf1s#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part091.rar",
    "https://fuckingfast.co/7mashlq0ygk7#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part092.rar",
    "https://fuckingfast.co/97yuf7opi8c4#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part093.rar",
    "https://fuckingfast.co/n7afmhsaco3b#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part094.rar",
    "https://fuckingfast.co/69svcsc5du7p#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part095.rar",
    "https://fuckingfast.co/bdi6j8cac5xk#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part096.rar",
    "https://fuckingfast.co/3v87lan3atcf#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part097.rar",
    "https://fuckingfast.co/miypsaa6clu3#ELDEN_RING_SotE_--_fitgirl-repacks.site_--_.part098.rar",
    "https://fuckingfast.co/049yfs6gezo9#fg-optional-bonus-content.part1.rar",
    "https://fuckingfast.co/d3j3c26y5pia#fg-optional-bonus-content.part2.rar",
    "https://fuckingfast.co/zx3b7s5ihs9v#fg-optional-bonus-content.part3.rar",
    "https://fuckingfast.co/mu9xzf50352i#fg-optional-bonus-content.part4.rar"
]

# Customize the download button selector if different
DOWNLOAD_BUTTON_ID = "link-button"

def setup_firefox(download_dir: str) -> webdriver.Firefox:
    """
    Setup Firefox options for automatic downloads and loads uBlock Origin extension.
    """
    options = Options()
    options.headless = True  # Run in headless mode (no GUI)

    # Set preferences directly on the options object
    options.set_preference("browser.download.folderList", 2)  # custom location
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/pdf,application/x-rar-compressed")  # MIME types
    options.set_preference("pdfjs.disabled", True)  # disable PDF viewer
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.manager.focusWhenStarting", False)
    options.set_preference("browser.download.useDownloadDir", True)
    options.set_preference("browser.helperApps.alwaysAsk.force", False)
    options.set_preference("browser.download.manager.alertOnEXEOpen", False)
    options.set_preference("browser.download.manager.closeWhenDone", True)
    options.set_preference("browser.download.manager.showAlertOnComplete", False)
    options.set_preference("browser.download.manager.useWindow", False)

    driver = webdriver.Firefox(options=options)

    # Add uBlock Origin extension (assumes ublock_origin.xpi is in the same directory)
    ublock_path = os.path.join(os.getcwd(), "ublock_origin.xpi")
    if os.path.exists(ublock_path):
        driver.install_addon(ublock_path, temporary=True)
        print("[*] uBlock Origin extension loaded.")
    else:
        print("[!] uBlock Origin .xpi not found. Continuing without adblock.")

    return driver

def download_from_url(driver: webdriver.Firefox, url: str, timeout: int = 15, is_first: bool = False) -> bool:
    """
    Opens the URL, clicks the download button, and returns True on success.
    Returns False if any error occurs.
    Tries JavaScript click if normal click is intercepted.
    If is_first is True, waits extra time after page load for adblocker/page to settle.
    """
    try:
        driver.get(url)
        if is_first:
            print("[*] Waiting extra 6 seconds for first URL to allow adblocker/page to settle...")
            time.sleep(6)
        wait = WebDriverWait(driver, timeout)
        download_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, DOWNLOAD_BUTTON_ID))
        )
        try:
            download_button.click()
        except Exception as click_error:
            # If click is intercepted, try JavaScript click
            print(f"[!] Normal click failed, trying JavaScript click: {click_error}")
            driver.execute_script("arguments[0].click();", download_button)
        print(f"[+] Download triggered at {url}")
        return True
    except TimeoutException:
        print(f"[-] Timeout: Download button not found or clickable at {url}")
    except NoSuchElementException:
        print(f"[-] Error: Download button with id '{DOWNLOAD_BUTTON_ID}' not found at {url}")
    except Exception as e:
        print(f"[-] Unexpected error at {url}: {e}")
    return False

def is_file_complete(filename):
    """
    Returns True if the file exists and is not a partial download.
    """
    return os.path.exists(filename) and not filename.endswith('.part')

def get_target_filename_from_url(url):
    """
    Extracts the intended filename from the URL hash (after #).
    """
    if '#' in url:
        return url.split('#')[-1]
    return None

def remove_stale_partial_file(filepath, max_age_hours=1):
    """
    If a .part file exists and is older than max_age_hours, delete it.
    """
    if os.path.exists(filepath):
        mtime = os.path.getmtime(filepath)
        age_hours = (time.time() - mtime) / 3600
        if age_hours > max_age_hours:
            print(f"[!] Removing stale partial file: {filepath}")
            os.remove(filepath)
            return True
    return False

def main():
    # Create download folder if it doesn't exist
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    driver = setup_firefox(DOWNLOAD_DIR)
    print("[*] Firefox driver initialized.")

    success_count = 0
    for idx, url in enumerate(URLS):
        is_first = (idx == 0)
        target_filename = get_target_filename_from_url(url)
        if not target_filename:
            print(f"[!] Could not determine filename for URL: {url}")
            continue
        final_path = os.path.join(DOWNLOAD_DIR, target_filename)
        part_path = final_path + ".part"
        # Special case for part098
        if "part098" in target_filename:
            min_size_mb = 41
        else:
            min_size_mb = 500
        # If a .part file exists and is less than threshold, treat as incomplete and delete
        if os.path.exists(part_path):
            part_size_mb = os.path.getsize(part_path) / (1024 * 1024)
            if part_size_mb < min_size_mb:
                print(f"[!] Incomplete .part file found (<{min_size_mb}MB), deleting: {os.path.basename(part_path)}")
                os.remove(part_path)
        # If the final file exists and is less than threshold, treat as incomplete and delete
        if os.path.exists(final_path):
            file_size_mb = os.path.getsize(final_path) / (1024 * 1024)
            if file_size_mb < min_size_mb:
                print(f"[!] Incomplete file found (<{min_size_mb}MB), deleting: {os.path.basename(final_path)}")
                os.remove(final_path)
            else:
                print(f"[=] File already exists and is >={min_size_mb}MB, skipping: {target_filename}")
                continue
        if download_from_url(driver, url, is_first=is_first):
            success_count += 1
        time.sleep(10)

    print(f"[*] Completed initiation of downloads: {success_count}/{len(URLS)}")
    print("[!] Firefox will remain open so downloads can finish. Close it manually when all downloads are done.")
    # driver.quit()  # Disabled to keep browser open for downloads

if __name__ == "__main__":
    main()