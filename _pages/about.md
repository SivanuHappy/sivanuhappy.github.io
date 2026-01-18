---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data.json" %}

<span class='anchor' id='about-me'></span>

# About Me

I am a **Research Scientist** at the **George Mason University**. I received my **Ph.D. in Earth Systems and Geoinformation Science** from George Mason University in December 2025.

My research focuses on developing deep learning models for air quality monitoring, including LSTM-based PM₂.₅ calibration models and uncertainty quantification frameworks. I am passionate about applying **Geospatial AI**, **Remote Sensing**, and **Spatial Data Fusion** techniques to environmental and public health challenges.

I received my M.Tech. in Remote Sensing from Anna University where I was awarded the **Gold Medal (First Rank)**, and M.S. in Information Systems from Illinois State University.

My publications have been cited <a href='https://scholar.google.com/citations?user=vDCNltwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> times.


# 🔬 Research Interests

- Remote Sensing for Air Quality Monitoring
- Geospatial AI/ML
- Uncertainty Quantification
- Spatial Data Fusion
- Deep Learning
- Geographic Information Systems
- Spatial Cloud Computing


# 🔥 News

- *2026.01*: &nbsp;🎉 Joined as **Research Scientist** at George Mason University
- *2025.12*: &nbsp;🎓 Completed **Ph.D.** in Earth Systems and Geoinformation Science from George Mason University
- *2025*: &nbsp;📄 Paper published in **GIScience & Remote Sensing** on AOD imputation using GAIN model
- *2025*: &nbsp;📄 Paper accepted in **International Journal of Big Earth Data** on uncertainty quantification
- *2024*: &nbsp;🎤 Paper presented at **ACM SIGSPATIAL Workshop** on multi-source data fusion
- *2023*: &nbsp;📄 Paper published in **International Journal of Digital Earth** on Ukraine air quality


# 📖 Education

- *2020.08 - 2025.12*, **Ph.D. in Earth Systems and Geoinformation Science**, George Mason University, USA
- *2016.08 - 2018.05*, **M.S. in Information Systems**, Illinois State University, USA
- *2010.09 - 2012.05*, **M.Tech. in Remote Sensing**, Anna University, India 🏆 **Gold Medalist (First Rank)**
- *2006.09 - 2010.05*, **B.E. in Computer Science**, Anna University, India


# 💼 Experience

- *2026.01 - Present*, **Research Scientist**, NSF Spatiotemporal Innovation Center, George Mason University
  - Conducting research on geospatial AI and remote sensing applications for environmental monitoring
  - Developing advanced deep learning models for air quality prediction and calibration

- *2020.08 - 2025.12*, **Graduate Research Assistant**, NSF Spatiotemporal Innovation Center, George Mason University
  - Led development of LSTM-based PM₂.₅ calibration models for low-cost sensors (PurpleAir, Clarity)
  - Designed uncertainty quantification framework for calibrated air quality estimates
  - Built Science Data Analytics Platform (SDAP) API services for operational deployment

- *2013.09 - 2014.04*, **Junior Research Fellow**, Indian Space Research Organization (ISRO)
  - Processed geospatial datasets from Indian Remote Sensing satellites
  - Automated radiometric correction workflows in MATLAB
  - Developed ML models for forest cover classification


# 📝 Selected Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GIScience & Remote Sensing 2025</div><img src='images/paper_aod.png' alt="AOD Paper" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Optimizing GAIN model to improve AOD imputation using MODIS MAIAC data and multi-source data fusion**

**Anusha S. Malarvizhi**, Peng Pan, Tyler Stover, Dingding Sun, Chaowei Yang

