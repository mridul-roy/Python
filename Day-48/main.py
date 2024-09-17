from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(
    "https://www.amazon.com/Razer-Ambidextrous-Gaming-Optical-Lighting/dp/B081DH26MQ/ref=slsr_d_dpds_fsdp4star_fa_xcat_cheapdynam_d_sccl_3_2/132-2415296-8141504?pd_rd_i=B081DH26MQ")

dollar_price = driver.find_element(By.CLASS_NAME,value="aok-offscreen")
print(f"The price is {dollar_price}")

driver.quit()
