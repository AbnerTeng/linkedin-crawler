# linkedin-crawler

An util to crawl linkedin job description and requirements.

#### 1. Clone repo

```plaintext
git clone https://github.com/AbnerTeng/linkedin-crawler.git
```

```plaintext
gh repo clone AbnerTeng/linkedin-crawler
```

#### 2. Setup ChromeDriver

The default path of `ChromeDriver` is 

```plaintext
/usr/local/bin/chromedriver.exe
```

You can modify the path in `dyna_crawl_setup.py`

#### 3. Arguments

- `-key `: Keyword of the job or industry. Default is `Machine%20Learning`
- `-loc `: Location of the job. Default is `Taipei%20City%2C%20Taiwan `
- `-type `: Type of the job, ex: Part-time, Full-time, etc.... Default types nothing, it represents ALL type of jobs
- `-path1 `and `-path2 `: Path to save `job_df.csv` and `descrip_df.csv`
- `-wc `: Whether to generate wordcloud of job description  and requirements. Default is `False`

#### 4. CLI
```plaintext
python3 main.py -key <key> -loc <loc> -type <type> -path1 <path1> -path2 <path2> -wc <True / False>
```
