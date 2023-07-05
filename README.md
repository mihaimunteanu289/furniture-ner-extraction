<h1>Furniture Named Entity Recognition (NER) Extraction</h1>

<p>This repository contains the source code for a Named Entity Recognition (NER) model that has been trained to identify product names from various furniture store websites.</p>

<h2>Project Overview</h2>

<p>The goal of this project is to extract product names from a list of URLs of furniture stores. The approach employed here is based on creating a NER model and training it to identify the 'PRODUCT' entities. The model is created using transformer architecture from HuggingFace Transformers library.</p>

<p>The entire project is divided into multiple Jupyter notebooks each detailing a step in the pipeline from data collection to model training.</p>

<h2>Repository Structure</h2>

<p>Here is a brief explanation of what each part of this repository covers:</p>

<ol>
<li><code>data</code>: Contains the input files for URLs as well as the generated files after data extraction.</li>
<li><code>logs</code>: Contains the log files generated during the execution of the code.</li>
<li><code>url_crawling</code>: Contains the files related to the crawling of websites from the input URLs.</li>
<li><code>1. raw_analysis.ipynb</code>: This notebook includes initial analysis of the given URLs, checking their validity and reachability.</li>
<li><code>2. crawl_analysis.ipynb</code>: This notebook deals with the crawling process of the websites to extract useful data.</li>
<li><code>3. data_preprocessing.ipynb</code>: In this notebook, the extracted raw data is cleaned and prepared for the model.</li>
<li><code>4. create_dataframe.ipynb</code>: This notebook includes the process of transforming the processed data into a structured dataframe.</li>
<li><code>5. model_training.ipynb</code>: This notebook includes the process of training the NER model using the prepared data.</li>
<li><code>README.md</code>: The file that provides an overview of the project and the repository.</li>
</ol>

<h2>Getting Started</h2>

<p>To get started with the project:</p>

<ol>
<li>Clone the repository using Git: <code>git clone https://github.com/mihaimunteanu289/furniture-ner-extraction.git</code>.</li>
<li>Install the necessary dependencies. This project requires Python 3.10</li>
<li>Run the notebooks in order.</li>
</ol>

<h2>Authors</h2>

<ul>
<li><strong>Mihai Munteanu</strong> - <a href="https://github.com/mihaimunteanu289">mihaimunteanu289</a></li>
</ul>
