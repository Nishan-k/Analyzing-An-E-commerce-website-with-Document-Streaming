
# Real-time Ecommerce Analytics End-To-End:

<img src="./images/workflow.png" alt="DE-workflow" title="Data Pipeline Worflow">

## Goal Of The Project:
Analyze use behavior of an E-commerce wesbite in real-time using Kafka.


## Table of Contents:
<ol>
    <li><a href="#about_the_data"> <b>About The Data </a></b></li>
    <li><a href="#used_steps_tools"><b>Used Steps & Tools</b>
        <ul>
        <li><a href="#tools"><b> Tools Used </a> </b></li>
        <li><a href="#ingestion"><b> Data Ingestion </a> </b></li>
        <li><a href="#loading"><b> Data Loading </a> </b></li>
        <li><a href="#viz"><b> Visualization </a> </b></li>
        </ul>
    </li>
</ol>


<h3 id ="about_the_data">1. About The Data:</h3>
The data used in this project was downloaded from Kaggle.
<a href="https://www.kaggle.com/datasets/carrie1/ecommerce-data">Link to the data source. </a>
In total, the data has 8 columns.

<h3 id="used_steps_tools">2. Used Steps & Tools:</h3>
<ul>
    <h4 id="tools">Tools Used:</h4>
    FastAPI, Postman, Apache Kafka, Spark Streaming, MongoDB, Streamlit and Docker.
    <li> Steps: </li>
    <h4 id="ingestion">Data Ingestion:</h4>
    <li>Read the CSV file as a Dataframe, and converted each row into a JSON per record. </li>
    <li> Created an API to validate the data type and the number of columns to be passed inheriting the BaseModel.
    <h4 id="loading">Data Loading:</h4>
    <li> Created a topic in Aapche kafka, ingestion-topic, where we sent the data from the API, each JSON records which were converted in the first step. Here linecache has been used to send the JSON.
    <li> Then Apache Streaming has acted as a consumer, consuming the data from the ingestion-topic.
    <li> Created a database named docstreaming in MongoDB and a collection inside that database named invoices.
    <li> Then the data that were being consumed by Spark Streaming will be written into the invoices.
    <h4 id="viz">Visualization:</h4>
    <li> Finally, from Streamlit, we connect to the MongoDB database (docstreaming) and visualize the data in dashboard using Streamlit. 
</ul>