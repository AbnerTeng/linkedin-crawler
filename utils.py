"""Elements of the crawling process"""
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dyna_crawl_setup import init_setup
from tqdm import tqdm


def elements(driver):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(("css selector", "h1 > span"))
    )
    no_of_jobs = int(element.get_attribute("innerText"))

    i = 2
    for j in tqdm(range(100)):
        while(i <= int(no_of_jobs /25) + 1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i += 1
            try:
                driver.find_element(By.XPATH, "/html/body/main/div/selection/button").click()
            except:
                pass
                time.sleep(3)

def count_jobs(driver):
    job_num = driver.title.split(" ")[0]
    print(f"Total number of jobs: {job_num}")

def get_job_lst(driver):
    job_lst = driver.find_element(By.CLASS_NAME, "jobs-search__results-list")
    jobs = job_lst.find_elements(By.TAG_NAME, "li")
    return jobs

def get_job_infos(jobs, driver):
    job_title_lst = []
    job_comp_lst = []

    for job in jobs:
        job_title = job.find_element(By.CSS_SELECTOR, "h3").get_attribute("innerText")
        job_title_lst.append(job_title)
        job_comp = job.find_element(By.CSS_SELECTOR, "h4").get_attribute("innerText")
        job_comp_lst.append(job_comp)

    job_descrip = []

    for i in range(len(jobs)):
        try:
            job_click_path = f'/html/body/div[1]/div/main/section[2]/ul/li[{i+1}]/div/div[1]/img'
            job_click = driver.find_element(By.XPATH, job_click_path)
            driver.execute_script("arguments[0].click();", job_click)
            time.sleep(1)
            job_descrip_path = f'/html/body/div[1]/div/section/div[2]/div/section[1]/div/div'
            job_descrip_lst = job.find_element(By.XPATH, job_descrip_path).get_attribute("innerText")
            job_descrip.append(job_descrip_lst)
        
        except:
            continue
    
    return job_title_lst, job_comp_lst, job_descrip

def to_df(job_title_lst, job_comp_lst, job_descrip, path1, path2):
    job_df = pd.DataFrame(
            {
                "job_title": job_title_lst,
                "job_comp": job_comp_lst,
            }
        )
    descrip_df = pd.DataFrame(job_descrip, columns = ["job_descrip"])
    descrip_df['job_descrip'] = descrip_df['job_descrip'].str.replace('\n', '')
    job_df.to_csv(path1, index = False, encoding = "utf-8-sig")
    descrip_df.to_csv(path2, index = False, encoding = "utf-8-sig") 


    
