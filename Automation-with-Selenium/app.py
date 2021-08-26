from pathlib import Path
from time import sleep
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver

gecko = GetGeckoDriver()
gecko.install()


def get_driver(downloads: Path) -> webdriver:
    """Setup webdriver options.

    Download PDF from firefox:
    https://stackoverflow.com/a/30455695
    """
    mime_types = "".join(
        [
            "application/pdf",
            "application/vnd.adobe.xfdf",
            "application/vnd.fdf",
            "application/vnd.adobe.xdp+xml",
        ]
    )
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", str(downloads))
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
    profile.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    profile.set_preference("pdfjs.disabled", True)

    driver = webdriver.Firefox(firefox_profile=profile)
    return driver


def rename_file(
    downloads: Path,
    new_name: str,
    old_name: str = "retrievePDF.pdf",
    wait_time: int = 1,
) -> None:
    """Rename downloaded file.

    If the file is not found, the function will wait for the file to be
    `new_name`. Otherwise, it will print a message and exit.
    """
    sleep(wait_time)
    file = downloads / old_name
    if file.exists():
        file.rename(file.with_stem(new_name))
    else:
        print(new_name)


def get_proof(tracking: str, downloads: Path) -> None:
    driver = get_driver(downloads)
    url = f"https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber={tracking}"
    driver.get(url)

    clicks = [
        ('//button[@class="eye-brow-link"][contains(text(),"Proof")]', 3),
        ('//*[@class="pod"]//button[contains(text(), "View PDF")]', 1),
    ]
    for xpath, wait_time in clicks:
        driver.implicitly_wait(wait_time)
        elem = driver.find_element_by_xpath(xpath)
        elem.click()

    driver.close()
    rename_file(downloads, f"Proof_for_{tracking}")


if __name__ == "__main__":
    downloads = Path().resolve() / "proofs"
    tracking_numbers = ["000000000000"]
    for tracking in tracking_numbers:
        get_proof(tracking, downloads)
