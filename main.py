"""Main file to run"""
from dyna_crawl_setup import init_setup
from utils import elements, count_jobs, get_job_lst, get_job_infos, to_df
from argparse import ArgumentParser
from merge_df import get_full_df
from lang_proc import process_text, clean_lst, wc

parser = ArgumentParser()
parser.add_argument('-key', '-keyword', type = str, default = "Machine%20Learning", help = "Keyword of the job")
parser.add_argument('-loc', '-location', type = str, default = "Taipei%20City%2C%20Taiwan", help = "Location of the job")
parser.add_argument('-type', '-type', type = str, default = " ", help = "Type of the job, ex: Part-time, Full-time, intern, etc.")
parser.add_argument('-path1', '-path1', type = str, default = "job_df.csv", help = "Path to save the job_df.csv")
parser.add_argument('-path2', '-path2', type = str, default = "descrip_df.csv", help = "Path to save the descrip_df.csv")
parser.add_argument('-path3', '-path3', type = str, default = "big_df.csv", help = "Path to save the big_df.csv")
args = parser.parse_args()

def main():
    driver = init_setup()
    url = f"https://www.linkedin.com/jobs/search?keywords={args.key}&location={args.loc}&locationId=&geoId=111879105&f_TPR={args.type}&position=1&pageNum=0"
    driver.get(url)

    elements(driver)
    count_jobs(driver)
    jobs = get_job_lst(driver)
    job_title_lst, job_comp_lst, job_descrip = get_job_infos(jobs, driver)
    to_df(job_title_lst, job_comp_lst, job_descrip, args.path1, args.path2)
    ## get_full_df(args.path3)
    descrip_lst = process_text(args.path2)
    clean_lst_2 = clean_lst(descrip_lst)
    wc(clean_lst_2)

if __name__ == "__main__":
    main()

