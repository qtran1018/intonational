from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests
import asyncio
import time
import csv

async def do_scrape():
    links = await get_country_links()
    print("### Finished getting links ###")
    country_data = await get_country_data(links)
    print("### Finished getting country data ###")
    return country_data

async def get_country_links():
    country_list = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://travel.state.gov/en/international-travel/travel-advisories.html")
        select = page.locator("select.datatable-selector[name='per-page']")
        await select.select_option("25")

        pagination_buttons = await page.query_selector_all("ul.datatable-pagination-list li button")
        num_pages = len(pagination_buttons)
        
        for i in range(2, num_pages+1):
            await page.wait_for_load_state("networkidle")

            button = await page.query_selector(f"ul.datatable-pagination-list li button[data-page='{i}']")

            #Get country links
            locator = page.locator("table#htmlTable tbody tr th a")
            count = await locator.count()
            for i in range(count):
                name = await locator.nth(i).inner_text()
                name = name.replace("(opens in a new tab)","").strip()
                href = await locator.nth(i).get_attribute("href")
                if href[0] == '/':
                    href = "https://travel.state.gov" + href
                country_list[name] = href
            if not button:
                print(f"Button for page {i} not found, skipping...")
                continue
            
            await button.click()
            await asyncio.sleep(0.5)

        with open('app/data/country_links.csv', 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for country, link in country_list.items():
                writer.writerow([country, link])
        await browser.close()
    
    return country_list

async def get_country_data(links):
    country_links = links
    country_data: list[dict] = []
    
    # Requests session with headers - not used with Playwright
    # session = requests.Session()
    # session.headers.update({
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    # })

    # Write to CSV file - another csv comment at the bottom
    # with open('app/data/country_data.csv', 'w', newline='', encoding="utf-8") as csvfile:
    #     writer = csv.writer(csvfile)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for key, value in country_links.items():
            name = key
            link = value
            date = None
            level = None
            notes = None
            passport_validity = None
            passport_pages = None
            visa = None
            vaccinations = None
            currency_entry = None
            currency_exit = None

            print(f"Getting data for {name}")

            # Response implementation. Replaced with Playwright.
            # try:
            #     response = session.get(link, allow_redirects=True)
            # except requests.exceptions.TooManyRedirects:
            #     print(f"Too many redirects for {link}")
            #     continue  # skip this country or handle differently
            
            page = await browser.new_page()
            await page.goto(link, wait_until="domcontentloaded")
            response = await page.content()

            soup = BeautifulSoup(response, 'html.parser')
            page_version_checker = soup.find("div", class_="herocontainer container responsivegrid")
                
            # newer format, less common, sporadic adoption
            if page_version_checker:
                date = soup.find("div", class_="cmp-traveladvisory__header-date-issued").get_text(strip=True).replace("Date issued: ","").replace(" -advisory history","").strip()
                level = soup.find("h3", class_="travel-level").get_text(strip=True)
                notes = soup.find("span", class_="body-regular").get_text(strip=True)
                visa = soup.find_all("div", class_="iconcallout-right")[0].get_text(strip=True, separator=" ").replace("Tourist visa requirements", "").strip()
                vaccinations = soup.find_all("div", class_="iconcallout-right")[1].get_text(strip=True, separator=" ").replace("Vaccinations", "").strip()
                passport_requirements = soup.find_all("div", class_="iconcallout-right")[2].get_text(strip=True, separator=" ").replace("Valid passport requirements", "").strip()
                currency_restrictions = soup.find_all("div", class_="iconcallout-right")[3].get_text(strip=True, separator=" ").replace("Currency on entry and exit", "").strip()
            
            # old format, still more common
            elif page_version_checker is None:
                date = soup.find("div", class_="tsg-rwd-eab-date-frame").get_text(strip=True)
                level = soup.find("h3", class_="tsg-rwd-eab-title-frame").get_text(strip=True).replace(f"{name} - ", "")
                notes = soup.find("div", class_="tsg-rwd-alert-teaser").get_text(strip=True)
                visa = soup.find_all("div", class_="tsg-rwd-qf-box-data")[2].get_text(strip=True)
                vaccinations = soup.find_all("div", class_="tsg-rwd-qf-box-data")[3].get_text(strip=True)

                passport_validity = soup.find_all("div", class_="tsg-rwd-qf-box-data")[0].get_text(strip=True)
                passport_pages = soup.find_all("div", class_="tsg-rwd-qf-box-data")[1].get_text(strip=True)
                passport_requirements = passport_validity + ". " + passport_pages
                
                currency_entry = soup.find_all("div", class_="tsg-rwd-qf-box-data")[4].get_text(strip=True)
                currency_exit = soup.find_all("div", class_="tsg-rwd-qf-box-data")[5].get_text(strip=True)

                # AI recommened fix because mine is too "hacky" and doesn't catch mulitple-period edge cases.
                currency_restrictions = ". ".join(s.strip(".") for s in [currency_entry, currency_exit]) + "."
                # currency_restrictions = currency_entry + ". " + currency_exit + "."
                # currency_restrictions = currency_restrictions.replace("..", ".")

            data = {
                "name": name,
                "link": link,
                "date": date,
                "level": level,
                "notes": notes,
                "visa": visa,
                "vaccinations": vaccinations,
                "passport_requirements": passport_requirements,
                "currency_restrictions": currency_restrictions
            }
            country_data.append(data)
            await page.close()

            # Write to CSV
            # writer.writerow([name, link, date, level, notes, visa, vaccinations, passport_requirements, currency_restrictions])
            await asyncio.sleep(1)

        await browser.close()
    print("### All country data scraped ###")
    return country_data

asyncio.run(do_scrape())
