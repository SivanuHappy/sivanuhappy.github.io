<h1 align="center">
Anusha Srirenganathan Malarvizhi
</h1>

<div align="center">

**Research Scientist | George Mason University**

[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-Profile-blue?logo=googlescholar)](https://scholar.google.com/citations?user=vDCNltwAAAAJ)

</div>

<p align="center">Academic Personal Homepage</p>

<p align="center">
    <br>
    <img src="docs/screenshot.png" width="100%"/>
    <br>
</p>

**Live Site:** [https://SivanuHappy.github.io](https://SivanuHappy.github.io)

## About

This is my academic personal homepage showcasing my research in:
- Remote Sensing for Air Quality Monitoring
- Geospatial AI/ML
- Uncertainty Quantification
- Spatial Data Fusion
- Deep Learning

## Key Features

- **Automatically update google scholar citations**: using the google scholar crawler and github action, citations update automatically.
- **Support Google analytics**: trace the traffic of the homepage.
- **Responsive**: automatically adjusts for different screen sizes and viewports.
- **Beautiful and Simple Design**: suitable for academic personal homepage.
- **SEO**: search Engine Optimization helps search engines find the information easily.

## Setup

1. Clone this repo
2. Configure Google Scholar citation crawler:
    1. Set `GOOGLE_SCHOLAR_ID` in `Settings -> Secrets -> Actions -> New repository secret`
    2. Enable workflows in `Actions` tab
3. Modify `_config.yml` with your information
4. Add content in `_pages/about.md`
5. Site publishes at `https://SivanuHappy.github.io`

## Debug Locally

1. Clone repo using `git clone`
2. Install Jekyll environment (`Ruby`, `RubyGems`, `GCC`, `Make`)
3. Run `bash run_server.sh`
4. Open http://127.0.0.1:4000