[**Paper**](https://doi.org/10.1080/15481603.2025.2571244) | *GIScience & Remote Sensing, 2025*

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Int. J. Digital Earth 2023</div><img src='images/paper_ukraine.png' alt="Ukraine Paper" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**The spatial dynamics of Ukraine air quality impacted by the war and pandemic**

**Anusha S. Malarvizhi**, Qian Liu, Thomas S. Trefonides, et al.

[**Paper**](https://doi.org/10.1080/17538947.2023.2239762) | <span class='show_paper_citations' data='vDCNltwAAAAJ:2osOgNQ5qMEC'></span> | *International Journal of Digital Earth, 16(1), 3680-3705, 2023*

</div>
</div>


## Journal Articles

- **Uncertainty quantification in geospatial AI/ML applications: Methods, metrics, and open-source support with an air quality use case**  
  **A.S. Malarvizhi**, K. Smith, C. Yang  
  *International Journal of Big Earth Data*, 2025 (in press)

- **Multi-source data fusion for filling gaps in satellite Aerosol Optical Depth (AOD) using generative models**  
  **A.S. Malarvizhi**, P. Pan  
  *ACM SIGSPATIAL Workshop on Spatial Big Data and AI*, pp. 28-38, 2024  
  [DOI](https://doi.org/10.1145/3681763.3698467) | <span class='show_paper_citations' data='vDCNltwAAAAJ:UebtZRa9Y70C'></span>

- **An Open-Source Workflow for Spatiotemporal Studies with COVID-19 as an Example**  
  **A.S. Malarvizhi**, Q. Liu, D. Sha, H. Lan, C. Yang  
  *ISPRS International Journal of Geo-Information*, 11(1), 2022  
  [DOI](https://doi.org/10.3390/ijgi11010013) | <span class='show_paper_citations' data='vDCNltwAAAAJ:2osOgNQ5qMEC'></span>

- **Data Augmentation Strategies for Improved PM2.5 Forecasting Using Transformer Architectures**  
  P. Pan, **A.S. Malarvizhi**, C. Yang  
  *Atmosphere*, 16(2), 2025  
  [DOI](https://doi.org/10.3390/atmos16020127) | <span class='show_paper_citations' data='vDCNltwAAAAJ:Se3iqnhoufwC'></span>

- **Spatiotemporal changes in global nitrogen dioxide emission due to COVID-19 mitigation policies**  
  Q. Liu, **A.S. Malarvizhi**, W. Liu, et al.  
  *Science of the Total Environment*, 776, 146027, 2021  
  [DOI](https://doi.org/10.1016/j.scitotenv.2021.146027) | <span class='show_paper_citations' data='vDCNltwAAAAJ:u-x6o8ySG0sC'></span>

- **A State-Level Socioeconomic Data Collection of the United States for COVID-19 Research**  
  D. Sha, **A.S. Malarvizhi**, Q. Liu, et al.  
  *Data*, 5(4), 2020  
  [DOI](https://doi.org/10.3390/data5040118) | <span class='show_paper_citations' data='vDCNltwAAAAJ:u5HHmVD_uO8C'></span>

- **A Systematic Study of Popular Software Packages and AI/ML Models for Calibrating In Situ Air Quality Data**  
  S. Smith, T. Trefonides, **A. Srirenganathan Malarvizhi**, et al.  
  *Sensors*, 25(4), 2025  
  [DOI](https://doi.org/10.3390/s25041028) | <span class='show_paper_citations' data='vDCNltwAAAAJ:hqOjcs7Dif8C'></span>

- **COVID-Scraper: An Open-Source Toolset for Automatically Scraping and Processing Global Multi-Scale Spatiotemporal COVID-19 Records**  
  H. Lan, D. Sha, **A.S. Malarvizhi**, et al.  
  *IEEE Access*, 9, 84783-84798, 2021  
  [DOI](https://doi.org/10.1109/access.2021.3085682) | <span class='show_paper_citations' data='vDCNltwAAAAJ:d1gkVwhDpl0C'></span>

- **Spatiotemporal Analysis of Sea Ice Leads in the Arctic Ocean**  
  D. Sha, Y. Koo, X. Miao, **A. Srirenganathan**, et al.  
  *Remote Sensing*, 13(20), 2021  
  [DOI](https://doi.org/10.3390/rs13204177) | <span class='show_paper_citations' data='vDCNltwAAAAJ:IjCSPb-OGe4C'></span>

- **Optimizing context-based location extraction by tuning open-source LLMs with RAG**  
  Z. Wang, Y. Masri, **A.S. Malarvizhi**, et al.  
  *International Journal of Digital Earth*, 18(1), 2521786, 2025  
  [DOI](https://doi.org/10.1080/17538947.2024.2521786) | <span class='show_paper_citations' data='vDCNltwAAAAJ:0EnyYjriUFMC'></span>


## Book Chapters

- **ArcCI: A high-resolution aerial image management and processing platform for sea ice**  
  D. Sha, **A.S. Malarvizhi**, H. Lan, et al.  
  *Recent Advancement in Geoinformatics and Data Science*, Vol. 558, Geological Society of America, 2023  
  [DOI](https://doi.org/10.1130/2022.2558(06)) | <span class='show_paper_citations' data='vDCNltwAAAAJ:zYLM7Y9cAGgC'></span>


# 🛠️ Technical Skills

| Category | Skills |
|----------|--------|
| **Programming** | Python, R, MATLAB, JavaScript |
| **Deep Learning** | PyTorch, TensorFlow |
| **Containerization** | Docker, Kubernetes |
| **Databases** | PostgreSQL (PostGIS), MySQL |
| **Geospatial** | Google Earth Engine, ArcGIS Pro |


# 🏆 Honors & Awards

- *2010-2012* **Gold Medalist (First Rank in University)** - M.Tech., Anna University


# 👩‍🏫 Teaching & Mentoring

- *2017.08 - 2018.05*, **Graduate Teaching Assistant**, Illinois State University
- *2020 - 2025 (Summers)*, **Mentor**, Aspiring Scientists Summer Internship Program (ASSIP), George Mason University
- *2022.08 - Present*, **Mentor**, NSF Skills Training in Advanced Research & Technology (START) Program